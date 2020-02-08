import time

import telebot
from telebot import apihelper
import sqlite3 as sql
from telebot import types
bot = telebot.TeleBot('995380002:AAH-LvUX2Cm9aiUGXAKcF777NyAYSUpFMKA')
apihelper.proxy = {'https':'https://64.227.2.136:8080'}
conn = sql.connect('db.db',check_same_thread=False)
cursor = conn.cursor()
cursor.execute("select id from users")
ids = cursor.fetchall()
conn.commit()
buff = []
for i in ids:
    buff.append(i[0])
print (buff)
cursor.execute("select * from users");
base = cursor.fetchall();
print(base)
cursor.execute("select name from snus")
snusname = cursor.fetchall()
snusbase = []
for i in snusname:
    snusbase.append(i[0])
print (snusbase)
@bot.message_handler(content_types=['text'])
def start(message):
    if (message.from_user.id) not in buff:
        bot.send_message(message.from_user.id, "Whats your name?");
        bot.register_next_step_handler(message, register);
    else:
        cursor.execute("select name from users where id = ?",(message.from_user.id,))
        name = str(cursor.fetchall())
        username = name.replace("[","").replace("'","").replace("(","").replace(")","").replace("]","").replace(",","");
        print (username)
        bot.send_message(message.from_user.id,f'Hello, {username}')
        choose(message)
def register(message):
    userid = message.from_user.id;
    username = message.text;
    print(userid);
    print(username);
    cursor.execute("insert into users (id,name) values (?,?)",((int(userid)),str(username)));
    conn.commit();
@bot.message_handler(commands=['buy','pricelist'])
def choose(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('buy', 'pricelist')  # Имена кнопок
    msg = bot.reply_to(message, 'why are you asking me?', reply_markup=markup)
    bot.register_next_step_handler(msg, process_step)
def pricelist(message)

def process_step(message):
    chat_id = message.chat.id
    if message.text == 'buy':
        bot.register_next_step_handler(message, shop);
    else:
        bot.register_next_step_handler(message, pricelist);
while True:
    try :
        bot.polling(none_stop=True,interval= 0,timeout=30)
    except:
        time.sleep(5)