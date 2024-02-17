
from ...models import TaskMessages
import telebot

bot = telebot.TeleBot("6384385753:AAHv0UeCOMIssdV9ufo9qlaB1gE-ojxJ8K4", parse_mode=None)

def task():
  messages = TaskMessages.objects.all()
  # Bu yerda chat_id = user_id ga teng
  bot.send_message(chat_id=5884447415, text='salom')
  for i in messages:
    print(i.template)