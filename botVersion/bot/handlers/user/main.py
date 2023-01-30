from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text


async def go_to_menu(msg: types.Message | types.CallbackQuery, state: FSMContext):
    await state.finish()
    
    # check on type message
    if type(msg) == types.CallbackQuery:
        msg = msg.message
    await msg.answer(msg.text)


def register_user_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(go_to_menu, text=["go_to_menu", "cancel_trade"], state="*")
    dp.register_message_handler(go_to_menu, Text(equals="Главное меню"), state="*")