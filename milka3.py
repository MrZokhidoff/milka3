import logging
import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes
from aiogram.types.message import ContentType

TOKEN = '5263204102:AAGbhwcrjSfFIH1kEeGOL8fcmjnzqxEIhdE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id,"Вас приветствует бот\n\nВыберите раздел\n\n📦 Товары и цены\nЖми 👉 /products\n- - - - - - - - - - - - - - - -\n🌆 Выбрать район\nЖми 👉 /locations\n- - - - - - - - - - - - - - - -\n💰 Мой последний заказ\nЖми 👉 /last_order", )

@dp.message_handler(commands='menu')
async def start(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id,"Вас приветствует бот\n\nВыберите раздел\n\n📦 Товары и цены\nЖми 👉 /products\n- - - - - - - - - - - - - - - -\n🌆 Выбрать район\nЖми 👉 /locations\n- - - - - - - - - - - - - - - -\n💰 Мой последний заказ\nЖми 👉 /last_order", )


@dp.message_handler(commands='products')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Выберите товар \n\n📦 SK VIP WHITE KRYSTALL (0.5 г)\n2500 руб 👉 /product_77\n- - - - - - - - - - - - - - - -\n📦 SK VIP WHITE KRYSTALL (0.3 г) \n1800 руб 👉 /product_78\n- - - - - - - - - - - - - - - -\n📦 МЕФ МЯУ (0.5 г)\n2500 руб 👉 /product_87 \n\n➖➖➖➖➖➖➖➖➖➖➖ \nⓂ️ Вернуться в меню \nЖми 👉 /menu", )

@dp.message_handler(commands='product_77')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Вы заказываете \nSK VIP WHITE KRYSTALL, 0.5 г за 2500 руб \nУточните район:\n\n🚩 Наманган\nДалее 👉 /order_10_77\n- - - - - - - - - - - - - - - -\n🚩 Андижан\nДалее 👉 /order_3_17\n🚩 Ташкент\nДалее 👉 /order_5_97\n- - - - - - - - - - - - - - - -\n🚩 Самарканд\nДалее 👉 /order_3_79\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='product_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Вы заказываете \nSK VIP WHITE KRYSTALL, 0.3 г за 1800 руб \nУточните район:\n\n🚩 Наманган\nДалее 👉 /order_11_87\n- - - - - - - - - - - - - - - -\n🚩 Андижан\nДалее 👉 /order_1_87\n🚩 Ташкент\nДалее 👉 /order_13_67\n- - - - - - - - - - - - - - - -\n🚩 Самарканд\nДалее 👉 /order_11_37\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='product_87')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Вы заказываете \n📦 МЕФ МЯУ (0.5 г) 2500 руб   \nУточните район:\n\n🚩 Наманган\nДалее 👉 /order_11_87\n- - - - - - - - - - - - - - - -\n🚩 Андижан\nДалее 👉 /order_1_87\n🚩 Ташкент\nДалее 👉 /order_13_67\n- - - - - - - - - - - - - - - -\n🚩 Самарканд\nДалее 👉 /order_11_37\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_11_87')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_17_77')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_17_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_17_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")


@dp.message_handler(commands='order_1_87')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_13_67')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_11_37')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_10_77')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_3_17')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_5_97')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_11_87')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_3_79')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='order_3_17')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ Выберите способ оплаты:   \n\n💰 Оплата с баланса 👉 /order35_17_78\n\n💰 Bitcoin (BTC) 👉 /order22_17_78\n\n💰 Оплата картой банка 👉 /order43_17_78\n\n💰 Litecoin (LTC) 👉 /order24_17_78\n\n💰 Ethereum (ETH) 👉 /order25_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='locations')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Выберите район:\n\n🚩 Наманган\nЖми 👉 /location_10\n- - - - - - - - - - - - - - - -\n🚩 Андижан\nЖми 👉 /location_18\n- - - - - - - - - - - - - - - -\n🚩 Ташкент\nЖми 👉 /location_20\n- - - - - - - - - - - - - - - -\n🚩 Самарканд\nЖми 👉 /location_22\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='location_10')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Наманган\nУточните район:\n\n🏘 По городу\nЖми 👉 /location_17\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='location_18')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Андижан\nУточните район:\n\n🏘 По городу\nЖми 👉 /location_27\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='location_20')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Ташкент\nУточните район:\n\n🏘 По городу\nЖми 👉 /location_11\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='location_22')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Самарканд\nУточните район:\n\n🏘 По городу\nЖми 👉 /location_19\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='location_17')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Выберите товар\nв районе По городу\n\n📦 SK VIP WHITE KRYSTALL (0.5 г)\n2500 руб\nЗаказать 👉 /order_17_77\n- - - - - - - - - - - - - - - -\n📦 SK VIP WHITE KRYSTALL (0.3 г)\n1700 руб\nЗаказать 👉 /order_17_78\n- - - - - - - - - - - - - - - -\n📦 МЕФ МЯУ (0.5 г)\n2700 руб\nЗаказать 👉 /order_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

@dp.message_handler(commands='location_27')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Выберите товар\nв районе По городу\n\n📦 SK VIP WHITE KRYSTALL (0.5 г)\n2500 руб\nЗаказать 👉 /order_17_77\n- - - - - - - - - - - - - - - -\n📦 SK VIP WHITE KRYSTALL (0.3 г)\n1700 руб\nЗаказать 👉 /order_17_78\n- - - - - - - - - - - - - - - -\n📦 МЕФ МЯУ (0.5 г)\n2700 руб\nЗаказать 👉 /order_17_78\n\n➖➖➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")

# @dp.message_handler(commands='order35_17_78')
# async def products(message: types.Message):
#     if message.chat.type == 'private':
#         await bot.send_message(message.from_user.id, "Приносим извинения за неудобства, в данный момент проблема с платежной системой, оплатить можно из программы Oson"+"приложение Oson\n\nhttps://oson.uz/")

@dp.message_handler(commands='order22_17_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Приносим извинения за неудобства, в настоящее время возникла проблема с платежной системой, теперь вы можете оплатить нашей картой \t\tVisa."+"\nнаша карта для оплаты:\n4890494773248745")

@dp.message_handler(commands='order35_17_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Приносим извинения за неудобства, в настоящее время возникла проблема с платежной системой, теперь вы можете оплатить нашей картой \t\tVisa."+"\nнаша карта для оплаты:\n4890494773248745")

@dp.message_handler(commands='order43_17_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Приносим извинения за неудобства, в настоящее время возникла проблема с платежной системой, теперь вы можете оплатить нашей картой \t\tVisa."+"\nнаша карта для оплаты:\n4890494773248745")

@dp.message_handler(commands='order25_17_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Приносим извинения за неудобства, в настоящее время возникла проблема с платежной системой, теперь вы можете оплатить нашей картой \t\tVisa."+"\nнаша карта для оплаты:\n4890494773248745")

@dp.message_handler(commands='order24_17_78')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "Приносим извинения за неудобства, в настоящее время возникла проблема с платежной системой, теперь вы можете оплатить нашей картой \t\tVisa."+"\nнаша карта для оплаты:\n4890494773248745")

@dp.message_handler(commands='last_order')
async def products(message: types.Message):
    if message.chat.type == 'private':
        await bot.send_message(message.from_user.id, "❗️ К сожалению,\nу нас нет информации о Вашем последнем заказе.\n\nПожалуйста, сначала заплатите\n4890494773248745\n\n➖➖➖➖➖➖➖➖➖\nⓂ️ Вернуться в меню\nЖми 👉 /menu")





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
