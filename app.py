import telebot
import bot.bot as mes
from bot.constans import TOKEN, ID_CHAT


token = TOKEN

bot = telebot.TeleBot(token)

bot.send_message(ID_CHAT, mes.answer_message)

