import telebot
from telebot import types

bot  = telebot.TeleBot('2124840185:AAE1nh4vlzNfqRV_hzAjQVUvuZv3HgVQT0s')

#start chatting with bot
@bot.message_handler(commands=['start'])
def start(message):
    sti = open('welcome_sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Доброго времени суток, <b>{0.first_name}</b>! \nС этого момента, я, <b>{1.first_name}</b>, буду вашим помощником\
 в составлении школьного расписания!".format(message.from_user, bot.get_me()), parse_mode='html')

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('📝 Создать новое расписание')
    item2 = types.KeyboardButton('✏️ Изменить расписание')
    markup.add(item1,item2)

    bot.send_message(message.chat.id, 'Давай посмотрим, что тебе нужно:', reply_markup=markup)

bot.polling(none_stop=True, interval=0)