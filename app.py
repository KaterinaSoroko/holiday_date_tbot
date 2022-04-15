import telebot
import bot.bot as mes
from bot.constans import TOKEN, ID_CHAT


token = TOKEN

bot = telebot.TeleBot(token)


date_today = mes.get_data()
answer_message = mes.prepare_message(date_today)
bot.send_message(ID_CHAT, answer_message)
