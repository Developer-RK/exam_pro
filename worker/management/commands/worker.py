import time
from typing import Any
from aiogram import executor

from .send_message import task

from django.core.management.base import BaseCommand

from apscheduler.schedulers.asyncio import AsyncIOScheduler

class Command(BaseCommand):
    help = "Botni ishga tushirish"
    def handle(self, *args: Any, **options: Any):
      while True:
        time.sleep(1.5)
        task()