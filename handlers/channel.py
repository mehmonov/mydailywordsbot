from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from loader import bot, db

import re
channel : Router=Router()

@channel.channel_post()
async def handle_message(message: Message):
    text = message.text
    lines = text.split('\n')
    dictionary = {}
    medium_links = []
    for line in lines:
        if ' - ' in line:
            eng, uzb = line.split(' - ')
            dictionary[eng.strip()] = uzb.strip()
        elif re.match(r'https?://medium.com/.*', line):
            medium_links.append(line.strip())
    print(dictionary)
    print(medium_links)
    for en, uz in dictionary.items():
        medium = medium_links[0] if medium_links else None
        db.add_words(en=en, uz=uz, medium=medium)
    words = db.select_all_words()
    await message.answer(str(words))
   