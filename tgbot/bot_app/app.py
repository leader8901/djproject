import telebot
from telebot.storage import StateMemoryStorage

from djproject import settings

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(settings.TOKEN, state_storage=state_storage)