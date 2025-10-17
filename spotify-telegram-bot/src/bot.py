from telegram import Update
from telegram.ext import CommandHandler, Context, ContextTypes, ApplicationBuilder #type: ignore
from services.spotify_client import SpotifyClient
from services.telegram_client import TelegramClient
import config
import os

def start(update: Update, context: Context) -> None:
    update.message.reply_text('Welcome to the Spotify Telegram Bot! Use /search to find songs, artists, or playlists.')

def search(update: Update, context: Context) -> None:
    query = ' '.join(context.args or [])
    if not query:
        update.message.reply_text('Please provide a search query.')
        return

    spotify_client = SpotifyClient()
    results = spotify_client.search(query, type_='track,artist,playlist')

    if results:
        response_message = format_search_results(results)
        update.message.reply_text(response_message)
    else:
        update.message.reply_text('No results found.')

def format_search_results(results) -> str:
    response = "Search Results:\n"
    for item in results:
        response += f"{item['type'].capitalize()}: {item['name']} - {item['url']}\n"
    return response

def main() -> None:
    # Resolve token from environment first, then try common names in config.py
    token = os.getenv("TELEGRAM_BOT_TOKEN") or getattr(config, "TELEGRAM_BOT_TOKEN", None) or getattr(config, "TELEGRAM_TOKEN", None)
    if not token:
        raise RuntimeError("Telegram bot token not configured; set TELEGRAM_BOT_TOKEN env var or add TELEGRAM_BOT_TOKEN to config.py")
    
    # Use ApplicationBuilder (python-telegram-bot v20+)
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("search", search))

    app.run_polling()

if __name__ == '__main__':
    main()