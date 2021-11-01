# codres-bot
A telegram bot for sending Competetive Programming contest notifications to channels.

## Deployment
1. Deploy a redis server
2. Clone the repository
```
git clone https://github.com/aerfanr/codres-bot.git
```
3. Install python requirements
```
pip install -r requirements.txt
```
5. Modify `conf.yaml` file. You should specify `clist-apikey`, `bot-token` and `channel-id`. You may also want to change other variables. You can move the file and change the path at runtime.
6. Execute `launch.sh`. You may need to change the default config path if it is not `conf.yaml`.
```
./launch.sh path/to/conf.yaml
```

## Configuration
You can change configuration options by editing the config file. There are comments describing config options in `conf.yaml`.

### Message templates
The bot sends two kinds of messages. Basic HTML formatting is supported.
You can use these variables in your templates:
| variable |        description        |
|:--------:|:-------------------------:|
|  {name}  |    Title of the contest   |
|  {href}  |  Link to the contest page |
|  {start} | Start time of the contest |

### Changing resources
You can add resources to `resources` config option. Each resource in a single line. Here is a list of available resources: https://clist.by/resources/