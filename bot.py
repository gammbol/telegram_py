import telebot
bot = telebot.TeleBot('2124840185:AAE1nh4vlzNfqRV_hzAjQVUvuZv3HgVQT0s')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, 'Привет! Чем могу помочь?')

bot.polling(none_stop=True, interval=0)