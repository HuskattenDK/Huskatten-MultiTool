import threading
import random
import string
import time
import requests
from colorama import Fore, Style, init

init()

def print_banner():
    banner = f"""{Fore.RED}
  _   _ _ _                _____                           _              
 | \ | (_) |              / ____|                         | |            
 |  \| |_| |_ _ __ ___   | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | . ` | | __| '__/ _ \  | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |\  | | |_| | | (_) | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_| \_|_|\__|_|  \___/   \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                        
{Style.RESET_ALL}"""
    print(banner)

def generate_and_validate_code(webhook_url):
    while True:
        # Genererer en tilfældig længde mellem 8 og 16
        length = random.randint(8, 16)
        # Genererer en tilfældig streng med den valgte længde
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        full_code = f'discord.gift/{code}'

        # Tjekker koden mod Discords API (Simuleret kald)
        try:
            # Dette er et simuleret API-kald, og den faktiske URL skal bruges med omhu.
            response = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true')
            
            if response.status_code == 200:
                print(f'{Fore.GREEN}{full_code} - Valid{Style.RESET_ALL}')
                
                # Sender en besked til Discord-webhooken
                if webhook_url:
                    data = {
                        "content": f'Valid Discord gift code found: {full_code}'
                    }
                    webhook_response = requests.post(webhook_url, json=data)
                    
                    if webhook_response.status_code == 204:
                        print(f'{Fore.CYAN}Successfully sent to webhook{Style.RESET_ALL}')
                    else:
                        print(f'{Fore.YELLOW}Failed to send to webhook: {webhook_response.status_code}{Style.RESET_ALL}')
            else:
                print(f'{Fore.RED}{full_code} - Invalid{Style.RESET_ALL}')  # Rød tekst for invalid
        except requests.RequestException as e:
            print(f'{Fore.YELLOW}{full_code} - Error checking code{Style.RESET_ALL}')
            print(e)

        # Simulerer en ventetid for ikke at overbelaste serveren
        time.sleep(0.1)

def start_threads(thread_count, webhook_url):
    threads = []
    for _ in range(thread_count):
        # Opretter og starter en ny tråd
        thread = threading.Thread(target=generate_and_validate_code, args=(webhook_url,))
        threads.append(thread)
        thread.start()

    # Venter på, at alle tråde er færdige (dette sker aldrig i denne kode, da trådene kører uendeligt)
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    # Print banner ved opstart
    print_banner()
    try:
        # Indtager Discord webhook-URL fra brugeren
        webhook_url = input(f'{Fore.RED}Indtast Discord webhook URL: {Style.RESET_ALL}')
        
        # Indtager antallet af tråde fra brugeren
        thread_count = int(input(f'{Fore.RED}Indtast antallet af threads: {Style.RESET_ALL}'))
        start_threads(thread_count, webhook_url)
    except ValueError:
        print('Indtast venligst et gyldigt tal for antallet af threads.')
