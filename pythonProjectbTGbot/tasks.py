import asyncio
from celeryq import app_celery
from handlers import bot


async def send_notification_message(text: str, chat_id: str) -> None:
    message = text
    await bot.send_message(chat_id=chat_id, text=message)


@app_celery.task(name='tasks.add')
def create_celery_task_send_message(text: str, chat_id: str) -> None:
    asyncio.run(send_notification_message(text, chat_id))

