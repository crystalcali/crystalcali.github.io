import logging
from aiogram import Bot, Dispatcher, executor, types
import sqlite3
from aiogram.types import CallbackQuery

import logging
from aiogram import Bot, Dispatcher, executor, types
import config as cfg
import markups as nav
import sqlite3
import tekst as txt
from db import Database
from aiogram.types import CallbackQuery

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')



#Старт и проверка на подписку
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        
        if not db.user_exists(message.from_user.id):
            start_command = message.text
            referer_id = str(str(start_command[7:]))
            if str(referer_id) != "":
                if str(referer_id) != str(message.from_user.id):
                    db.add_user(message.from_user.id, referer_id)
                    try:
                        username = message.from_user.username
                        await bot.send_message(referer_id, f"По вашей ссылке зарегестрировался новый {username}")
                    except:
                        pass
                else:
                    db.add_user(message.from_user.id)
                    await bot.send_message(message.from_user.id, "Нельзя регестрироваться по собственной ссылке!")
            else:
                db.add_user(message.from_user.id)
            
        with open('res/start.jpg', 'rb') as photo_file: 
            await bot.send_photo(message.from_user.id, photo_file, caption=txt.start_message, parse_mode=types.ParseMode.MARKDOWN, reply_markup=nav.start_keyboard)
        

@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 541540871:
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1] != 1):
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка")
#Обработчик подписки


@dp.callback_query_handler(text="wallet_button")
async def button1_callback(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    user_id = message.from_user.id
    profile_message = (
        f"👛***Ваш кошелек DM***\n"
        f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
        f"💳***Баланс: ***{Database.get_user_balance(user_id)} DM\n\n"
        f"🔑ID: ***{user_id}***\n"
        f"👤Всего рефералов: ***{Database.count_referer(user_id)}***\n"
        f"💎PRO STATUS: `не активно`\n"
        )
    await bot.send_message(message.from_user.id, profile_message, parse_mode=types.ParseMode.MARKDOWN,reply_markup=nav.profile_keyboard)
    
@dp.callback_query_handler(text="referer_button")
async def button2_callback(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    user_id = message.from_user.id
    ref_dir = f"`https://t.me/{cfg.BOT_NICKNAME}?start={user_id}`"
            
    referer_message = (
        f"🚀*** Пригласите друзей в нашего бота и зapабoтaйте DMcoin!***\n\n"
        f"***🔗 Ваша уникальная реферальная ссылка:***\n"+
        f"{ref_dir}\n\n"  
        f"***👥 Уже присоединились: {Database.count_referer(user_id)}***\n\n"
        f"***💰 За каждого приглашенного друга вы получаете 3 DMcoin в награду! Не упустите шанс заработать больше. Присоединяйтесь и приглашайте друзей прямо сейчас!***"
        )

    await bot.send_message(message.from_user.id, referer_message, parse_mode=types.ParseMode.MARKDOWN,reply_markup=nav.back_keyboard)

@dp.callback_query_handler(text="vip_button")
async def button3_callback(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    user_id = message.from_user.id
    VIP_message = (
        txt.vip_message
        )
    await bot.send_message(message.from_user.id, VIP_message,parse_mode=types.ParseMode.MARKDOWN,reply_markup=nav.back_keyboard)

@dp.callback_query_handler(text="example_button")
async def button4_callback(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    user_id = message.from_user.id
 
    example_message = (
        f"***{user_id}***, по этому ID не подключена систама оплаты, обратитесь у менеджеру!"
            )
    await bot.send_message(message.from_user.id, example_message,parse_mode=types.ParseMode.MARKDOWN,reply_markup=nav.back_keyboard)
   

@dp.callback_query_handler(text="ibtnOut")
async def button_callback(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Минимальная сумма вывода 10 DM", reply_markup=nav.back_keyboardPROF)

@dp.callback_query_handler(text="ibtnIn")
async def button_callback(message: types.Message):
    ton_adress = db.generate_ton_address()
    await bot.delete_message(message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, 
                           f"📪Ваш DM адрес:\n\n"
                           f"`{ton_adress}`", parse_mode=types.ParseMode.MARKDOWN, reply_markup=nav.back_keyboardPROF)

@dp.callback_query_handler(text="back_button")
async def button_callback(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    with open('res/start.jpg', 'rb') as photo_file: 
        await bot.send_photo(message.from_user.id, photo_file, caption=txt.start_message, parse_mode=types.ParseMode.MARKDOWN, reply_markup=nav.start_keyboard)

@dp.callback_query_handler(text="back_buttonPROF")
async def button_callback(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message.message_id)
    user_id = message.from_user.id
    profile_message = (
        f"👛***Ваш кошелек DM***\n"
        f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
        f"💳***Баланс: ***{Database.get_user_balance(user_id)} DM\n\n"
        f"🔑ID: ***{user_id}***\n"
        f"👤Всего рефералов: ***{Database.count_referer(user_id)}***\n"
        f"💎PRO STATUS: `не активно`\n"
        )
    await bot.send_message(message.from_user.id, profile_message, parse_mode=types.ParseMode.MARKDOWN, reply_markup=nav.profile_keyboard)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)