from src.services.spotify_client import SpotifyClient
from src.config import SEARCH_LIMIT


def search_song(query: str):
    client = SpotifyClient()
    client.authenticate()
    return client.search(query, "track", limit=SEARCH_LIMIT)


def search_artist(query: str):
    client = SpotifyClient()
    client.authenticate()
    return client.search(query, "artist", limit=SEARCH_LIMIT)


def search_playlist(query: str):
    client = SpotifyClient()
    client.authenticate()
    return client.search(query, "playlist", limit=SEARCH_LIMIT)