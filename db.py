"""Database functions for codres-bot"""
import os
from redis import Redis

# define constants
REDIS_HOST = os.environ.get('CODRES_DB_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('CODRES_DB_PORT', '6379'))

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
