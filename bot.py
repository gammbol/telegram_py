import telebot
from telebot import types

bot  = telebot.TeleBot('2124840185:AAE1nh4vlzNfqRV_hzAjQVUvuZv3HgVQT0s')

#timetable data
chosen_time = ''
chosen_date = ''
chosen_lesson = ''
monday={}
tuesday = {}
wednesday = {}
thursday = {}
friday = {}
saturday = {}
sunday = {}

#start chatting with bot
@bot.message_handler(commands=['start'])
def start(message):
    sti = open('welcome_sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Доброго времени суток, <b>{0.first_name}</b>! \nС этого момента, я, <b>{1.first_name}</b>, буду вашим помощником\
 в составлении школьного расписания!".format(message.from_user, bot.get_me()), parse_mode='html')

#start of registration
@bot.message_handler(commands=['reg'])
def reg(message):
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('📝 Создать новое расписание')
    item2 = types.KeyboardButton('✏️ Изменить расписание')
    markup.add(item1,item2)

    bot.send_message(message.chat.id, 'Давай посмотрим, что тебе нужно:', reply_markup=markup)

#echo all messages
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == '📝 Создать новое расписание':
        bot.register_next_step_handler(message, create_new_timetable)
    elif message.text == '✏️ Изменить расписание':
        global monday, tuesday, wednesday, thursday, friday, saturday, sunday

        #checks dictionaries filling
        if monday=='' or tuesday=='' or wednesday=='' or thursday=='' or friday=='' or saturday=='' or sunday=='':
            bot.reply_to(message, 'Тебе нечего изменять!\nСоздай новое расписание!')

        #using keyboeard
        else:
            #keyboard
            date = types.ReplyKeyboardMarkup(resize_keyboard=True)
            mo = types.KeyboardButton('🌃 Понедельник')
            tu = types.KeyboardButton('🏙 Вторник')
            we = types.KeyboardButton('🏞 Среда')
            th = types.KeyboardButton('🌅 Четверг')
            fr = types.KeyboardButton('🌄 Пятница')
            sa = types.KeyboardButton('🌇 Суббота')
            su = types.KeyboardButton('🌌 Воскресенье')
            date.add(mo, tu, we, th, fr, sa, su).куп

            #question
            bot.send_message(message.chat.id, 'Хорошо!\nРасписание какого дня тебе нужно изменить?', reply_markup=date)

            #next registration step
            bot.register_next_step_handler(message, determine_date)
    else:
        bot.reply_to(message, 'У тебя нет друзей?\nПочему ты общаешься с ботом?')

#creating new timetable
def create_new_timetable(message):
    bot.send_message(message.chat.id, 'Хорошо! Тогда давай начнем с понедельника.\n\
        Отправь мне название урока или "0", чтобы закончить редактирование дня :)')
    if message.text == '0':
        bot.send_message(message.chat.id, 'Так, до сюда дошли))')

#determines a date of week
def determine_date(message):
    global chosen_date
    if message.text == '🌃 Понедельник':
        chosen_date = 'Понедельник'
        bot.send_message(message.chat.id, 'Теперь отправь название урока!')
        bot.register_next_step_handler(message, determine_lesson)
    elif message.text == '🏙 Вторник':
        chosen_date = 'Вторник'
        bot.send_message(message.chat.id, 'Теперь отправь название урока!')
        bot.register_next_step_handler(message, determine_lesson)
    elif message.text == '🏞 Среда':
        chosen_date = 'Среда'
        bot.send_message(message.chat.id, 'Теперь отправь название урока!')
        bot.register_next_step_handler(message, determine_lesson)
    elif message.text == '🌅 Четверг':
        chosen_date = 'Четверг'
        bot.send_message(message.chat.id, 'Теперь отправь название урока!')
        bot.register_next_step_handler(message, determine_lesson)
    elif message.text == '🌄 Пятница':
        chosen_date = 'Пятница'
        bot.send_message(message.chat.id, 'Теперь отправь название урока!')
        bot.register_next_step_handler(message, determine_lesson)
    elif message.text == '🌇 Суббота':
        chosen_date = 'Суббота'
        bot.send_message(message.chat.id, 'Теперь отправь название урока!')
        bot.register_next_step_handler(message, determine_lesson)
    elif message.text == '🌌 Воскресенье':
        chosen_date = 'Воскресенье'
        bot.send_message(message.chat.id, 'Теперь отправь название урока!')
        bot.register_next_step_handler(message, determine_lesson)
    else:
        bot.reply_to(message, 'Ты ввел что-то непонятное\n Пожалуйста, пользуйся уже данной тебе клавиатурой :)')

#determines a lesson
def determine_lesson(message):
    global chosen_lesson
    chosen_lesson = message.text

    bot.send_message(message.chat.id, 'Введи время начала урока!\n(Только вводи в форме HH:MM и в 24-часовом формате, например, 22:30)')
    bot.register_next_step_handler(message, confirm_timetable)

#confirms timetable
def confirm_timetable(message):
    global monday, tuesday, wednesday, thursday, friday, saturday, sunday, chosen_lesson, chosen_date, chosen_time
    chosen_time = str(message.text)
    
    #keyboard
    confirm = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton('Да, все верно!')
    no = types.KeyboardButton('Нет, я хочу кое-что изменить!')
    confirm.add(yes, no)

    #sends a message and makes next step
    bot.send_message(message.chat.id, 'Теперь давай все проверим)\n\
В {0.text}, {1} у тебя будет урок {2}. Верно?'.format(message,chosen_date,chosen_lesson), reply_markup=confirm)
    bot.register_next_step_handler(message, apply_changes)

#applies changes
def apply_changes(message):
    if message.text == 'Да, все верно!':
        global monday, tuesday, wednesday, thursday, friday, saturday, sunday, chosen_lesson, chosen_date, chosen_time
        #writing a lesson in dictionary
        if chosen_date == 'Понедельник':
            monday[chosen_lesson] = chosen_time
        elif chosen_date == 'Вторник':
            tuesday[chosen_lesson] = chosen_time
        elif chosen_date == 'Среда':
            wednesday[chosen_lesson] = chosen_time
        elif chosen_date == 'Четверг':
            thursday[chosen_lesson] = chosen_time
        elif chosen_date == 'Пятница':
            friday[chosen_lesson] = chosen_time
        elif chosen_date == 'Суббота':
            saturday[chosen_lesson] = chosen_time
        elif chosen_date == 'Воскресенье':
            sunday[chosen_lesson] = chosen_time

        bot.send_message(message.chat.id, 'Все! Я запомнил твой урок! Теперь можешь обращаться к этому расписанию,\
когда захочешь!')
    elif message.text == 'Нет, я хочу кое-что изменить!':
        bot.send_message(message.chat.id, 'Хорошо! Возвращаю тебя в начало!')
    else:
        bot.reply_to(message, 'Извини, но ты ввел что-то непонятное!')

bot.polling(none_stop=True, interval=0)