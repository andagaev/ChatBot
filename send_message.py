import asyncio
import logging
import os

import telethon

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

api_id = "your api id"  # To get your api id and hash visit https://my.telegram.org/apps
api_hash = "your api hash"
username = "user's username"


client = None


def init_client():
    global client
    if client is None:
        client = telethon.TelegramClient("session_name", api_id, api_hash)


async def send_message_to_bot(text: str):
    init_client()
    await client.start(bot_token=TOKEN)
    await client.send_message(username, message=text)


async def run_client(message: str):
    init_client()
    async with client:
        await send_message_to_bot(text=message)


def send_message_to_Telegram(message_to_send):
    asyncio.run(run_client(message=message_to_send))
