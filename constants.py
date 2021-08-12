"""This module defines constants for Codres bot"""
import os

# Clist related
URL = 'https://clist.by/api/v2/contest/'
APIKEY = os.environ.get('CODRES_APIKEY')
SERVER_DATETIME = '%Y-%m-%dT%H:%M:%S'

# databse related
REDIS_HOST = os.environ.get('CODRES_DB_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('CODRES_DB_PORT', '6379'))

# telegram related
TELEGRAM_KEY = os.environ.get('CODRES_TELEGRAM_KEY', '')
TELEGRAM_ID = os.environ.get('CODRES_TELEGRAM_ID')

# datetime related
DATETIME_FORMAT = os.environ.get('CODRES_DATETIME_FORMAT', '%Y-%m-%d %H:%M')
TIMEZONE = os.environ.get('CODRES_TIMEZONE', 'UTC')
CALENDAR = os.environ.get('CODRES_CALENDAR', 'gregorian')

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
