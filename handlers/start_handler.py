from aiogram import Router, F
from loader import db
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
start_router: Router= Router()

@start_router.message(Command("start"))
async def  start_handler(message: Message):
    
    try:
        db.add_users(
            name=message.from_user.full_name,
            telegram_id=message.from_user.id
        )
    except Exception as err:
        print(err)

    keyboar = ReplyKeyboardMarkup(
           keyboard=[
               [
                   KeyboardButton(text="So'z qidirish")
               ],
            #    [
            #        KeyboardButton(text="So'z qo'shish")
            #    ],
               [
                   KeyboardButton(text="Test")
               ]
           ],
           resize_keyboard=True
         )
    await message.answer(f"Salom {message.from_user.full_name}. Nima qilamiz?    ", reply_markup=keyboar)
    await message.answer("Aytgancha, bu kanalga a'zo bo'lib oling. O'zimiz uchun aytmayapmiz. Bot bir butunni faqat yarmi. Yarmi esa kanaldir) \n\n   https://t.me/mywordsdaily")
     
    if message.from_user.id == 6329800356:
        users = db.count_users()[0]
        words = db.count_words()[0]
        await message.answer(f"Sizga alohida salom :)  \n\n  Botdagi jami userlar soni {users}. So'zlar soni esa {words}")
        