from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import tekst as txt




mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
btnProfile = KeyboardButton(txt.profile_text)
btnReferer = KeyboardButton(txt.referer_text)
btnVIP = KeyboardButton(txt.VIP_text)
mainMenu.add(btnProfile)
mainMenu.add(btnReferer)
mainMenu.add(btnVIP)

back_button = InlineKeyboardButton("Назад", callback_data="back_button")
back_buttonPROF = InlineKeyboardButton("Назад", callback_data="back_buttonPROF")

start_keyboard = InlineKeyboardMarkup()
wallet_button = InlineKeyboardButton(txt.profile_text, callback_data="wallet_button") 
referer_button = InlineKeyboardButton(txt.referer_text, callback_data="referer_button") 
example_button = InlineKeyboardButton(txt.example_text, callback_data="example_button") 
vip_button = InlineKeyboardButton(txt.VIP_text, callback_data="vip_button")
start_keyboard.add(wallet_button)
start_keyboard.add(referer_button)
start_keyboard.add(vip_button)
start_keyboard.add(example_button)
profile_keyboard = InlineKeyboardMarkup(row_width=2)
ibtnIn = InlineKeyboardButton("Получить", callback_data="ibtnIn")
ibtnOut = InlineKeyboardButton("Вывод", callback_data="ibtnOut")
profile_keyboard.add(ibtnOut, ibtnIn)
profile_keyboard.add(back_button)
back_keyboard = InlineKeyboardMarkup()
back_keyboard.add(back_button)
back_keyboardPROF = InlineKeyboardMarkup()
back_keyboardPROF.add(back_buttonPROF)
