class TelegramClient:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}/"

    def send_message(self, chat_id, text):
        url = f"{self.base_url}sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, json=payload)
        return response.json()

    def handle_updates(self, update):
        # Logic to handle incoming updates from Telegram
        pass

    def get_updates(self):
        url = f"{self.base_url}getUpdates"
        response = requests.get(url)
        return response.json()