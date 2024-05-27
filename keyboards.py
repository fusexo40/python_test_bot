from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


main_kb = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
               [KeyboardButton(text="Мои пари"),
                KeyboardButton(text="Создать пари")]
        ]
    )


create_kb = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=[
               [InlineKeyboardButton(text="Главное меню", callback_data="main")]
        ]
    )