"""Output functions for codres-bot"""
from datetime import datetime
from zoneinfo import ZoneInfo
import time
import jdatetime
import telegram

from constants import TELEGRAM_ID, TELEGRAM_KEY, DATETIME_FORMAT, TIMEZONE
from constants import CALENDAR, MESSAGE1, MESSAGE2, SERVER_DATETIME

# initialize telegram bot connection
bot = telegram.Bot(token=TELEGRAM_KEY)


def convert_datetime(dt_string):
    """Convert server datetime to correct datetime"""
    result_dt = datetime(*time.strptime(dt_string, SERVER_DATETIME)[0:6],
                         tzinfo=ZoneInfo('UTC')).astimezone(ZoneInfo(TIMEZONE))

    if CALENDAR == 'jalali':
        result = jdatetime.datetime.fromgregorian(datetime=result_dt)
        return jdatetime.datetime.strftime(result, DATETIME_FORMAT)
    return datetime.strftime(result_dt, DATETIME_FORMAT)


def send_message(event):
    """Sends message for new event and return message id"""
    text = MESSAGE1.format(
        name=event['event'],
        start=convert_datetime(event['start']),
        href=event['href']
    )
    return bot.send_message(text=text, chat_id=TELEGRAM_ID, parse_mode='HTML'
                            )['message_id']


def update_message(event, msg_id):
    """Update message for existing event"""
    text1 = MESSAGE1.format(
        name=event['event'],
        start=convert_datetime(event['start']),
        href=event['href']
    )
    text2 = MESSAGE2.format(
        name=event['event'],
        start=convert_datetime(event['start']),
        href=event['href']
    )
    bot.edit_message_text(text=text1, message_id=msg_id, chat_id=TELEGRAM_ID,
                          parse_mode='HTML')
    bot.send_message(text=text2, reply_to_message_id=msg_id,
                     chat_id=TELEGRAM_ID, parse_mode='HTML')
