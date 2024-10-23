import requests
from colorama import Fore, Style, init


init()

def print_ascii_art():
    ascii_art = f"""
{Fore.RED}  _____ _____    _      ____   ____  _  ___    _ _____  
 |_   _|  __ \  | |    / __ \ / __ \| |/ / |  | |  __ \ 
   | | | |__) | | |   | |  | | |  | | ' /| |  | | |__) |
   | | |  ___/  | |   | |  | | |  | |  < | |  | |  ___/ 
  _| |_| |      | |___| |__| | |__| | . \| |__| | |     
 |_____|_|      |______\____/ \____/|_|\_\\____/|_|     
{Style.RESET_ALL}
    """
    print(ascii_art)

def ip_lookup(ip_address):
    """Forespørger IP-adresseoplysninger fra ipinfo.io API."""
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Unable to fetch data"}
    except requests.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Print ASCII-tegning ved scriptstart
    print_ascii_art()
    
    ip_address = input(f"{Fore.RED}Indtast IP-adresse: {Style.RESET_ALL}")
    result = ip_lookup(ip_address)
    
    if "error" in result:
        print(f"{Fore.RED}{result['error']}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Resultater:{Style.RESET_ALL}")
        print(f"{Fore.RED}IP-adresse: {result.get('ip', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.RED}Værtsnavn: {result.get('hostname', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.RED}By: {result.get('city', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.RED}Region: {result.get('region', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.RED}Land: {result.get('country', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.RED}Postnummer: {result.get('postal', 'N/A')}{Style.RESET_ALL}")
        loc = result.get('loc', 'N/A').split(',') if result.get('loc') else ['N/A', 'N/A']
        print(f"{Fore.RED}Breddegrad: {loc[0]}{Style.RESET_ALL}")
        print(f"{Fore.RED}Længdegrad: {loc[1]}{Style.RESET_ALL}")
        print(f"{Fore.RED}Organisation: {result.get('org', 'N/A')}{Style.RESET_ALL}")
    
    input(f"{Fore.RED}Tryk på Enter for at afslutte...{Style.RESET_ALL}")
