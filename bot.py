import telebot
from jikanpy import Jikan

bot = telebot.TeleBot("674936263:AAEVPh_lLAwGkdaUKaE3q_E2gkeRjp0vvys")
jikan = Jikan()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Бот работает да")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['search'])
def search_anime(message):
    if message.text != "/search":
        title = jikan.search("anime", message.text[8:])
        title = jikan.anime(title['results'][1]['mal_id'])
        #bot.send_message(message.chat.id, title['synopsis'])
        caption = "Title: " + title['title'] + "\nSynosysis: " + title['synopsis']
        bot.send_photo(message.chat.id, title['image_url'], caption)


bot.polling()
