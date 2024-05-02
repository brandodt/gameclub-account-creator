import subprocess
import requests
import warnings
import random
import string
import os
from colorama import init, Fore

init(autoreset=True)
warnings.filterwarnings("ignore", category=requests.packages.urllib3.exceptions.InsecureRequestWarning)

title = '''
 ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ . ▄▄· ▄▄▌  ▄• ▄▌▄▄▄▄·                                
▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·▐█ ▌▪██•  █▪██▌▐█ ▀█▪                               
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄██ ▄▄██▪  █▌▐█▌▐█▀▀█▄                               
▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌▐███▌▐█▌▐▌▐█▄█▌██▄▪▐█                               
·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀ ·▀▀▀ .▀▀▀  ▀▀▀ ·▀▀▀▀                                
 ▄▄▄·  ▄▄·  ▄▄·       ▄• ▄▌ ▐ ▄ ▄▄▄▄▄     ▄▄· ▄▄▄  ▄▄▄ . ▄▄▄· ▄▄▄▄▄      ▄▄▄  
▐█ ▀█ ▐█ ▌▪▐█ ▌▪▪     █▪██▌•█▌▐█•██      ▐█ ▌▪▀▄ █·▀▄.▀·▐█ ▀█ •██  ▪     ▀▄ █·
▄█▀▀█ ██ ▄▄██ ▄▄ ▄█▀▄ █▌▐█▌▐█▐▐▌ ▐█.▪    ██ ▄▄▐▀▀▄ ▐▀▀▪▄▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█ ▪▐▌▐███▌▐███▌▐█▌.▐▌▐█▄█▌██▐█▌ ▐█▌·    ▐███▌▐█•█▌▐█▄▄▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
 ▀  ▀ ·▀▀▀ ·▀▀▀  ▀█▄▀▪ ▀▀▀ ▀▀ █▪ ▀▀▀     ·▀▀▀ .▀  ▀ ▀▀▀  ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀
by: dwaynelifter (Discord: 0x13371)         
'''

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}{title}{Fore.RESET}")

def generate_random_string(length=8):
    """Generate a random string of letters and digits."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def install_dependencies():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
        clear()
        print(f"{Fore.GREEN}Status: Dependencies installed successfully.{Fore.RESET}")
    except subprocess.CalledProcessError:
        clear()
        print(f"{Fore.YELLOW}Status: Failed to install dependencies. Please install them manually using 'pip install -r requirements.txt'.{Fore.RESET}")


def register_account(username, password, filename=None):
    url = "https://www.gameclub.ph/Join/MemberJoin"

    payload = {
        'user_id': username,
        'user_pw': password,
        'email': f'{generate_random_string()}@yahoo.com',
        'first_name': 'aleksandr',
        'last_name': 'kuznetsov',
        'birthday': '2000/01/01',
        'question': '1', #What is your mothers maiden name
        'txtQuestion': '',
        'answer': 'alekspogi',
        'siteCode': 'LB'
    }

    headers = {
        'Cookie': 'ASP.NET_SessionId=obbnv0firqyugzozexyisofv'
    }

    response = requests.post(url, headers=headers, data=payload, verify=False)

    if response.status_code == 200:
        data = response.json()
        if data.get('code', -1) == 0:
            if filename:
                with open(filename, 'a') as file:
                    file.write(f"{username}:{password}\n")
            return "success"
        elif data.get('code', -1) == -15:
            return "already taken"
        else:
            return "failed"
    else:
        return "failed"

def register_multiple_accounts(base_username, password, num_accounts):
    filename = f"{base_username}_accounts.txt"
    success_count = 0
    failed_count = 0
    failed_usernames = []
    
    clear()

    for i in range(num_accounts):
        username = f"{base_username}{i}"
        result = register_account(username, password, filename)

        if result == "success":
            success_count += 1
        else:
            failed_count += 1
            failed_usernames.append(username)
        clear()
        print(f"Loading... [{i+1}/{num_accounts}]")
            

    if filename:
        clear()
        print(f"Saved on {filename}")
        print(f"{Fore.GREEN}Success: {success_count}{Fore.RESET}")
        print(f"{Fore.YELLOW}Already Registered: {failed_count}{Fore.RESET}")
    
if __name__ == "__main__":
    install_dependencies()
    print("Choose an option:")
    print("1. Single Account")
    print("2. Multiple Accounts")

    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        clear()
        print("Single Account")
        username = input("Enter your desired username: ")
        password = input("Enter your desired password: ")
        result = register_account(username, password)
        if result == "success":
            clear()
            print(f"{Fore.GREEN}Account '{username}:{password}' successfully registered!{Fore.RESET}")
        elif result == "already taken":
            clear()
            print(f"{Fore.YELLOW}Username '{username}' is already taken. Please choose another one.{Fore.RESET}")
        else:
            clear()
            print(f"{Fore.YELLOW}Registration failed. Check the response content for more details.{Fore.RESET}")
    elif choice == '2':
        clear()
        print("Multiple Account")
        base_username = input("Enter username: ")
        password = input("Enter the password: ")
        num_accounts = int(input("Enter the number of accounts to create: "))
        register_multiple_accounts(base_username, password, num_accounts)
    else:
        print(f"{Fore.YELLOW}Invalid choice. Please enter '1' or '2'.{Fore.RESET}")
