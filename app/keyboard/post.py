from typing import Optional

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def choose_screen_color_kb():
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text='ервоний', callback_data='red'),
        InlineKeyboardButton(text='Зелений', callback_data='green'),

        InlineKeyboardButton(text='Синій', callback_data='blue'),
        InlineKeyboardButton(text='Жовтий', callback_data='yellow'),

        InlineKeyboardButton(text='Темний', callback_data='dark')
    )
    return keyboard


def create_post_kb(like_text: Optional[str] = None,
                   dislike_text: Optional[str] = None):
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
    if like_text:
        keyboard.add(
            InlineKeyboardButton(text=like_text, callback_data='likes'),
            InlineKeyboardButton(text=dislike_text, callback_data='dislikes')
        )
        return keyboard
    keyboard.add(
        InlineKeyboardButton(text='🔥 0', callback_data='likes'),
        InlineKeyboardButton(text='👎 0', callback_data='dislikes')
    )
    return keyboard
