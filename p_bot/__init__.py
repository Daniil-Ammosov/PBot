import datetime as dt

from aiogram import Bot, Dispatcher, types

from .database import Database
from .logger import get_logger
from .payments import LICENSE, HELPING, OPTION

__author__ = "Daniil Ammosov"

API_TOKEN = "1586731792:AAFVL6HyRoldBP0uACqCy9gox7gbb2f8qK0"                        # TODO add bot token
PAYMENTS_PROVIDER_TOKEN = '401643678:TEST:bf25ad88-76f7-4b79-93e8-82b7da147cf3'  # TODO add bot token
LUNTIC_URL = "https://d.newsweek.com/en/full/520858/supermoon-moon-smartphone-photo-picture.jpg"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database(login="root", password="root", database="telegram_bot", host="localhost")

bot.logger = get_logger()


# =====================================================================================
@dp.message_handler(commands=["start"])
async def welcome_message(message: types.Message):
    bot.logger.info(f"New message from {message.from_user.full_name} ID: {message.from_user.id} ChatID: {message.chat.id}")
    return await message.answer("Привет, я умею то-сё, пятое-десятое")


@dp.message_handler(commands=["buy"])
async def processing_payment(message: types.Message):
    await bot.send_invoice(message.chat.id,
                           title="Покупка подписки",
                           description="Подписка, дающая возможность получать раличные URLs",
                           provider_token=PAYMENTS_PROVIDER_TOKEN,
                           currency='rub',
                           photo_url=LUNTIC_URL,
                           photo_height=512,  # !=0/None, иначе изображение не покажется
                           photo_width=512,
                           photo_size=512,
                           is_flexible=False,  # True если конечная цена зависит от способа доставки
                           prices=[HELPING],
                           start_parameter='example',
                           payload="nothing")


@dp.shipping_query_handler(lambda query: True)
async def shipping(shipping_query: types.ShippingQuery):
    await bot.answer_shipping_query(shipping_query.id,
                                    ok=True,
                                    shipping_options=OPTION,
                                    error_message="Попробуй позже")


@dp.pre_checkout_query_handler(lambda query: True)
async def checkout(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id,
                                        ok=True,
                                        error_message="Не получилось")


@dp.message_handler(commands=["delete"])
async def del_user(message: types.Message):
    chat = message.chat
    bot.logger.info(chat)
    await message.chat.kick(user_id=285251903, until_date=(dt.datetime.now() + dt.timedelta(minutes=2)))
    bot.logger.info(f"User 285251903 deleted")
    return


@dp.message_handler(content_types=types.message.ContentTypes.SUCCESSFUL_PAYMENT)
async def got_payment(message: types.Message):
    await bot.send_message(message.chat.id,
                           "Юхуууу"
                           f"Твой заказ: {message.successful_payment.total_amount / 100} {message.successful_payment.currency}")
