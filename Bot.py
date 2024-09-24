import telebot
import random
import time
import json
from encodings.aliases import aliases
# import key

i= 0
bot = telebot.TeleBot('7272108290:AAGB6OnZfmwiaWZwQgy8asVh2J3oohXkZyg')

keyboard = telebot.types.ReplyKeyboardMarkup(True, True, True, True)
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Организация мероприятия', 'Взять отгул от занятий', 'Все мероприятия', 'Составы клубов' )
keyboard1.row('Назад')

@bot.message_handler(commands=['start'])
def start_messages(message):
    bot.send_message(message.from_user.id, "Что вам нужно?", reply_markup = keyboard)

@bot.message_handler(content_types=['text'])
def text(message):



#обработка запроса и его запись
     if message.text == 'Взять отгул от занятий':
          cid = message.chat.id
          msg = bot.send_message(cid, 'Введите дату и занятие(я) которые нужно пропустить' "\n" + 'Формат сообщения (ФИО, Группа, Клуб, 12.05 1/3 пары)')
          if msg == 'Назад':
               bot.send_message(cid, '')
          else:
               bot.register_next_step_handler(msg, after_daysoff)
     elif message.text == 'Организация мероприятия':
          cid = message.chat.id
          msg = bot.send_message(cid, 'Введите Название мероприятия, его тип, желаемую дату')
          if msg == 'Назад':
               bot.send_message(cid, '')
          else:
               bot.register_next_step_handler(msg, after_mp)


#обработка файла и вывод из него данных
     elif message.text == 'Все мероприятия':
            global data1
            srt = open('db_mp.json', mode='r', encoding='utf-8')
            zov = json.load(srt)
            
            cid = message.chat.id
            msg = zov['events'][0]['student']
            bot.send_message(cid, msg)
     elif message.text == 'Составы клубов':
          cid = message.chat.id
          mem = open('clubM.json', mode='r', encoding='utf-8')
          bot.send_message(cid, mem)


     elif message.text == 'Назад':
         bot.send_message(message.from_user.id, 'Что бы вы хотели сделать?', reply_markup = keyboard)
     
     else:
         bot.send_message(message.from_user.id, 'Я вас не понимаю')



#Функции записи данных в json
def after_daysoff(message):
     global data1
     a = message.text
     cid = message.chat.id
     bot.send_message(cid, 'Данные записаны!', reply_markup = keyboard1)
     data1 = {}
     data1['off'] = []
     data1['off'] .append ({
          'user': a})
     with open('daysoff.json','a', encoding='utf-8') as out:
          json.dump(data1, out, ensure_ascii=False)

def after_mp(message):
     b = message.text
     h = message.text
     v = str(b)
     cid = message.chat.id
     bot.send_message(cid, 'Данные записаны!',reply_markup = keyboard1)
     data = {}
     data['events'] = []
     data['events'] .append ({
          'student':  v})
     with open('db_mp.json','a', encoding='utf-8') as outfile:
          json.dump(data, outfile, ensure_ascii=False)


bot.polling(none_stop=True, interval=0)
