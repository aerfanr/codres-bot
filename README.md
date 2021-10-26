# codres-bot
A telegram bot for sending Competetive Programming contest notifications to channels.

## TODO for next release:
- [x] Regex filtering support

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
5. Modify `conf.yaml` file. You should change specify `clist-apikey`, `bot-token` and `channel-id`. You may also want to change other variables. Or you can create a config file at a different path.
6. Execute `launch.sh`. You may need to change the default config path if it is not `conf.yaml`.
```
./launch.sh [path/to/config.yaml]
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

## Configuration
Default config file is `conf.yaml` in the script directory. You can also specify a config file as a command line argument.
### List of config options
|  variable name  |   default value  |                    description                    |
|:---------------:|:----------------:|:-------------------------------------------------:|
|   clist-apikey  |                  |                   Clist API Key                   |
|     db-host     |    "localhost"   |              Redis database hostname              |
|     db-port     |       6379       |                Redis database port                |
|    bot-token    |                  |               Telegram bot API token              |
|    channel-id   |                  |   Telegram channel ID (prefixed with '@' or '-')  |
| datetime-format | "%Y-%m-%d %H:%M" |            Date and time output format            |
|     timezone    |       "UTC"      |      Output timezone, example: 'Asia/Tehran'      |
|     calendar    |    "gregorian"   | Calendar to use, options: ['gregorian', 'jalali'] |
### Changing other config files
If you are using docker, you should mount a volume on `/usr/src/app/config` and add your templates there. For docker-compose, you can add this to `codres` service in `docker-compose.yaml`:
```
codres:
        ...
        volumes:
                - ./config:/usr/src/app/config
                ...
```

### Message templates
The bot sends two kinds of messages. You can edit `config/message1` and `config/message2` to change message template. Basic HTML formatting is supported.
You can use these variables in your templates:
| variable |        description        |
|:--------:|:-------------------------:|
|  {name}  |    Title of the contest   |
|  {href}  |  Link to the contest page |
|  {start} | Start time of the contest |

### Changing resources
You can add resources to `config/resources` file. Each resource in a single line. Here is a list of available resources: https://clist.by/resources/

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
