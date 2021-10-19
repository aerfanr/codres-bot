"""This module defines constants for Codres bot"""
import os
import yaml

# config related
CONFIG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config/')

with open(os.path.join(CONFIG_DIR, 'message1')) as file:
    MESSAGE1 = file.read()

with open(os.path.join(CONFIG_DIR, 'message2')) as file:
    MESSAGE2 = file.read()

with open(os.path.join(CONFIG_DIR, 'resources')) as file:
    resources = file.readlines()
    RESOURCES = ''
    for line in resources:
        RESOURCES += line.rstrip() + ','

FILTERS = {}
with open(os.path.join(CONFIG_DIR, 'filters')) as file:
    lines = file.readlines()
    for line in lines:
        key = line.split()[0]
        value = line[len(key) + 1:].rstrip()
        print(key, value)
        if not key in FILTERS:
            FILTERS[key] = []
        FILTERS[key].append(value)


URL = 'https://clist.by/api/v2/contest/'
SERVER_DATETIME = '%Y-%m-%dT%H:%M:%S'

CONFIG_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                'conf.yaml')

with open(CONFIG_FILE_PATH) as config_yaml:
    try:
        config = yaml.safe_load(config_yaml)
        APIKEY = config['clist-apikey']
        REDIS_HOST = config.get('db-host', 'localhost')
        REDIS_PORT = config.get('db-port', 6379)
        TELEGRAM_KEY = config['bot-token']
        TELEGRAM_ID = config['channel-id']
        DATETIME_FORMAT = config.get('datetime-format', '%Y-%m-%d %H:%M')
        TIMEZONE = config.get('timezone', 'UTC')
        CALENDAR = config.get('calendar', 'gregorian')
    except yaml.YAMLError as exc:
        print(exc)
