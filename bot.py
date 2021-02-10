# -*- coding: utf-8 -*-
# -*- twitter.com/pijawca -*-
from aiogram import executor, Dispatcher
from misc import dp
import handlers


async def shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_shutdown=shutdown)
