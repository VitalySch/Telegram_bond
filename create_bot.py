from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
TOKEN = "5661972652:AAEhY9IvbhJHgaQGiFekgPeJ8dpPCReQtns"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
