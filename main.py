#!/usr/bin/python3
"""A telegram bot for sending codeforces events to a channel"""
from datetime import datetime, timezone
import os
import time
import json
import requests
import redis

from output import send_message, update_message

URL = 'https://clist.by/api/v2/contest/'
APIKEY = os.environ.get('CODRES_APIKEY')

REDIS_HOST = os.environ.get('CODRES_DB_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('CODRES_DB_PORT', '6379'))

#read resource list
with open('./config/resources') as file:
    resources = file.readlines()
    RESOURCES = ''
    for line in resources:
        RESOURCES += line.rstrip() + ','

db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

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

def check_event(event):
    """Check message status of event and send necessery messages"""
    if not id_exists(event['id']):
        #add event and send message if event does not exist in database
        add_event(event, send_message(event))
    else:
        if event_changed(event):
            #change event and update message if event exists and is changed in
            #database
            msg_id = get_msg_id(event['id'])
            add_event(event, msg_id)
            update_message(event, msg_id)


def get_events():
    """Get list of events and checks for changes"""
    #get current time
    now = datetime.now(timezone.utc)
    current_time = now.strftime("%Y-%m-%d %H:%M")

    #get at most 5 events starting after current time
    headers = {
        'Authorization': 'ApiKey {}'.format(APIKEY)
    }
    payload = {
        'limit': 5,
        'resource': RESOURCES,
        'order_by': 'start',
        'start__gt': current_time
    }
    response = json.loads(
        requests.get(URL, headers=headers, params=payload).text
    )

    #check each event
    for event in response['objects']:
        check_event(event)

if __name__ == '__main__':
    while True:
        get_events()
        time.sleep(60)
