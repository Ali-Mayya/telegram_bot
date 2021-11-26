from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor
from aiogram.dispatcher.storage import BaseStorage
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram.contrib.fsm_storage.redis import RedisStorage2

# storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='my_fsm_key')

storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)


TOKEN="2100679408:AAHTdh7sJFK3m1uu9TtPVMqQlNWn2q3WfDE"
# os.getenv('TOKEN'))
bot=Bot(token=TOKEN)
dp=Dispatcher(bot,storage=storage)
