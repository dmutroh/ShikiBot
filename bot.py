import telebot
from telebot import types
from jikanpy import Jikan


bot = telebot.TeleBot("674936263:AAEVPh_lLAwGkdaUKaE3q_E2gkeRjp0vvys")
jikan = Jikan()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Бот работает да")


@bot.message_handler(commands=['anime'])
def search_anime(message):
    if message.text != "/anime":
        title = jikan.search("anime", message.text[7:])
        if len(title['results']) == 0:
            bot.send_message(message.chat.id, "Not Found!")
            return 0
        title_id = title['results'][0]['mal_id']
        title = jikan.anime(title_id)

        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(text='\U0001F4C3', callback_data='synopsis_' + 'anime_' + str(title_id)),
            telebot.types.InlineKeyboardButton(text='\U0001F5BC', callback_data='screenshots_' + 'anime_' + str(title_id)),
            telebot.types.InlineKeyboardButton(text='\U0001F4AC', callback_data='comments_' + 'anime_' + str(title_id))
        )

        caption = "*Title*: " + title['title']
        bot.send_photo(message.chat.id, title['image_url'], caption, reply_markup=keyboard, parse_mode="MARKDOWN")


@bot.message_handler(commands=['manga'])
def search_manga(message):
    if message.text != "/manga":
        title = jikan.search("manga", message.text[7:])
        if len(title['results']) == 0:
            bot.send_message(message.chat.id, "Not Found!")
            return 0
        title_id = title['results'][0]['mal_id']
        title = jikan.manga(title_id)
        # bot.send_message(message.chat.id, title['synopsis'])

        keyboard = types.InlineKeyboardMarkup()

        keyboard.row(
            telebot.types.InlineKeyboardButton(text='\U0001F4C3', callback_data='synopsis_' + 'manga_' + str(title_id)),
            # telebot.types.InlineKeyboardButton(text='\U0001F5BC', callback_data='screenshots_' + 'manga_' + str(title_id)),
            telebot.types.InlineKeyboardButton(text='\U0001F4AC', callback_data='comments_' + 'manga_' + str(title_id))
        )

        caption = "*Title*: " + title['title']
        bot.send_photo(message.chat.id, title['image_url'], caption, reply_markup=keyboard, parse_mode="MARKDOWN")


@bot.callback_query_handler(func=lambda call: True)
def callback_synopsis(call):
    if call.data.split('_')[0] == "synopsis":
        title_id = call.data.split('_')[2]
        if call.data.split('_')[1] == 'anime':
            bot.send_message(call.message.chat.id, "*Synopsis for " + jikan.anime(title_id)['title'] + "*" + "\n" +
                             jikan.anime(title_id)['synopsis'], parse_mode="MARKDOWN")
        if call.data.split('_')[1] == 'manga':
            bot.send_message(call.message.chat.id, "*Synopsis for " + jikan.manga(title_id)['title'] + "*" + "\n" +
                             jikan.manga(title_id)['synopsis'], parse_mode="MARKDOWN")


bot.polling(none_stop=True, interval=0)
