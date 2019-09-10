import telebot
from telebot import types
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
        title = jikan.anime(title['results'][0]['mal_id'])
        #bot.send_message(message.chat.id, title['synopsis'])
        
        keyboard = types.InlineKeyboardMarkup();
       
        keyboard.row(
        telebot.types.InlineKeyboardButton(text='Synopsis', callback_data='synopsis'),
        #keyboard.add(key_synopsis);

        telebot.types.InlineKeyboardButton(text='Knopka', callback_data='knopka'),
        #keyboard.add(key_synopsis1);

        telebot.types.InlineKeyboardButton(text='hujopka', callback_data='hujopka')
        #keyboard.add(key_synopsis2);
        )

        caption = "*Title*: " + title['title']
        bot.send_photo(message.chat.id, title['image_url'], caption, reply_markup=keyboard, parse_mode="MARKDOWN")

    @bot.callback_query_handler(func=lambda call: True)
    def callback_synopsis(call):
        if call.data == "synopsis": 
            bot.send_message(call.message.chat.id, "*Synopsis for "+title['title']+"*"+"\n"+title['synopsis'],parse_mode="MARKDOWN");

bot.polling(none_stop=True, interval=0)



