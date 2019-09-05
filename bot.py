import telebot

bot = telebot.TeleBot("DSN")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Бот работает да")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['search'])
def search_anime(message):
	if message.text != "/search":
		bot.send_message(message.chat.id, message.text[8:])



bot.polling()
