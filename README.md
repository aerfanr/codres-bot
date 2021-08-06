# codres-bot
A telegram bot for sending Competetive Programming contest notifications to channels.

## Manual deployment
1. Deploy a redis server
2. Clone the repository
```
git clone https://github.com/aerfanr/codres-bot.git
```
3. Install python requirements
```
pip install -r requirements.txt
```
5. Modify `launch.sh` file. You may need to change `CODRES_DB_HOST` and `CODRES_DB_PORT` fields.
6. Execute `launch.sh`.
```
./launch.sh
```

## Deployment using docker-compose
1. Set up Docker and Docker Compose
2. Clone the repository
```
git clone https://github.com/aerfanr/codres-bot.git
```
or you can just download `docker-compose.yaml.example`, `env.example` and (optionally) `config/`

3. Modify `docker-compose.yaml.example` and `env.example` to your need
4. Copy files to their correct names
```
cp docker-compose.yaml.example docker-compose.yaml
cp env.example .env
```
5. Deploy the project
```
docker-compose up -d
```

You can also deploy the bot using other tools (Docker without compose, podman etc.)

## Using custom message templates
The bot sends two kinds of messages. You can edit `config/message1` and `config/message2` to change message template. Basic HTML formatting is supported.
You can use these variables in your templates:
| variable |        description        |
|:--------:|:-------------------------:|
|  {name}  |    Title of the contest   |
|  {href}  |  Link to the contest page |
|  {start} | Start time of the contest |

If you are using docker, you should mount a volume on `/usr/src/app/config` and add your templates there. For docker-compose, you can add this to `codres` service in `docker-compose.yaml`:
```
codres:
        ...
        volumes:
                - ./config:/usr/src/app/config
                ...
```

## Using proxy with docker-compose
If you need a proxy, you can add `http_proxy` and `https_proxy` to the environments section in docker-compose.
```
...
codres:
        ...
        environment:
                ...
                        - http_proxy
                        - https_proxy
                        ...
```
and add a proxy server in `.env`
```
http_proxy=http://X.X.X.X:Y
https_proxy=http://X.X.X.X:Y
```
