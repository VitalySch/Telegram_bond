from aiogram.utils import executor
from create_bot import dp
from handlers import client

client.register_handler_client(dp)


executor.start_polling(dp, skip_updates=False)