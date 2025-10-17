import unittest
from src.handlers.search import search_song, search_artist, search_playlist
from src.services.spotify_client import SpotifyClient

class TestSearchFunctions(unittest.TestCase):

    def setUp(self):
        self.spotify_client = SpotifyClient()
        self.spotify_client.authenticate()  # Assuming there's an authenticate method

    def test_search_song(self):
        result = search_song("Shape of You")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Shape of You", [song['name'] for song in result])

    def test_search_artist(self):
        result = search_artist("Ed Sheeran")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Ed Sheeran", [artist['name'] for artist in result])

    def test_search_playlist(self):
        result = search_playlist("Chill Vibes")
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)
        self.assertIn("Chill Vibes", [playlist['name'] for playlist in result])

if __name__ == '__main__':
    unittest.main()