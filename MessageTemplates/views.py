from django.shortcuts import render
from .models import MessageTemplates

import logging
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from asgiref.sync import sync_to_async

# Create your views here.
API_TOKEN = '6384385753:AAHv0UeCOMIssdV9ufo9qlaB1gE-ojxJ8K4'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def send_message():
  a = sync_to_async(MessageTemplates).objects.all()
  print('salom')

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)