# Virtualizor_Bandwidth_Notifier
Notifies to telegram if remaining traffics quota of a VPS is reaching it's limits in Virtualizor Panel

I was too lazy to make a setup script so you have to do it with JSON knowledge ;)

# What you need

## Telegram Bot
To make a telegram bot:
1. start the BotFather in telegram: https://t.me/BotFather
2. Create a bot, BotFather will send you its api_token, Save it!

## Telegram Chat ID
To find your chat id:
1. start the IDBot in telegram: https://t.me/username_to_id_bot
2. IDBot will send you your Chat ID, Save it!

## Virtualizor Info
### API Access
To gain api access of your Virtualizor account:
1. Login to your account and click on your username on the top and then click on "API Credentials"
2. On the "Create API Credentials" tab, click on "Create API Key Pair"
3. Back on "List API Credentials" tab, you can see generated "API Key" and "API Password", Save it!

### Virtualizor Panel IP
The IP address of your Virtualizor Panel IP given to you by the administrator, Usualy ends with 4083 port!

### VPS ID
Login to your Virtualizor account, on the "List VPS" menu, you can see your VPS info.
Save the "ID" of your desired VPS

# Setting up the script
Linux:
## Clone the project:
```bash
cd /
git clone https://github.com/Ashaxer/Virtualizor_Bandwidth_Notifier
cd Virtualizor_Bandwidth_Notifier
```
Windows: simply download the project as zip and extract it in a folder

## Config the JSON file:
You can optionally use online tools to edit the config file.
Linux:
```bash
nano db.json
```
Windows: use notepad or notepad++ or other text-editing tools and edit the db.json file.

Replace these variables:

(There is an example file, it will help you out:  https://github.com/Ashaxer/Virtualizor_Bandwidth_Notifier/blob/main/db_example.json)

TG_API_KEY with your telegram bot api key

CHAT_IDS with your telegram chat id (you can add more ids, just separate them with comma. E.X. "chat_ids": ["123456","987654"]

NNAME with a NickName for your prefered VPS name

V_API_KEY with your Virtualizor panel API Key

V_API_PASS with your Virtualizor panel API Pass

V_Address with your Virtualizor IP Address including the port E.X. 78.79.88.47:4083

VPS_ID with your VPS ID

W_QUOTA with desired warning quota

NT_SLEEP with desired time in seconds for script to wait if it sent you a notifications

T_SLEEP with desired time in seconds for script to wait before check again

You setup multiple Virtualizor and VPS information to the config by adding all of your server info inside the "vps_list" list!


## Install requirements
You need to have python and requests on your machine:
Linux:
```bash
apt install python3
apt install python3-pip
pip install requests
```

Windows:
Download and install latest python from https://Python.org

after installing python, open "This PC" and type "cmd" on your address bar and hit Enter

in Command Prompt window, enter following command:
```cmd
python -m pip install requests
```

# Run the script
Linux:
```bash
python3 Virtualizor.py
```
alternatively you can install Screen package on your machine and use it to check the logs and prevent closing the proccess:
```bash
apt install screen
screen -dmS VCheck sh -c 'cd /root/Virtualizor_Bandwidth_Notifier/ && /usr/bin/python3 Virtualizor.py'
```
to Enter the screen:
```bash
screen -r VCheck
```
to Detach from screen, Press Ctrl + A + D keys simultaneously.
