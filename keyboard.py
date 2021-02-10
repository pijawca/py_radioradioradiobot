# -*- coding: utf-8 -*-
#twitter.com/pijawca
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


home_btn = KeyboardButton('Домой')
userRadio_btn = 'Пользовательское Радио'
maximum_btn = KeyboardButton('Радио Maximum') # Радио Maximum
energy_btn = KeyboardButton('Радио Energy') # Радио Energy
auto_btn = KeyboardButton('Радио Авторадио') # Радио Авторадио
comedy_btn = KeyboardButton('Comedy Radio') # Comedy Radio
marusya_btn = KeyboardButton('Маруся FM') # Маруся FM
markup = ReplyKeyboardMarkup(resize_keyboard=False).row(maximum_btn, energy_btn, comedy_btn).row(marusya_btn).row(userRadio_btn)


user_zoloto_shansona = 'Золото Шансона'
userMarkup = ReplyKeyboardMarkup(resize_keyboard=True).row(user_zoloto_shansona, home_btn)
