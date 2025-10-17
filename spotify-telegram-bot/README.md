# Spotify Telegram Bot

This project is a Telegram bot that allows users to search for songs, artists, and playlists on Spotify, and share or preview them directly in chat.

## Features

- Search for songs, artists, and playlists using commands.
- Preview tracks directly in Telegram.
- Share links to Spotify tracks, artists, and playlists.

## Project Structure

```
spotify-telegram-bot
├── src
│   ├── bot.py                # Main entry point for the Telegram bot
│   ├── config.py             # Configuration settings (API keys, tokens)
│   ├── __init__.py           # Package initialization
│   ├── handlers               # Command handlers for the bot
│   │   ├── search.py          # Handles search commands
│   │   ├── preview.py         # Handles preview requests
│   │   └── share.py           # Handles sharing requests
│   ├── services               # Services for interacting with APIs
│   │   ├── spotify_client.py   # Spotify API client
│   │   └── telegram_client.py   # Telegram API client
│   ├── models                 # Data models for Spotify entities
│   │   └── spotify.py         # Defines models for tracks, artists, playlists
│   └── utils                  # Utility functions
│       └── helpers.py         # Helper functions for various tasks
├── tests                      # Unit tests for the bot
│   ├── test_search.py         # Tests for search functionality
│   └── test_spotify_client.py  # Tests for SpotifyClient class
├── requirements.txt           # Project dependencies
├── pyproject.toml             # Project configuration
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore file
├── Dockerfile                 # Docker image instructions
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd spotify-telegram-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables by copying `.env.example` to `.env` and filling in the required values.

## Usage

1. Run the bot:
   ```
   python src/bot.py
   ```

2. Interact with the bot on Telegram using the available commands:
   - `/song <song_name>`: Search for a song.
   - `/artist <artist_name>`: Search for an artist.
   - `/playlist <playlist_name>`: Search for a playlist.
   - `/preview <track_id>`: Get a preview of a track.
   - `/share <track_id>`: Share a link to a track.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.