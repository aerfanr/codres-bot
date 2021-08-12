"""Database functions for codres-bot"""
from redis import Redis

from constants import REDIS_HOST, REDIS_PORT

# initialize database connection
db = Redis(host=REDIS_HOST, port=REDIS_PORT)


def id_exists(event_id):
    """Return true if an event with id exists"""
    return db.exists(event_id)


def event_changed(event):
    """Return true if event is changed"""
    event_name = db.hget(event['id'], 'name')
    event_start = db.hget(event['id'], 'start')
    event_href = db.hget(event['id'], 'href')

    result = False
    if event['event'] == event_name:
        result = True
    if event['start'] == event_start:
        result = True
    if event['href'] == event_href:
        result = True

    return result


def add_event(event, msg_id):
    """Add event to database"""
    db.hset(event['id'], 'msg_id', msg_id, {
        'name': event['event'],
        'start': event['start'],
        'href': event['href']
    })


def get_msg_id(event_id):
    """Return message id for event"""
    return db.hget(event_id, 'msg_id')
