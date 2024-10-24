import phonenumbers
import os
from phonenumbers import geocoder, carrier, timezone
from pystyle import Colors

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_error(message):
    print(f"{Colors.red}Error: {message}{Colors.reset}")

def main():
    clear()


    try:
        while True:
            phone_number = input(f"{Colors.red}\nTelefon Nummer FX (+4550441131) : {Colors.reset}").strip()
            
            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "None"
                    operator = carrier.name_for_number(parsed_number, "fr")
                    type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"
                    timezones = timezone.time_zones_for_number(parsed_number)
                    timezone_info = timezones[0] if timezones else "None"
                    country = phonenumbers.region_code_for_number(parsed_number)
                    region = geocoder.description_for_number(parsed_number, "fr")
                    status = "Valid"
                    
                    print(f"""{Colors.red}
Phone : {phone_number}
Country Code : {country_code}
Country : {country}
Region : {region}
Timezone : {timezone_info}
Operator : {operator}
Type Number : {type_number}
{Colors.reset}""")
                    
                else:
                    print_error("Forkert Telefon Nummer! [FX: +442012345678 Eller +33623456789]")

            except Exception as e:
                print_error(f"Exception occurred: {e}")

            choice = input(f"{Colors.red}Vil du Fortsætte? (J/N): {Colors.reset}").strip().lower()
            if choice != 'j':
                break

    except Exception as e:
        print_error(f"Error: {e}")

if __name__ == "__main__":
    main()
