import telebot
import threading
import time
import schedule

TOKEN = "8697245449:AAGtpJ9CQHPnXDwqQQai-c1aQO0DXr9cv_s"

bot = telebot.TeleBot(TOKEN)

users = set()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "test ❤️")

def send_heart():
    for user_id in users:
        try:
            bot.send_message(user_id, "❤️")
        except:
            pass

schedule.every().day.at("00:00").do(send_heart)

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=scheduler).start()

print("Bot is running...")

bot.infinity_polling()
