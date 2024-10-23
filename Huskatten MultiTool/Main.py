import subprocess
import sys
import os
from colorama import Fore, Style, init

# Initialiser colorama
init(autoreset=True)

def print_banner():
    banner =f"""{Fore.RED}
  _    _           _         _   _               __  __       _ _   _ _______          _ 
 | |  | |         | |       | | | |             |  \/  |     | | | (_)__   __|        | |
 | |__| |_   _ ___| | ____ _| |_| |_ ___ _ __   | \  / |_   _| | |_ _   | | ___   ___ | |
 |  __  | | | / __| |/ / _` | __| __/ _ \ '_ \  | |\/| | | | | | __| |  | |/ _ \ / _ \| |
 | |  | | |_| \__ \   < (_| | |_| ||  __/ | | | | |  | | |_| | | |_| |  | | (_) | (_) | |
 |_|  |_|\__,_|___/_|\_\__,_|\__|\__\___|_| |_| |_|  |_|\__,_|_|\__|_|  |_|\___/ \___/|_|
                                                                                         
                                                                                         
{Style.RESET_ALL}"""
    print(banner)

def print_menu():
    print(f"""
{Fore.RED}[1] Bot Nuker       [6] Token Login
[2] IP Lookup       [7] Search User
[3] Nitrogen        [8] Server Info
[4] WebhookSpammer  [9] Token Decrypt
[5] Ip Pinger       [10] Nummer Info

Made By Huskatten V1.0
{Style.RESET_ALL}
    """)

def main():
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    
    programs_dir = os.path.join(base_dir, 'Programs')
    
    
    print_menu()
    choice = input(f"{Fore.RED}Vælg en option: {Style.RESET_ALL}")

    if choice == '1':
        script_path = os.path.join(programs_dir, 'DiscordNuker.py')
    elif choice == '2':
        script_path = os.path.join(programs_dir, 'iplookup.py')
    elif choice == '3':
        script_path = os.path.join(programs_dir, 'nitrogen.py')
    elif choice == '4':
        script_path = os.path.join(programs_dir, 'webhookspammer.py')
    elif choice == '5':
        script_path = os.path.join(programs_dir, 'ippinger.py')
    elif choice == '6':
        script_path = os.path.join(programs_dir, 'tokenlogin.py')
    elif choice == '7':
        script_path = os.path.join(programs_dir, 'searchuser.py')
    elif choice == '8':
        script_path = os.path.join(programs_dir, 'serverinfo.py')
    elif choice == '9':
        script_path = os.path.join(programs_dir, 'tokendecrypt.py')
    elif choice == '10':
        script_path = os.path.join(programs_dir, 'NummerInfo.py')
    else:
        print(f"{Fore.RED}Ugyldigt valg. Vælg venligst 1 eller 2.{Style.RESET_ALL}")
        return

    try:
        subprocess.run([sys.executable, script_path], check=True)
    except Exception as e:
        print(f"{Fore.RED}Fejl ved kørsel af scriptet: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_banner()
    main()
