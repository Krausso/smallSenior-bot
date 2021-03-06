from typing import NoReturn

from aiogram.types import Message

from app.functions.stats import count_members
from app.config import dp


@dp.message_handler(commands=['stats'], state="*")
async def stats(message: Message) -> NoReturn:
    await message.answer(await count_members())
