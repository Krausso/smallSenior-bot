from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choose_screen_color_kb():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Червоний", callback_data="red"),
        InlineKeyboardButton(text="Зелений", callback_data="green"),

        InlineKeyboardButton(text="Синій", callback_data="blue"),
        InlineKeyboardButton(text="Жовтий", callback_data="yellow"),

        InlineKeyboardButton(text="Темний", callback_data="dark")
    )
    return keyboard


def create_post_kb(url=None):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="🔥 0", callback_data="like"),
        InlineKeyboardButton(text="👎 0", callback_data="dlike")
    )
    if url:
        keyboard.add(
            InlineKeyboardButton(text="Посмотреть", url=url)
        )
    return keyboard
