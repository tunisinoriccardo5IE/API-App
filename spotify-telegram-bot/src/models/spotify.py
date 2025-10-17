class Track:
    def __init__(self, id, name, artists, album, preview_url):
        self.id = id
        self.name = name
        self.artists = artists
        self.album = album
        self.preview_url = preview_url

class Artist:
    def __init__(self, id, name, genres):
        self.id = id
        self.name = name
        self.genres = genres

class Playlist:
    def __init__(self, id, name, description, tracks):
        self.id = id
        self.name = name
        self.description = description
        self.tracks = tracks

class SpotifyResponse:
    def __init__(self, tracks=None, artists=None, playlists=None):
        self.tracks = tracks if tracks else []
        self.artists = artists if artists else []
        self.playlists = playlists if playlists else []