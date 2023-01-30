from aiogram import Dispatcher
from aiogram.types import Message

from bot import main
from bot.keyboards.reply import menu_kb


async def bot_start(msg: Message):
    # if username close then use his first name
    name = msg.from_user.username if msg.from_user.username != "None" else msg.from_user.first_name
    
    main.database.create_user(int(msg.from_user.id), name)
    
    await msg.answer_photo(photo=open("files_for_admin\\photo_for_start.png", "rb"),
                           caption=f'<em>Hello</em>, <b>{name}</b>!\n'
                                   f'Select a menu of interest',
                           reply_markup=menu_kb,
                           parse_mode="HTML")
        

def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])