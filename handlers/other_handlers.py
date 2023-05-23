from aiogram import Router
from aiogram.types import Message

router: Router = Router()

# Хэндлер для любых сообщений вне логики бота
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Я не знаю такой комманды {message.text}')