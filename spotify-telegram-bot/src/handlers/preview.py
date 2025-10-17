from services.spotify_client import SpotifyClient
from services.telegram_client import TelegramClient

def preview_track(track_id):
    spotify_client = SpotifyClient()
    track_info = spotify_client.get_track(track_id)
    
    if track_info:
        preview_url = track_info['preview_url']
        track_name = track_info['name']
        artist_name = ', '.join(artist['name'] for artist in track_info['artists'])
        
        return f"Preview of '{track_name}' by {artist_name}: {preview_url}"
    else:
        return "Track not found."

def handle_preview_request(update, context):
    track_id = context.args[0] if context.args else None
    
    if track_id:
        preview_message = preview_track(track_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=preview_message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please provide a track ID.")