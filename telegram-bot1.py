
import telebot
from telebot import types

token = "5014167121:AAGHJ24fLfioTF2os_Qo_TQA8_CpvNK2Eys"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу","/hello","/age","/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею...')

@bot.message_handler(commands=['hello'])
def hello(message):
    sent = bot.send_message(message.chat.id, 'Как тебя зовут?')
    bot.register_next_step_handler(sent, hello1)
def hello1(message):
    bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

@bot.message_handler(commands=['age'])
def age(message):
    sent=bot.send_message(message.chat.id, 'Какой сейчас год ?')
    bot.register_next_step_handler(sent,age1)
def age1(message):
    if message.text.lower() == '2022':
      bot.send_message(message.chat.id, 'Да, сейчас {name}.'.format(name=message.text))
    else: bot.send_message(message.chat.id, "Нет, сейчас 2022")

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')



bot.polling()