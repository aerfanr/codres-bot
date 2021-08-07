#!/usr/bin/bash

#This script runs main.py using default config. If you want to change config,
#change this file or manualy set environment variables and run main.py

#Clist API key without 'ApiKey'
export CODRES_APIKEY=""

#Telegram API Token and Channel ID
#Channel ID could be a '@' prefixed text or a '-' prefixed number
export CODRES_TELEGRAM_KEY=""
export CODRES_TELEGRAM_ID=""

#Redis server connection details
#Defaults are 'localhost' and '6379'
# export CODRES_DB_HOST="localhost"
# export CODRES_DB_PORT="6379"

python3 main.py
