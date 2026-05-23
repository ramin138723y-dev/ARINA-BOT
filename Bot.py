import telebot
import time
import threading
import json
import os

TOKEN = "8697245449:AAGtpJ9CQHPnXDwqQQai-c1aQO0DXr9cv_s"
bot = telebot.TeleBot(TOKEN)

FILE = "users.json"

# لود کاربران
def load_users():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return set(json.load(f))
    return set()

# ذخیره کاربران
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
    while True:
        now = time.strftime("%H:%M")
        if now == "00:00":
            for u in list(users):
                try:
                    bot.send_message(u, "❤️")
                except:
                    pass
            time.sleep(60)
        time.sleep(1)

threading.Thread(target=send_daily).start()

print("Bot is running...")
bot.infinity_polling()
