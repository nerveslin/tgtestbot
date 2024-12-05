import asyncio
import redis
from celery import Celery
from celery.schedules import crontab
from config import TELEGRAM_WORKER_ID

app_celery = Celery('tasks', broker='redis://127.0.0.1:6379/0', include=['tasks'])
r = redis.Redis(host="127.0.0.1", port=6379)


@app_celery.task(name='tasks.send_scheduled_message')
async def create_celery_task_send_message(text: str) -> None:
    asyncio.run(send_scheduled_task(text))


async def send_scheduled_task(text: str) -> None:
    from handlers import bot
    message = text
    await bot.send_message(chat_id=TELEGRAM_WORKER_ID, text=message)


beat_schedule = {
    'send_message_every_monday_morning': {
        'task': 'tasks.send_scheduled_message',
        'schedule': crontab(hour='9', minute='30', day_of_week='1'),
        'args': TELEGRAM_WORKER_ID,
    },
}
