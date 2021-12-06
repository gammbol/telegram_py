import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('2124840185:AAE1nh4vlzNfqRV_hzAjQVUvuZv3HgVQT0s')

#timetable data
chosen_time = ''
chosen_date = ''
chosen_lesson = ''
lesson_end_time = ''
lesson_start_time = ''

#data base
connect = sqlite3.connect('timetable.db', check_same_thread=False)
cursor = connect.cursor()

#creating timetable
cursor.execute("""CREATE TABLE IF NOT EXISTS timetable(
    id INTEGER,
    lesson VARCHAR,
    date VARCHAR,
    start VARCHAR,
    end VARCHAR    
)""")
connect.commit()

#keyboard
date = types.ReplyKeyboardMarkup(resize_keyboard=True)
mo = types.KeyboardButton('🌃 Понедельник')
tu = types.KeyboardButton('🏙 Вторник')
we = types.KeyboardButton('🏞 Среда')
th = types.KeyboardButton('🌅 Четверг')
fr = types.KeyboardButton('🌄 Пятница')
sa = types.KeyboardButton('🌇 Суббота')
su = types.KeyboardButton('🌌 Воскресенье')
date.add(mo, tu, we, th, fr, sa, su)

#keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('📝 Создать новое расписание')
item2 = types.KeyboardButton('✏️ Изменить расписание')
item3 = types.KeyboardButton('🔍 Показать расписание')
markup.add(item1,item2,item3)

action = types.ReplyKeyboardMarkup(resize_keyboard=True)
add = types.KeyboardButton('📌 Добавить')
delete = types.KeyboardButton('❌ Удалить')
action.add(add, delete)

#start chatting with bot
@bot.message_handler(commands=['start'])
def start(message):
    sti = open('welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Доброго времени суток, <b>{0.first_name}</b>! \nС этого момента, я, <b>{1.first_name}</b>,\
буду вашим помощником в составлении школьного расписания!".format(message.from_user, bot.get_me()), parse_mode='html')
    bot.send_message(message.chat.id, 'Отправьте мне \'/reg\', чтобы начать работу!')

#start of registration
@bot.message_handler(commands=['reg'])
def reg(message):
    bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)

#echo all messages
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == '📝 Создать новое расписание':
        #keyboard
        choice = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y = types.KeyboardButton('🟩 Да, уверен(-а)')
        n = types.KeyboardButton('🟥 Нет, не уверен(-а)')
        choice.add(y,n)

        bot.send_message(message.chat.id, 'Вы уверены?\nЭто удалит все ваше расписание!', reply_markup=choice)
        bot.register_next_step_handler(message, create_new_timetable)
    elif message.text == '✏️ Изменить расписание':
        global monday, tuesday, wednesday, thursday, friday, saturday, sunday

        #next registration step
        bot.send_message(message.chat.id, 'Как именно вы хотите изменить свое расписание?', reply_markup=action)
        bot.register_next_step_handler(message, choosing_action)
    elif message.text == '🔍 Показать расписание':
        bot.send_message(message.chat.id, 'Расписание какого дня вы хотите посмотреть?', reply_markup=date)
        bot.register_next_step_handler(message, show_timetable)
    else:
        bot.reply_to(message, 'У тебя нет друзей?\nПочему ты общаешься с ботом?')

#shows timetable
def show_timetable(message):
    user_id = message.chat.id
    if message.text == '🌃 Понедельник':
        cursor.execute(f"SELECT * FROM timetable WHERE id = {user_id} AND date = 'Понедельник'")
        data = cursor.fetchall()
        if data:
            for row in data: 
                bot.send_message(message.chat.id, '{0}: {1} - {2}'.format(row[1], row[3], row[4]))
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        else:
            bot.reply_to(message, 'Мне нечего показывать!\nВаше расписание пустое!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    elif message.text == '🏙 Вторник':
        cursor.execute(f"SELECT * FROM timetable WHERE id = {user_id} AND date = 'Вторник'")
        data = cursor.fetchall()
        if data:
            for row in data: 
                bot.send_message(message.chat.id, '{0}: {1} - {2}'.format(row[1], row[3], row[4]))
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        else:
            bot.reply_to(message, 'Мне нечего показывать!\nВаше расписание пустое!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    elif message.text == '🏞 Среда':
        cursor.execute(f"SELECT * FROM timetable WHERE id = {user_id} AND date = 'Среда'")
        data = cursor.fetchall()
        if data:
            for row in data: 
                bot.send_message(message.chat.id, '{0}: {1} - {2}'.format(row[1], row[3], row[4]))
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        else:
            bot.reply_to(message, 'Мне нечего показывать!\nВаше расписание пустое!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    elif message.text == '🌅 Четверг':
        cursor.execute(f"SELECT * FROM timetable WHERE id = {user_id} AND date = 'Четверг'")
        data = cursor.fetchall()
        if data:
            for row in data: 
                bot.send_message(message.chat.id, '{0}: {1} - {2}'.format(row[1], row[3], row[4]))
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        else:
            bot.reply_to(message, 'Мне нечего показывать!\nВаше расписание пустое!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    elif message.text == '🌄 Пятница':
        cursor.execute(f"SELECT * FROM timetable WHERE id = {user_id} AND date = 'Пятница'")
        data = cursor.fetchall()
        if data:
            for row in data: 
                bot.send_message(message.chat.id, '{0}: {1} - {2}'.format(row[1], row[3], row[4]))
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        else:
            bot.reply_to(message, 'Мне нечего показывать!\nВаше расписание пустое!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    elif message.text == '🌇 Суббота':
        cursor.execute(f"SELECT * FROM timetable WHERE id = {user_id} AND date = 'Суббота'")
        data = cursor.fetchall()
        if data:
            for row in data: 
                bot.send_message(message.chat.id, '{0}: {1} - {2}'.format(row[1], row[3], row[4]))
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        else:
            bot.reply_to(message, 'Мне нечего показывать!\nВаше расписание пустое!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    elif message.text == '🌌 Воскресенье':
        cursor.execute(f"SELECT * FROM timetable WHERE id = {user_id} AND date = 'Воскресенье'")
        data = cursor.fetchall()
        if data:
            for row in data: 
                bot.send_message(message.chat.id, '{0}: {1} - {2}'.format(row[1], row[3], row[4]))
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        else:
            bot.reply_to(message, 'Мне нечего показывать!\nВаше расписание пустое!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    else:
        bot.reply_to(message, 'Вы ввели что-то непонятное\nПожалуйста, пользуйтесь уже данной вам клавиатурой :)')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)
    

#creating new timetable
def create_new_timetable(message):
    user_id = message.chat.id
    if message.text == '🟩 Да, уверен(-а)':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id}")
        connect.commit()

        bot.send_message(message.chat.id, 'Ваше расписание было успешно сброшено!')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)
    elif message.text == '🟥 Нет, не уверен(-а)':
        bot.send_message(message.chat.id, 'Хорошо! Возвращаю вас в начало!')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)
    else:
        bot.reply_to(message, 'Вы ввели что-то непонятное\nПожалуйста, пользуйтесь уже данной вам клавиатурой :)')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)

#choses action to do (delete or add)
def choosing_action(message):
    if message.text == '❌ Удалить':
        bot.send_message(message.chat.id, 'Укажите день, в котором урок нужно удалить', reply_markup=date)
        bot.register_next_step_handler(message, determine_date_to_delete)
    elif message.text == '📌 Добавить':
            #question
            bot.send_message(message.chat.id, 'Хорошо!\nРасписание какого дня вам нужно изменить?', reply_markup=date)

            #next registration step
            bot.register_next_step_handler(message, determine_date)

#detirmines date to delete
def determine_date_to_delete(message):
    global chosen_date
    if message.text == '🌃 Понедельник':
        chosen_date = 'Понедельник'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, delete_lesson)
    elif message.text == '🏙 Вторник':
        chosen_date = 'Вторник'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, delete_lesson)
    elif message.text == '🏞 Среда':
        chosen_date = 'Среда'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, delete_lesson)
    elif message.text == '🌅 Четверг':
        chosen_date = 'Четверг'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, delete_lesson)
    elif message.text == '🌄 Пятница':
        chosen_date = 'Пятница'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, delete_lesson)
    elif message.text == '🌇 Суббота':
        chosen_date = 'Суббота'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, delete_lesson)
    elif message.text == '🌌 Воскресенье':
        chosen_date = 'Воскресенье'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, delete_lesson)
    else:
        bot.reply_to(message, 'Вы ввели что-то непонятное\nПожалуйста, пользуйтесь уже данной вам клавиатурой :)')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)

#deletes determined lesson
def delete_lesson(message):
    user_id = message.chat.id
    lesson_to_delete = message.text
    if chosen_date == 'Понедельник':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id} AND date = 'Понедельник' AND lesson = '{lesson_to_delete}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Урок был успешно удален!\n\
Направляю вас в начало диалога')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)


    elif chosen_date == 'Вторник':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id} AND date = 'Вторник' AND lesson = '{lesson_to_delete}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Урок был успешно удален!\n\
Направляю вас в начало диалога')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)


    elif chosen_date == 'Среда':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id} AND date = 'Среда' AND lesson = '{lesson_to_delete}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Урок был успешно удален!\n\
Направляю вас в начало диалога')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)


    elif chosen_date == 'Четверг':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id} AND date = 'Четверг' AND lesson = '{lesson_to_delete}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Урок был успешно удален!\n\
Направляю вас в начало диалога')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)


    elif chosen_date == 'Пятница':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id} AND date = 'Пятница' AND lesson = '{lesson_to_delete}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Урок был успешно удален!\n\
Направляю вас в начало диалога')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)


    elif chosen_date == 'Суббота':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id} AND date = 'Суббота' AND lesson = '{lesson_to_delete}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Урок был успешно удален!\n\
Направляю вас в начало диалога')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)


    elif chosen_date == 'Воскресенье':
        cursor.execute(f"DELETE FROM timetable WHERE id = {user_id} AND date = 'Воскресенье' AND lesson = '{lesson_to_delete}'")
        connect.commit()
        bot.send_message(message.chat.id, 'Урок был успешно удален!\n\
Направляю вас в начало диалога')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)


    else:
        bot.reply_to(message, 'Вы ввели что-то непонятное\n Пожалуйста, пользуйтесь уже данной вам клавиатурой :)')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)

#determines a date of week
def determine_date(message):
    global chosen_date
    if message.text == '🌃 Понедельник':
        chosen_date = 'Понедельник'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, lesson_starts)
    elif message.text == '🏙 Вторник':
        chosen_date = 'Вторник'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, lesson_starts)
    elif message.text == '🏞 Среда':
        chosen_date = 'Среда'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, lesson_starts)
    elif message.text == '🌅 Четверг':
        chosen_date = 'Четверг'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, lesson_starts)
    elif message.text == '🌄 Пятница':
        chosen_date = 'Пятница'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, lesson_starts)
    elif message.text == '🌇 Суббота':
        chosen_date = 'Суббота'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, lesson_starts)
    elif message.text == '🌌 Воскресенье':
        chosen_date = 'Воскресенье'
        bot.send_message(message.chat.id, 'Теперь отправьте название урока!')
        bot.register_next_step_handler(message, lesson_starts)
    else:
        bot.reply_to(message, 'Вы ввели что-то непонятное\n Пожалуйста, пользуйтесь уже данной вам клавиатурой :)')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)

#determines a lesson
def lesson_starts(message):
    global chosen_lesson
    chosen_lesson = message.text

    bot.send_message(message.chat.id, 'Введите время начала урока!\n\
(Только вводите в форме HH:MM и в 24-часовом формате, например, 12:30)')
    bot.register_next_step_handler(message, lesson_ends)

def lesson_ends(message):
    global lesson_start_time
    lesson_start_time = message.text
    bot.send_message(message.chat.id, 'Теперь введите время конца урока!\n\
(Только вводите в форме HH:MM и в 24-часовом формате, например, 12:30)')
    bot.register_next_step_handler(message, confirm_timetable)

#confirms timetable
def confirm_timetable(message):
    global chosen_lesson, chosen_date, lesson_start_time, lesson_end_time
    lesson_end_time = message.text
    
    #keyboard
    confirm = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yes = types.KeyboardButton('🟢 Да, все верно!')
    no = types.KeyboardButton('🔴 Нет, я хочу кое-что изменить!')
    confirm.add(yes, no)

    #sends a message and makes next step
    bot.send_message(message.chat.id, 'Теперь давайте все проверим)\n\
В {0}, {1} у вас будет урок {2}, который закончится в {3}. \
Верно?'.format(lesson_start_time,chosen_date,chosen_lesson, lesson_end_time), reply_markup=confirm)
    bot.register_next_step_handler(message, apply_changes)

#applies changes
def apply_changes(message):
    if message.text == '🟢 Да, все верно!':
        global chosen_lesson, chosen_date, lesson_start_time, lesson_end_time
        #writing a lesson in db
        if chosen_date == 'Понедельник':
            cursor.execute(f"INSERT INTO timetable VALUES (?, ?, ?, ?, ?)", (message.chat.id, chosen_lesson, chosen_date, lesson_start_time, lesson_end_time))
            connect.commit()
            bot.send_message(message.chat.id, 'Ваш урок был успешно добавлен!\nВозвращаю вас в начало!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        elif chosen_date == 'Вторник':
            cursor.execute(f"INSERT INTO timetable VALUES (?, ?, ?, ?, ?)", (message.chat.id, chosen_lesson, chosen_date, lesson_start_time, lesson_end_time))
            connect.commit()
            bot.send_message(message.chat.id, 'Ваш урок был успешно добавлен!\nВозвращаю вас в начало!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        elif chosen_date == 'Среда':
            cursor.execute(f"INSERT INTO timetable VALUES (?, ?, ?, ?, ?)", (message.chat.id, chosen_lesson, chosen_date, lesson_start_time, lesson_end_time))
            connect.commit()
            bot.send_message(message.chat.id, 'Ваш урок был успешно добавлен!\nВозвращаю вас в начало!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        elif chosen_date == 'Четверг':
            cursor.execute(f"INSERT INTO timetable VALUES (?, ?, ?, ?, ?)", (message.chat.id, chosen_lesson, chosen_date, lesson_start_time, lesson_end_time))
            connect.commit()
            bot.send_message(message.chat.id, 'Ваш урок был успешно добавлен!\nВозвращаю вас в начало!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        elif chosen_date == 'Пятница':
            cursor.execute(f"INSERT INTO timetable VALUES (?, ?, ?, ?, ?)", (message.chat.id, chosen_lesson, chosen_date, lesson_start_time, lesson_end_time))
            connect.commit()
            bot.send_message(message.chat.id, 'Ваш урок был успешно добавлен!\nВозвращаю вас в начало!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        elif chosen_date == 'Суббота':
            cursor.execute(f"INSERT INTO timetable VALUES (?, ?, ?, ?, ?)", (message.chat.id, chosen_lesson, chosen_date, lesson_start_time, lesson_end_time))
            connect.commit()
            bot.send_message(message.chat.id, 'Ваш урок был успешно добавлен!\nВозвращаю вас в начало!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)
        elif chosen_date == 'Воскресенье':
            cursor.execute(f"INSERT INTO timetable VALUES (?, ?, ?, ?, ?)", (message.chat.id, chosen_lesson, chosen_date, lesson_start_time, lesson_end_time))
            connect.commit()
            bot.send_message(message.chat.id, 'Ваш урок был успешно добавлен!\nВозвращаю вас в начало!')
            bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
            bot.register_next_step_handler(message, echo_all)

    elif message.text == '🔴 Нет, я хочу кое-что изменить!':
        bot.send_message(message.chat.id, 'Хорошо! Возвращаю вас в начало!')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)
    else:
        bot.reply_to(message, 'Извините, но вы ввели что-то непонятное!')
        bot.send_message(message.chat.id, 'Давайте посмотрим, что вам нужно:', reply_markup=markup)
        bot.register_next_step_handler(message, echo_all)

bot.polling(none_stop=True, interval=0)