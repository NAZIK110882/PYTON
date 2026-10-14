from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
import database
import weather_api

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    welcome_text = (
        "Привіт! Я твій бот-помічник.\n\n"
        "Доступні команди:\n"
        "/weather <місто> - дізнатися погоду\n"
        "/addnote <текст> - додати нотатку\n"
        "/notes - переглянути мої нотатки\n"
        "/help - допомога"
    )
    await message.answer(welcome_text)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Я можу зберігати твої нотатки та показувати погоду.\nВикористовуй меню команд для навігації.")

@router.message(Command("weather"))
async def cmd_weather(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer("Будь ласка, вкажи місто. Формат: /weather Київ")
        return
    
    city = parts[1]
    weather_info = await weather_api.get_weather(city)
    await message.answer(weather_info)

@router.message(Command("addnote"))
async def cmd_addnote(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer("Текст нотатки порожній. Формат: /addnote Купити молоко")
        return
    
    note_text = parts[1]
    await database.add_note(message.from_user.id, note_text)
    await message.answer("Нотатку успішно збережено!")

@router.message(Command("notes"))
async def cmd_notes(message: Message):
    notes = await database.get_notes(message.from_user.id)
    if not notes:
        await message.answer("У тебе поки немає збережених нотаток.")
        return

    for note_id, text in notes:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="❌ Видалити", callback_data=f"del_{note_id}")]
        ])
        await message.answer(f"📌 {text}", reply_markup=keyboard)

@router.callback_query(F.data.startswith("del_"))
async def process_delete_note(callback: CallbackQuery):
    note_id = int(callback.data.split("_")[1])
    await database.delete_note(note_id, callback.from_user.id)
    await callback.message.edit_text("Нотатку видалено 🗑️")
    await callback.answer()

@router.message()
async def process_unknown(message: Message):
    await message.answer("Я не розумію цієї команди. Використовуй /help для списку доступних дій.")