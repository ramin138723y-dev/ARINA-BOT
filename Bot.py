import telebot
import json
import os
from datetime import datetime
import pytz
import schedule
import time
import threading

TOKEN = "توکن_بات"
bot = telebot.TeleBot(TOKEN)

FILE = "users.json"

def load_users():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_users():
    with open(FILE, "w") as f:
        json.dump(list(users), f)

users = load_users()

@bot.message_handler(commands=['start'])
def start(message):
    users.add(message.chat.id)
    save_users()
    bot.send_message(message.chat.id, "❤️")

def job():
    for u in list(users):
        try:
            bot.send_message(u, "❤️")
        except:
            pass

# ساعت ایران
schedule.every().day.at("00:00").do(job)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=run_schedule).start()

print("Bot running...")
bot.infinity_polling()
