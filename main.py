import telebot
import config_dev as config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcom_message(message):
    with open('./static/my_photo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    with open('./static/welcom_message.txt', 'r') as text:
        bot.send_message(message.chat.id, text.read().format(message.from_user.first_name))

@bot.message_handler(content_types=['text'])
def lalala(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
