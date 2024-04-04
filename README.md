Этот скрипт предназначен для мониторинга новых попыток на портале dvmn.org и отправки уведомлений в Telegram о новых заданиях.
Требования

Для запуска этого скрипта необходимо установить следующие зависимости:

    requests
    telebot
    python-dotenv

Вы можете установить их, выполнив следующую команду:

bash

pip install requests telebot python-dotenv

Использование

    Установка токенов

    Вам нужно получить токены для доступа к API Devman и API Telegram. Создайте файл .env в той же директории, что и скрипт, и добавьте в него следующие строки:

    makefile

TOKEN_TELEGRAM=YOUR_TELEGRAM_TOKEN
TOKEN_DEVMAN=YOUR_DEVMAN_TOKEN
CHAT_ID=YOUR_CHAT_ID
TIMESTAMP=YOUR_TIMESTAMP

Замените YOUR_TELEGRAM_TOKEN, YOUR_DEVMAN_TOKEN, YOUR_CHAT_ID и YOUR_TIMESTAMP на соответствующие значения.

Запуск скрипта

После установки зависимостей и настройки токенов вы можете запустить скрипт, выполнив в терминале следующую команду:

bash

    python your_script_name.py

Важно

    Перед запуском убедитесь, что ваша среда выполнения имеет доступ к сети Интернет.
    Для получения TOKEN_TELEGRAM, TOKEN_DEVMAN и CHAT_ID вам нужно зарегистрироваться на Telegram и Devman.
    TIMESTAMP - это метка времени, которая используется для запросов к API Devman. Указывайте время в формате Unix Timestamp.

Дополнительная информация

    Документация Telegram Bot API
    Документация API Devman

Автор

Автор: Toreakhmet Salamat