import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import emoji
import webbrowser
import asyncio
import os
load_dotenv()
TOKEN = os.getenv('TOKEN')
router = Router()


@router.message(Command("start"))
async def command_start_handler(message:Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@router.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=emoji.emojize('🎲'))

@router.message(F.text)
async def handle_text(message: types.Message):
    reply = f"You sent text and i got it, {message.text}"
    await message.answer(reply)
    await message.reply(reply)

@router.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
