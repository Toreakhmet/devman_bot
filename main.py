import logging
import os
import time
import requests
import telebot
from dotenv import load_dotenv

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
TELEGRAM_USER_ID = os.environ.get("CHAT_ID")
REQUEST_COUNT = 0


def main():

    @bot.message_handler(commands=["start"])
    def start(message):
        while True:
            try:
                response = requests.get(
                    URL_DEVMAN, params=PARAMS, headers=HEADER_AUTHENTICATION, timeout=60)
                if response.ok:
                    response_json = response.json()
                    if response_json["status"] == "found":
                        attempts = response_json["new_attempts"]
                        for attempt in attempts:
                            lesson_title = attempt["lesson_title"]
                            lesson_url = attempt["lesson_url"]
                            message_text = f"New attempt detected!\nLesson Title: {lesson_title}\nLesson URL: {lesson_url}"
                            bot.send_message(TELEGRAM_USER_ID, message_text)
                else:
                    REQUEST_COUNT += 1
                    if REQUEST_COUNT == 10:
                        bot.send_message(
                            TELEGRAM_USER_ID, 'Сервер не отвечает вы может отправить повторно запрос чере час')
                        REQUEST_COUNT = 0
                        time.sleep(60*60)
            except requests.exceptions.RequestException as e:
                logger.error(f"Request error: {e}")
            except requests.exceptions.Timeout as e:
                logger.error(f"Request timed out: {e}")


if __name__ == "__main__":
    main()
