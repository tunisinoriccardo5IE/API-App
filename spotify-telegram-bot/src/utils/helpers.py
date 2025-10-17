def format_message(title, url, description):
    return f"*{title}*\n{description}\n[Listen here]({url})"

def handle_error(error_message):
    return f"An error occurred: {error_message}"

def extract_track_info(track_data):
    return {
        "title": track_data.get("name"),
        "artist": ", ".join(artist["name"] for artist in track_data.get("artists", [])),
        "url": track_data.get("external_urls", {}).get("spotify"),
        "preview_url": track_data.get("preview_url"),
    }