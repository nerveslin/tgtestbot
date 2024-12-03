import asyncio
import logging

from aiogram import Dispatcher
from aiogram.methods import DeleteWebhook


from handlers import router, bot


async def main():
    await bot(DeleteWebhook(drop_pending_updates=True))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

