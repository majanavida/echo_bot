from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_EN

# Initializing the module level router 
router = Router()


# This handler will work on any messages, except /start and /help 
@router.message
async def send_echo(message: Message) -> Message:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer(LEXICON_EN['TypeError'])