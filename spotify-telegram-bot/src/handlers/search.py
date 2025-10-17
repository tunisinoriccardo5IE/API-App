from src.services.spotify_client import SpotifyClient

try:
    import importlib
    config = importlib.import_module("src.config")
    SEARCH_LIMIT = getattr(config, "SEARCH_LIMIT", 10)
except Exception:
    # Fallback search limit when src.config does not define SEARCH_LIMIT
    SEARCH_LIMIT = 10


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