import os
import logging
import multiprocessing
import asyncio
import time
from telegram import Update
from telegram.ext import (
    filters,
    MessageHandler,
    ApplicationBuilder,
    ContextTypes,
)
from telethon import TelegramClient

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

api_id = "your api id"  # To get your api id and hash visit https://my.telegram.org/apps
api_hash = "your api hash"
phone_number = "your phone number for Telegram"
bot_username = "your Bot username"

client = TelegramClient("session_name", api_id, api_hash)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text=f"Hello {update.message.text}!"
    )


def run_bot(stop_event):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    application = ApplicationBuilder().token(TOKEN).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), hello)
    application.add_handler(echo_handler)

    loop.create_task(stop_bot(application, stop_event))
    application.run_polling()


async def stop_bot(application, stop_event):
    while not stop_event.is_set():
        await asyncio.sleep(2)

    application.stop_running()


async def send_message_to_bot(text: str):
    await client.start(phone=phone_number)
    message = text
    await client.send_message(bot_username, message=message)


def run_client(message: str):
    with client:
        client.loop.run_until_complete(send_message_to_bot(text=message))


def send_message_to_Telegram(message_to_send):
    stop_event = multiprocessing.Event()

    bot_process = multiprocessing.Process(target=run_bot, args=(stop_event,))
    bot_process.start()

    time.sleep(2)

    client_process = multiprocessing.Process(target=run_client, args=(message_to_send,))
    client_process.start()
    client_process.join()

    time.sleep(2)

    stop_event.set()

    bot_process.join()
