import asyncio
import telegram
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def main():
    bot = telegram.Bot(TOKEN)
    async with bot:
        updates = await bot.get_updates()
        update = updates[0]
        chat_id = update.message.from_user.id
        await bot.send_message(text="Hi John123!", chat_id=chat_id)


if __name__ == "__main__":
    asyncio.run(main())
