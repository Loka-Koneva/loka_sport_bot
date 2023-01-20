from telebot import types, TeleBot

import config_dev as config

WARM_UP_BUTTOM = 'Разминка/Заминка/Растяжка'
WARM_UP_LINK = 'Разминка: https://www.youtube.com/watch?v=j6C-6F6dr-4&ab_channel=ChloeTing \n' \
               'Растяжка: https://www.youtube.com/watch?v=iapsX8jB7k8&ab_channel=ChloeTing \n'

bot = TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcom_message(message):
    with open('./static/my_photo.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(WARM_UP_BUTTOM)
    markup.add(item1)

    with open('./static/welcom_message.txt', 'r') as text:
        bot.send_message(message.chat.id,
                         text.read().format(message.from_user.first_name),
                         reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == WARM_UP_BUTTOM:
            bot.send_message(message.chat.id, WARM_UP_LINK)


bot.polling(none_stop=True)
