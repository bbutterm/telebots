import time

import telebot
from telebot import apihelper
import sqlite3 as sql
from telebot import types
bot = telebot.TeleBot('995380002:AAH-LvUX2Cm9aiUGXAKcF777NyAYSUpFMKA')
apihelper.proxy = {'https':'https://167.86.80.2:3128'}
conn = sql.connect('db.db',check_same_thread=False)
cursor = conn.cursor()
cursor.execute("select id from users")
ids = cursor.fetchall()
conn.commit()
buff = []
for i in ids:
    buff.append(i[0])
print (buff)
@bot.message_handler(content_types=['text'])
def start(message):
    if (message.from_user.id) not in buff:
        bot.send_message(message.from_user.id, "Whats your name?");
        bot.register_next_step_handler(message, register);
    else:
        cursor.execute("select name from users where id = message.from_user.id")
        username = cursor.fetchall()
        bot.send_message(message.from_user.id,{}, "Hello", username);
def register(message):
    userid = message.from_user.id;
    username = message.text;
    print(userid);
    print(username);
    cursor.execute("insert into users (id,name) values (?,?)",((int(userid)),str(username)));
    conn.commit();


while True:
    try :
        bot.polling(none_stop=True,interval= 0,timeout=30)
    except:
        time.sleep(5)