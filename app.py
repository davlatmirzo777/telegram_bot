from aiogram.types import Message
from config import dp
from aiogram import executor
import wikipedia


@dp.message_handler()
async def wiki(msg: Message):
    print(msg.chat.id)
    try:
        response = wikipedia.summary(msg.text)
        await msg.answer(response)
    except:
        await msg.answer("bu mavzuga oid maqola topilmadi!!!")


if __name__ == '__main__':
    executor.start_polling(dp)