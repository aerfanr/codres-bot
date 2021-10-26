#!/usr/bin/python3
"""A telegram bot for sending codeforces events to a channel"""
from datetime import datetime, timezone, timedelta
from sys import stderr
import re
import time
import json
import requests

from constants import URL, APIKEY, SERVER_DATETIME, RESOURCES, FILTERS
from output import send_message, update_message
from db import id_exists, event_changed, add_event, get_msg_id

def check_event(event):
    """Check message status of event and send necessery messages"""
    #Check patterns for resource, return if nothing matched
    matched = False
    try:
        for pattern in FILTERS[event['resource']]:
            if re.fullmatch(pattern, event['event']):
                matched = True
                break
        if not matched:
            return
    except KeyError:
        print('No pattern is defined for resource {}.'
              .format(event['resource']), file=stderr)
        return

    if not id_exists(event['id']):
        # add event and send message if event does not exist in database
        print('New event: {}'.format(event['id']))
        add_event(event, send_message(event))
    else:
        if event_changed(event):
            # change event and update message if event exists and is changed in
            # database
            msg_id = get_msg_id(event['id'])
            add_event(event, msg_id)
            update_message(event, msg_id)


def get_events():
    """Get list of events and checks for changes"""
    # get current time
    now = datetime.now(timezone.utc)
    min_time = now.strftime(SERVER_DATETIME)
    max_time = (now + timedelta(weeks=1)).strftime(SERVER_DATETIME)

    # get at most 5 events starting after current time
    headers = {
        'Authorization': 'ApiKey {}'.format(APIKEY)
    }
    payload = {
        'resource': RESOURCES,
        'order_by': 'start',
        'start__gt': min_time,
        'start__lt': max_time
    }
    response = json.loads(
        requests.get(URL, headers=headers, params=payload).text
    )

    # check each event
    for event in response['objects']:
        check_event(event)


if __name__ == '__main__':
    print("Codres bot is running")
    while True:
        get_events()
        time.sleep(60)
