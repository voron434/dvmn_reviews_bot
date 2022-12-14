import os
import time
import logging
from contextlib import suppress
from dotenv import load_dotenv

import requests
import telegram

logger = logging.getLogger(__file__)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_API_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    bot = telegram.Bot(token=tg_token)

    class TgBotHandler(logging.Handler):

        def emit(self, record):
            log_entry = self.format(record)
            bot.send_message(chat_id=chat_id, text=log_entry)
    
    logger.setLevel(logging.INFO)
    logger.addHandler(TgBotHandler())
    logger.info('Запустил бота!')

    dvmn_token = os.getenv('DVMN_API_TOKEN')
    headers = {
        'Authorization': f'Token {dvmn_token}'
    }
    while True:
        try:
            1/0
            timestamp = None
            dvmn_api_url = 'https://dvmn.org/api/long_polling/'
            params = {}
            if timestamp:
                params['timestamp'] = timestamp
            try:
                response = requests.get(dvmn_api_url,
                                        headers=headers,
                                        timeout=90)
                response.raise_for_status()
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                time.sleep(5)
                continue
            review_answer = response.json()
            review_status = review_answer['status']
            if review_status == 'timeout':
                timestamp = review_answer['timestamp_to_request']
                continue
            elif review_status == 'found':
                timestamp = review_answer['last_attempt_timestamp']
            else:
                continue
            for attempt in review_answer['new_attempts']:
                lesson_title = attempt['lesson_title']
                message_text = f"У вас проверили работу «{lesson_title}»\n\n"
                if attempt['is_negative']:
                    message_text += "К сожалению, в работе нашлись ошибки"
                else:
                    message_text += "Преподу понравилось, можно идти дальше!"
                bot.send_message(chat_id=chat_id, text=message_text)
        except Exception as e:
            logger.exception(e)
            time.sleep(5)
