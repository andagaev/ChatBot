import logging
import os

import requests

from src.db import database as db

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

bot_token = os.environ["DISCORD_TOKEN"]


def send_message_to_Discord(message_to_send: str):
    users = db.get_discord_users()
    channels = db.get_discord_channels()

    headers = {"Authorization": f"Bot {bot_token}"}

    for user in users:
        print(user.id)
        res = requests.post(
            url=f"https://discord.com/api/channels/{user.id}/messages",
            headers=headers,
            json={"content": message_to_send, "tts": False},
        )
        if res.status_code != 200:
            logger.error(f"Failed to send message to {user.username}")
        else:
            logger.info(f"Message sent to {user.username}")

    for channel in channels:
        print(channel.id)
        res = requests.post(
            url=f"https://discord.com/api/channels/{channel.id}/messages",
            headers=headers,
            json={"content": message_to_send, "tts": False},
        )
        if res.status_code != 200:
            logger.error(f"Failed to send message to {channel.name}")
        else:
            logger.info(f"Message sent to {channel.name}")
