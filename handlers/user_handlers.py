from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_EN


# Initializing the module level router 
router = Router()


# This handler will work on command /start 
@router.message(CommandStart())
async def process_start_command(message: Message) -> Message:
    await message.answer(text=LEXICON_EN['/start']) 
    

# This handler will work on command /help 
@router.message(Command(commands=['help']))
async def process_help_command(message: Message) -> Message:
    await message.answer(text=LEXICON_EN['/help'])