# -*- coding: utf-8 -*-
# -*- twitter.com/pijawca -*-
import keyboard as kb
from aiogram import types
from bot import dp
from aiogram.dispatcher.filters import Text


@dp.message_handler(Text(equals=['/start']))
async def start_command(message: types.Message):
    await message.answer(f'Привет *{message.from_user.full_name}*, я бот с потоковыми вещаниями радио.\n\n'
                         f'Теперь чтобы слушать свои любимые радиостанции не нужно искать в поисковике.\n\n'
                         f'Достаточно выбрать радиостанцию из списка и получить ссылку на прямой эфир!\n\n'
                         f'🐍 Coder: @pijawca\n🎫 Github: @pijawca\n🐦 Twitter: @pijawca',
                         parse_mode=types.ParseMode.MARKDOWN, reply_markup=kb.markup)

@dp.message_handler(Text(equals=['Домой']))
async def start_command(message: types.Message):
    await message.answer('Возвращаюсь.', reply_markup=kb.markup)

class userRadio:
    @dp.message_handler(Text(equals=['Пользовательское Радио']))
    async def usersRadio(message: types.Message):
        await message.answer(f'Здесь вы можете слушать пользователькие потоки!',
                             parse_mode=types.ParseMode.MARKDOWN, reply_markup=kb.userMarkup)

    @dp.message_handler(Text(equals=['Золото Шансона']))
    async def zolotoShansona(message: types.Message):
        await message.answer('*Золото Шансона*\n'
                             '[Слушать сейчас](https://pub0202.101.ru:8443/stream/personal/aacp/64/589426)',
                             parse_mode=types.ParseMode.MARKDOWN)

class Radio:
    @dp.message_handler(Text(equals=['Радио Maximum']))
    async def radioMaximum(message: types.Message):
        await message.answer('*Радио Maximum*\n'
                             '[Слушать сейчас](https://maximum.hostingradio.ru/maximum96.aacp)',
                             parse_mode=types.ParseMode.MARKDOWN)

    @dp.message_handler(Text(equals=['Радио Energy']))
    async def radioEnergy(message: types.Message):
        await message.answer('*Радио Energy*\n'
                             '[Слушать сейчас](https://pub0301.101.ru:8443/stream/air/mp3/256/99)',
                             parse_mode=types.ParseMode.MARKDOWN)

    @dp.message_handler(Text(equals=['Радио Авторадио']))
    async def autoRadio(message: types.Message):
        await message.answer('*Радио Авторадио*\n'
                             '[Слушать сейчас](https://pub0201.101.ru:8000/stream/air/aac/64/100)',
                             parse_mode=types.ParseMode.MARKDOWN)

    @dp.message_handler(Text(equals=['Comedy Radio']))
    async def comedyRadio(message: types.Message):
        await message.answer('*Comedy Radio*\n'
                             '[Слушать сейчас](https://pub0302.101.ru:8443/stream/air/aac/64/202)',
                             parse_mode=types.ParseMode.MARKDOWN)

    @dp.message_handler(Text(equals=['Маруся FM']))
    async def r_maximum(message: types.Message):
        await message.answer('*Маруся FM*\n'
                             '[Слушать сейчас](https://pub0302.101.ru:8443/stream/pull/aac/64/301)',
                             parse_mode=types.ParseMode.MARKDOWN)

    # @dp.message_handler(Text(equals=['Comedy Radio']))
    # async def r_maximum(message: types.Message):
    #     await message.answer('*Comedy Radio*\n'
    #                          '[Слушать сейчас](https://pub0302.101.ru:8443/stream/air/aac/64/202)',
    #                          parse_mode=types.ParseMode.MARKDOWN)
    #
    # @dp.message_handler(Text(equals=['Comedy Radio']))
    # async def r_maximum(message: types.Message):
    #     await message.answer('*Comedy Radio*\n'
    #                          '[Слушать сейчас](https://pub0302.101.ru:8443/stream/air/aac/64/202)',
    #                          parse_mode=types.ParseMode.MARKDOWN)
    #
    # @dp.message_handler(Text(equals=['Comedy Radio']))
    # async def r_maximum(message: types.Message):
    #     await message.answer('*Comedy Radio*\n'
    #                          '[Слушать сейчас](https://pub0302.101.ru:8443/stream/air/aac/64/202)',
    #                          parse_mode=types.ParseMode.MARKDOWN)
