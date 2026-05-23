import telebot
import threading
import time
import json
import os
import pytz
from datetime import datetime

TOKEN = "8697245449:AAGtpJ9CQHPnXDwqQQai-c1aQO0DXr9cv_s"
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

def send_daily():
    tehran = pytz.timezone("Asia/Tehran")

    sent_today = False

    while True:
        now = datetime.now(tehran).strftime("%H:%M")

        if now == "00:00" and not sent_today:
            for u in list(users):
                try:
                    bot.send_message(u, "❤️")
                except:
                    pass
            sent_today = True

        if now != "00:00":
            sent_today = False

        time.sleep(1)

threading.Thread(target=send_daily).start()

print("Bot is running...")
bot.infinity_polling()
