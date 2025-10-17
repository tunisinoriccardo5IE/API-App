from services.spotify_client import SpotifyClient
from services.telegram_client import TelegramClient

def search_song(query):
    spotify_client = SpotifyClient()
    results = spotify_client.search_songs(query)
    formatted_results = format_search_results(results)
    return formatted_results

def search_artist(query):
    spotify_client = SpotifyClient()
    results = spotify_client.search_artists(query)
    formatted_results = format_search_results(results)
    return formatted_results

def search_playlist(query):
    spotify_client = SpotifyClient()
    results = spotify_client.search_playlists(query)
    formatted_results = format_search_results(results)
    return formatted_results

def format_search_results(results):
    formatted = []
    for item in results:
        formatted.append(f"{item['name']} by {item['artist']} - {item['url']}")
    return "\n".join(formatted) if formatted else "No results found."