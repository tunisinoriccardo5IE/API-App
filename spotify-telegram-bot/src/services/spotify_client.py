import base64
import time
from urllib.parse import urlencode
import os
from typing import Optional

import requests

# Read Spotify credentials from environment if available; class __init__ will use env vars when not passed
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

class SpotifyClient:
    def __init__(self, client_id: Optional[str] = None, client_secret: Optional[str] = None):
        self.client_id = client_id or SPOTIFY_CLIENT_ID
        self.client_secret = client_secret or SPOTIFY_CLIENT_SECRET
        self.token = None
        self.token_expires_at = 0
        self.auth_url = "https://accounts.spotify.com/api/token"
        self.base_url = "https://api.spotify.com/v1"
        self.base_url = "https://api.spotify.com/v1"

    def authenticate(self):
        if not self.client_id or not self.client_secret:
            raise RuntimeError("SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET must be set in env/.env")
        # reuse token if not expired (with 30s buffer)
        if self.token and time.time() < self.token_expires_at - 30:
            return self.token

        creds = f"{self.client_id}:{self.client_secret}".encode("utf-8")
        b64 = base64.b64encode(creds).decode("utf-8")
        headers = {"Authorization": f"Basic {b64}", "Content-Type": "application/x-www-form-urlencoded"}
        data = {"grant_type": "client_credentials"}

        r = requests.post(self.auth_url, headers=headers, data=data, timeout=10)
        r.raise_for_status()
        payload = r.json()
        self.token = payload.get("access_token")
        expires_in = int(payload.get("expires_in", 3600))
        self.token_expires_at = time.time() + expires_in
        return self.token

    def _headers(self):
        token = self.authenticate()
        return {"Authorization": f"Bearer {token}"}
    def get_track(self, track_id):
        """Get Spotify track information by track ID."""
        if not track_id:
            return None
        try:
            url = f"{self.base_url}/tracks/{track_id}"
            r = requests.get(url, headers=self._headers(), timeout=10)
            r.raise_for_status()
            it = r.json()
            thumb = None
            images = it.get("album", {}).get("images") or []
            if images:
                thumb = images[0].get("url")
            return {
                "id": it.get("id"),
                "name": it.get("name"),
                "url": it.get("external_urls", {}).get("spotify"),
                "thumbnail": thumb,
                "preview_url": it.get("preview_url"),
                "artists": [a.get("name") for a in it.get("artists", [])]
            }
        except Exception as e:
            print(f"Error getting track: {e}")
            return None
    def search(self, q: str, type_: str, limit: int = 10):
        if not q:
            return []
        params = {"q": q, "type": type_, "limit": limit}
        url = f"{self.base_url}/search?{urlencode(params)}"
        r = requests.get(url, headers=self._headers(), timeout=10)
        r.raise_for_status()
        data = r.json()
        results = []

        if type_ == "track":
            items = data.get("tracks", {}).get("items", [])
            for it in items:
                thumb = None
                images = it.get("album", {}).get("images") or []
                if images:
                    thumb = images[0].get("url")
                results.append({
                    "id": it.get("id"),
                    "name": it.get("name"),
                    "url": it.get("external_urls", {}).get("spotify"),
                    "thumbnail": thumb,
                    "preview_url": it.get("preview_url"),
                    "artists": [a.get("name") for a in it.get("artists", [])]
                })

        elif type_ == "artist":
            items = data.get("artists", {}).get("items", [])
            for it in items:
                images = it.get("images") or []
                thumb = images[0].get("url") if images else None
                results.append({
                    "id": it.get("id"),
                    "name": it.get("name"),
                    "url": it.get("external_urls", {}).get("spotify"),
                    "thumbnail": thumb
                })

        elif type_ == "playlist":
            items = data.get("playlists", {}).get("items", [])
            for it in items:
                images = it.get("images") or []
                thumb = images[0].get("url") if images else None
                results.append({
                    "id": it.get("id"),
                    "name": it.get("name"),
                    "url": it.get("external_urls", {}).get("spotify"),
                    "thumbnail": thumb,
                    "description": it.get("description")
                })

        return results