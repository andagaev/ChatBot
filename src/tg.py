import asyncio
import logging
import os

import telethon

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
tg_username = os.environ["TG_USERNAME"]
bot_token = os.environ["TOKEN"]

client = None


def init_client():
    global client
    if client is None:
        client = telethon.TelegramClient("session_name", api_id, api_hash)


async def send_message_to_bot(text: str):
    init_client()
    await client.start(bot_token=bot_token)
    await client.send_message(tg_username, message=text)


async def run_client(message: str):
    init_client()
    async with client:
        await send_message_to_bot(text=message)


def send_message_to_Telegram(message_to_send):
    asyncio.run(run_client(message=message_to_send))
