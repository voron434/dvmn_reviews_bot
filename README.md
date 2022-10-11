# Бот с уведомлениями о проверках работ на dvmn.org

Бот для уведомления меня о новых ревью на сайте [dvmn.org](https://dvmn.org/modules/)

## Установка

[Установите Python](https://www.python.org/), если этого ещё не сделали. Требуется Python 3.8. Код может запуститься на других версиях питона от 3.1 и старше, но на них не тестировался.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть 3.8

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того, установлен ли у вас Python старой второй версии. 

Скачайте код:
```sh
git clone https://github.com/voron434/dvmn_reviews_bot.git
```

Перейдите в каталог проекта:
```sh
cd dvmn_reviews_bot
```

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Определите переменные окружения. Создайте файл `.env` в каталоге `dvmn_reviews_bot/` и положите туда такой код:
```sh
DVMN_API_TOKEN=d66ef720c30ac8...23bdwd24
TELEGRAM_API_TOKEN=52...215:AAHv...FwbbCZ4
TELEGRAM_CHAT_ID=2...35
```

Данные выше приведены для примера. `DVMN_API_TOKEN` нужно заменить на токен от сайта Devman, его можно получить [на этой странице](https://dvmn.org/api/docs/). `TELEGRAM_API_TOKEN` замените на токен он чатбота в Telegram. Вот [туториал](https://spark.ru/startup/it-agenstvo-index/blog/47364/kak-poluchit-tokeni-dlya-sozdaniya-chat-bota-v-telegrame-vajbere-i-v-vkontakte), как это сделать. `TELEGRAM_CHAT_ID` замените на свой chat_id в Telegram. Его можно получить у [@userinfobot](https://telegram.me/userinfobot).


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
