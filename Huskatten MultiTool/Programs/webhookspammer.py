import requests
import threading
import time
from colorama import Fore, Style, init

init()

def print_banner():
    banner = f"""{Fore.RED}
 __          __  _     _                 _       _____                                           
 \ \        / / | |   | |               | |     / ____|                                          
  \ \  /\  / /__| |__ | |__   ___   ___ | | __ | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
   \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
    \  /\  /  __/ |_) | | | | (_) | (_) |   <   ____) | |_) | (_| | | | | | | | | | | |  __/ |   
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                      | |                                        
                                                      |_|
{Style.RESET_ALL}"""
    print(banner)

def send_webhook(webhook_url, message, interval):
    while True:
        try:
            response = requests.post(webhook_url, json={"content": message})
            print(f"Skrev: {message}")
            time.sleep(interval)
        except Exception as e:
            print(f"Fejl: {e}")

def webhook_spammer():
    webhook_url = input(f"{Fore.RED}Indtast webhook URL: {Style.RESET_ALL}")
    message = input(f"{Fore.RED}Indtast besked: {Style.RESET_ALL}")
    interval = float(input(f"{Fore.RED}Skriv hvor mange sekunder der skal være imellem hver besked: {Style.RESET_ALL}"))

    
    thread = threading.Thread(target=send_webhook, args=(webhook_url, message, interval))
    thread.start()

    print("Startet luk den for at stoppe")

if __name__ == "__main__":
    print_banner()
    webhook_spammer()
