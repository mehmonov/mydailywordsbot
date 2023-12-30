from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from googletrans import Translator
from states.searchWordStates import search_s
from  aiogram.fsm.context import FSMContext
from loader import db

search_words: Router= Router()

@search_words.message(F.text == "So'z qidirish")
async def search_word(message: Message, state: FSMContext):
    await state.set_state(search_s.search)
    await message.answer("So'zni kiriting: ")
    
    
    
@search_words.message(search_s.search)
async def result_word(message: Message, state: FSMContext):
    input = message.text
    translator = Translator()
    language = translator.detect(input)

    if language.lang == 'en':
        word = db.select_words(en=input)
        
        if word:
            en = word[1]   
            uz = word[2]
            m = word[3] 
            d = word[4]
            await message.reply(
                text=f" *{uz}* -----  *{en}*,  \n\n Medium {m}\n\n Vaqti {d} " , parse_mode='Markdown'
            )
        else:
            t = translator.translate(text=input, dest='uz')

            await message.reply(f"Bu so'z bizda yo'q shekilli. Unutmang, biz faqatgina ushbu kanaldan so'zlarni qidiramiz. \n\n\n Google translate bilan tarjimasi \n\n\n {t.text}")
    else:
        word = db.select_words(uz=input)
        
        if word:
            en = word[1]   
            uz = word[2]
            m = word[3] 
            d = word[4]
            await message.reply(
                text=f"  *{en}* ----- *{uz}*,  \n\n medium {m}\n\n vaqti {d} " , parse_mode='Markdown'
            )
        else:
            t = translator.translate(text=input, dest='en')
            
            await message.reply(f"Bu so'z bizda yo'q shekilli. Unutmang, biz faqatgina ushbu kanaldan so'zlarni qidiramiz. \n\n\n Google translate bilan tarjimasi: \n\n\n {t.text}")
