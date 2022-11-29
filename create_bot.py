from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()
my_secret = os.environ['TOKEN']
bot = Bot(token=my_secret)
dp = Dispatcher(bot, storage=storage)
