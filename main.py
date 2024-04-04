import requests
import telebot
import time
import logging
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
TELEGRAM_TOKEN = os.environ.get("TOKEN_TELEGRAM")
URL_DEVMAN = "https://dvmn.org/api/long_polling/"
DEVMAN_TOKEN = os.environ.get("TOKEN_DEVMAN")
HEADER_AUTHENTICATION = {
    "Authorization": f"Token {DEVMAN_TOKEN}"
}
TIMESTAMP = os.environ.get("TIMESTAMP")
PARAMS = {"timestamp": TIMESTAMP}
bot = telebot.TeleBot(TELEGRAM_TOKEN)
CHAT_USER_ID = os.environ.get("CHAT_ID")

@bot.message_handler(commands=["start"])
def start(message):
    while True:
        try:
            response = requests.get(URL_DEVMAN, params=PARAMS, headers=HEADER_AUTHENTICATION, timeout=60)
            response.raise_for_status()
            if response.ok:
                data = response.json()
                if data["status"] == "found":
                    attempts = data["new_attempts"]
                    for attempt in attempts:
                        lesson_title = attempt["lesson_title"]
                        lesson_url = attempt["lesson_url"]
                        message_text = f"New attempt detected!\nLesson Title: {lesson_title}\nLesson URL: {lesson_url}"
                        bot.send_message(CHAT_USER_ID, message_text)
                time.sleep(60)
        except requests.exceptions.RequestException as e:
            logger.error(f"Request error: {e}")
        except requests.exceptions.Timeout as e:
            logger.error(f"Request timed out: {e}")

if __name__ == "__main__":
    bot.polling(none_stop=True)
