import threading
import json
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

with open("db.json", "r") as file: database = json.loads(file.read()); file.close()

def Notify(msg, chat_ids, api_key):
    url = f"https://api.telegram.org/bot{api_key}/sendMessage"
    for chat_id in chat_ids:
        params = {"chat_id": chat_id,
                  "text": msg}
        requests.get(url, params=params)

def Check(machine, chat_ids, api_key):
    NICKNAME=machine['MACHINE_NICKNAME']
    print(f"[{NICKNAME}] Checking...")
    params = {"act": "vps_stats",
              "svs": machine["SV_ID"],
              "api": "json",
              "apikey": machine["API_KEY"],
              "apipass": machine["API_PASS"]}
    url = f"https://{machine['HOST_IP']}/index.php"
    while True:
        try:
            response = requests.get(url, params=params, verify=False)
            response = response.json()
            print(f'[{NICKNAME}] FREE GB: {response["info"]["bandwidth"]["free_gb"]}')
            if response["info"]["bandwidth"]["free_gb"] < machine["QUOTA_WARN_GB"]:
                msg = f'{machine["MACHINE_NICKNAME"]} Traffic is reaching quota\nUsage: {response["info"]["bandwidth"]["used_gb"]}/{response["info"]["bandwidth"]["limit_gb"]}\nRemaining: {response["info"]["bandwidth"]["free_gb"]}'
                print(f'[{NICKNAME}] Sending message to telegram...')
                Notify(msg, chat_ids, api_key)
                print(f'[{NICKNAME}] Sleeping for {machine["NOTIFY_SLEEP_TIMER"]}s...')
                time.sleep(machine["NOTIFY_SLEEP_TIMER"])
            else:
                print(f'[{NICKNAME}] Sleeping for {machine["SLEEP_TIMER"]}s...')
                time.sleep(machine["SLEEP_TIMER"])
        except Exception as e:
            print("Exception happened:",e)
            print(f'[{NICKNAME}] Sleeping for {machine["SLEEP_TIMER"]}s...')
            time.sleep(machine["SLEEP_TIMER"])


if __name__=="__main__":
    for machine in database["list"]:
        threading.Thread(target=Check, args=(machine,database["chat_ids"],database["api_key"],)).start()