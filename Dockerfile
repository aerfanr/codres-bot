FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV CODRES_APIKEY=
ENV CODRES_DB_HOST=localhost
ENV CODRES_DB_PORT=6379
ENV CODRES_TELEGRAM_KEY=
ENV CODRES_TELEGRAM_ID=

CMD [ "python", "./main.py" ]
