import os
from contextlib import suppress
from dotenv import load_dotenv

import requests
import telegram


def long_pool_dvmn_api(token, timestamp=None):
    """Long pool dvmn.org reviews API

    This function tries to get a review on the dvmn.org
    website via LongPoll API. This means response takes 90 seconds
    by default, but may take less in case if review is done during pending response.

    Args:
        token (str): API Token for dvmn.org
        timestamp (int, optional): Timestamp of last request to API
    
    Returns:
        review_answer (dict): Full decoded response from API
    """
    dvmn_api_url = 'https://dvmn.org/api/long_polling/'
    params = {}
    if timestamp:
        params['timestamp'] = timestamp
    response = requests.get(dvmn_api_url,
                            headers=headers,
                            timeout=90)
    response.raise_for_status()
    review_answer = response.json()
    return review_answer


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('TELEGRAM_API_TOKEN')
    bot = telegram.Bot(token=tg_token)
    chat_id = os.getenv('TELEGRAM_CHAT_ID')

    dvmn_token = os.getenv('DVMN_API_TOKEN')
    headers = {
        'Authorization': f'Token {dvmn_token}'
    }

    while True:
        with suppress(requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            timestamp = None
            review_answer = long_pool_dvmn_api(dvmn_token, timestamp)
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
