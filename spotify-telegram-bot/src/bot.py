from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from services.spotify_client import SpotifyClient
from services.telegram_client import TelegramClient
import config

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Spotify Telegram Bot! Use /search to find songs, artists, or playlists.')

def search(update: Update, context: CallbackContext) -> None:
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text('Please provide a search query.')
        return

    spotify_client = SpotifyClient()
    results = spotify_client.search(query)

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
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("search", search))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()