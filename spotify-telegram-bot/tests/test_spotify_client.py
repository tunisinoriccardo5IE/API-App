import unittest
from src.services.spotify_client import SpotifyClient

class TestSpotifyClient(unittest.TestCase):

    def setUp(self):
        self.client = SpotifyClient()

    def test_authentication(self):
        self.assertTrue(self.client.authenticate(), "Authentication should succeed")

    def test_search_song(self):
        result = self.client.search("Imagine", type="track")
        self.assertIsInstance(result, list, "Search should return a list")
        self.assertGreater(len(result), 0, "Search result should not be empty")

    def test_search_artist(self):
        result = self.client.search("The Beatles", type="artist")
        self.assertIsInstance(result, list, "Search should return a list")
        self.assertGreater(len(result), 0, "Search result should not be empty")

    def test_search_playlist(self):
        result = self.client.search("Chill Vibes", type="playlist")
        self.assertIsInstance(result, list, "Search should return a list")
        self.assertGreater(len(result), 0, "Search result should not be empty")

if __name__ == '__main__':
    unittest.main()