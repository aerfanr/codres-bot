"""This module defines constants for Codres bot"""
import os
import sys
import yaml

URL = 'https://clist.by/api/v2/contest/'
SERVER_DATETIME = '%Y-%m-%dT%H:%M:%S'


# initialize global variables
APIKEY = ''
REDIS_HOST = ''
REDIS_PORT = ''
TELEGRAM_KEY = ''
TELEGRAM_ID = ''
DATETIME_FORMAT = ''
TIMEZONE = ''
CALENDAR = ''
MESSAGE1 = ''
MESSAGE2 = ''
RESOURCES = ''
FILTERS = {}

def read_config(path):
    """Read config from path"""
    global APIKEY
    global REDIS_HOST
    global REDIS_PORT
    global TELEGRAM_KEY
    global TELEGRAM_ID
    global DATETIME_FORMAT
    global TIMEZONE
    global CALENDAR
    global MESSAGE1
    global MESSAGE2
    global RESOURCES
    global FILTERS
    with open(path) as config_yaml:
        try:
            # Get config options
            config = yaml.safe_load(config_yaml)
            APIKEY = config.get('clist-apikey', APIKEY)
            REDIS_HOST = config.get('db-host', REDIS_HOST)
            REDIS_PORT = config.get('db-port', REDIS_PORT)
            TELEGRAM_KEY = config.get('bot-token', TELEGRAM_KEY)
            TELEGRAM_ID = config.get('channel-id', TELEGRAM_ID)
            DATETIME_FORMAT = config.get('datetime-format', DATETIME_FORMAT)
            TIMEZONE = config.get('timezone', TIMEZONE)
            CALENDAR = config.get('calendar', CALENDAR)
            MESSAGE1 = config.get('message1', MESSAGE1)
            MESSAGE2 = config.get('message2', MESSAGE2)

            # Get resource list
            if config.get('resources', False):
                resources = ''
            for resource in config.get('resources', []):
                RESOURCES += resource + ','

            # Get filter list
            FILTERS = config.get('filters', FILTERS)
        except yaml.YAMLError as exc:
            print(exc)

# Defualt config file is config.yaml in the script directory
CONFIG_FILE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                'defaults.yaml')
read_config(CONFIG_FILE_PATH)
# Change the config file if it is specified in command arguments
if len(sys.argv) > 1:
    read_config(sys.argv[1])
