import requests
import telebot
import time
from dotenv import load_dotenv
import os

load_dotenv()
token_tel = os.environ.get("TOKEN_TELEGRAM")
url = "https://dvmn.org/api/long_polling/"
token_dev =os.environ.get("TOKEN_DEVMAN")
header = {
    "Authorization": f"Token {token_dev}"
}
params = {"timestamp": 1555493856}
bot = telebot.TeleBot(token_tel)
chat_id=os.environ.get("chat_id")

@bot.message_handler(commands=["start"])
def start(message):
    while True:
        try:
            response = requests.get(url, params=params, headers=header, timeout=60)
            if response.ok:
                data = response.json()
                if data["status"] == "found":
                    attempts = data["new_attempts"]
                    for attempt in attempts:
                        lesson_title = attempt["lesson_title"]
                        lesson_url = attempt["lesson_url"]
                        message_text = f"New attempt detected!\nLesson Title: {lesson_title}\nLesson URL: {lesson_url}"
                        bot.send_message(chat_id, message_text)
                        print(response.text)
                time.sleep(60)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
        except requests.exceptions.Timeout as e:
            print(e)

bot.polling(none_stop=True)
