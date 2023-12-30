from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, PollAnswer
from googletrans import Translator
from states.random_words import random_s
from  aiogram.fsm.context import FSMContext
from loader import db, bot
import random
from aiogram.handlers import PollHandler

random_words: Router= Router()


@random_words.message(F.text == "Test")
async def random_w(message: Message, state: FSMContext):
    await state.set_state(random_s.random)
    words = db.select_random_word()
    global correct_option_id
    options = [word[0] for word in words]
    
    true_word = random.choice(words)
    correct_option_id = options.index(true_word[0])

    await message.answer_poll(
        question=f" \"{true_word[1]}\" ushbu so'zni tarjimasini toping",
        options=options,
        type="quiz",
        correct_option_id=correct_option_id,
        open_period=10,
        )    
    
