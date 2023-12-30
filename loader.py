
from aiogram import Bot, Dispatcher
from config import Config, load_config
from models.sqlite import Database

config: Config = load_config()


bot: Bot = Bot(token="6857404775:AAFK1T0zSwqI6rmcqj30j1o3cP--cz-QjtE", parse_mode="HTML")
db = Database(path_to_db="main.db")