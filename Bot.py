import telebot
import random
import time
import json
from encodings.aliases import aliases

i= 0
bot = telebot.TeleBot('7409771005:AAFLG21JkNmhssJy--f32szVI47fAdZqCJE')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Организация мероприятия', 'Взять отгул от занятий', 'Все мероприятия', '' )
keyboard1.row('Назад')

@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(message.from_user.id, "Что вам нужно?", reply_markup = keyboard)

@bot.message_handler(content_types=['text'])
def text(message):
     if message.text == 'Взять отгул от занятий':
          # # global msg

          cid = message.chat.id
          msg = bot.send_message(cid, 'Введите дату и занятие(я) которые нужно пропустить' "\n" + 'Формат сообщения (ФИО, Группа, Клуб, 12.05 1/3 пары)', reply_markup = keyboard1)
          bot.register_next_step_handler(msg, after_daysoff) 

     elif message.text == 'Организация мероприятия':
          cid = message.chat.id
          msg = bot.send_message(cid, 'Введите Название мероприятия, его тип, желаемую дату', reply_markup = keyboard1)
          bot.register_next_step_handler(msg, after_mp) 
     
     elif message.text == 'Все мероприятия':

          cid = message.chat.id
          srt = open('db_mp.json', mode='r', encoding='utf-8')
          bot.send_message(cid, srt)

               

     elif message.text == 'Назад':
         bot.send_message(message.from_user.id, 'Что бы вы хотели сделать?', reply_markup = keyboard)
     else:
         bot.send_message(message.from_user.id, 'Я вас не понимаю')

def after_daysoff(message):
     a = message.text
     cid = message.chat.id
     bot.send_message(cid, 'Данные записаны!'.format(a))
     data = {}
     data['daysoff'] = []
     data['daysoff'] .append ({
          'student':  a })
     with open('daysoff.json','a', encoding='utf-8') as out:
          json.dump(data, out, ensure_ascii=False)
     


def after_mp(message):
     b = message.text
     h = message.text
     v = str(b)
     cid = message.chat.id
     bot.send_message(cid, 'Данные записаны!'.format(b))
     data = {}
     data['db_mp'] = []
     data['db_mp'] .append ({
          'student':  v})
     with open('db_mp.json','a', encoding='utf-8') as outfile:
          json.dump(data, outfile, ensure_ascii=False)


bot.polling(none_stop=True, interval=0)