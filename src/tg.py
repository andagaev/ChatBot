import logging
import os

import requests

from src.db import database as db

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

bot_token = os.environ["TG_TOKEN"]


def send_message_to_Telegram(message_to_send: str):
    users = db.get_tg_users()

    for user in users:
        res = requests.post(
            url=f"https://api.telegram.org/bot{bot_token}/sendMessage",
            json={
                "chat_id": int(user.id),
                "text": message_to_send,
            },
        )
        if res.status_code != 200:
            logger.error(f"Failed to send message to {user.username}")
        else:
            logger.info(f"Message sent to {user.username}")
