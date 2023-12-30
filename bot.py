import asyncio
import logging

from aiogram import Dispatcher

from handlers.echo import router
from handlers.start_handler import start_router
from handlers.channel import channel
from handlers.search_words import search_words
from handlers.random_words import random_words
from loader import bot, db
logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
       
    )

    logger.info("Starting bot")
    try:
        db.create_table_users()
    except Exception as err:
        print(err)

    dp: Dispatcher = Dispatcher()

    dp.include_routers(
        random_words,
        search_words,
        channel,
        start_router,
        
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
