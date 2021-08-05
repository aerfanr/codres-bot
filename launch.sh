#!/usr/bin/bash

#This script runs main.py using default config. If you want to change config,
#change this file or manualy set environment variables and run main.py

export CODRES_APIKEY="" #Change this
export CODRES_DB_HOST="localhost"
export CODRES_DB_PORT="6379"
export CODRES_TELEGRAM_KEY="" #Change this
export CODRES_TELEGRAM_ID="" #Change this

python3 main.py
