# Coded / Dev: ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################

import os
import sys
import os.path
import colorama
import requests
import webbrowser
from time import sleep
from colored import fg, attr
from requests.api import options
from colorama import Fore, Back, Style, init

from utilities.Settings.common import *

colorama.init(autoreset=True)

def menu():
    print(f"""
[\x1b[95m1\x1b[95m\x1B[37m] Server Lookup
[\x1b[95m2\x1b[95m\x1B[37m] Exit
""")
menu()

option = int(input(f"[\x1b[95m>\x1b[95m\x1B[37m] Choice?: "))

def fetch_data():
        menu()
if option == 1:
        sleep(1)

        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Authorization' : input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ")
        }

        guildId = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ")

        response = requests.get(
            f"https://discord.com/api/guilds/{guildId}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        owner = requests.get(
            f"https://discord.com/api/guilds/{guildId}/members/{response['owner_id']}",
            headers = headers,
            params = {"with_counts" : True}
        ).json()

        print(f"""
{Fore.RESET}{Fore.GREEN}####### Server Infomation #######{Fore.RESET}

[{Fore.LIGHTMAGENTA_EX}Name{Fore.RESET}]      $:   {response['name']} 
[{Fore.LIGHTMAGENTA_EX}ID{Fore.RESET}]        $:   {response['id']}
[{Fore.LIGHTMAGENTA_EX}Owner{Fore.RESET}]     $:   {owner['user']['username']}#{owner['user']['discriminator']} 
[{Fore.LIGHTMAGENTA_EX}Owner ID{Fore.RESET}]  $:   {response['owner_id']}
[{Fore.LIGHTMAGENTA_EX}Members{Fore.RESET}]   $:   {response['approximate_member_count']}
[{Fore.LIGHTMAGENTA_EX}Region{Fore.RESET}]    $:   {response['region']}
[{Fore.LIGHTMAGENTA_EX}Icon URL{Fore.RESET}]  $:   https://cdn.discordapp.com/icons/{guildId}/{response['icon']}.webp?size=256
""")
        sleep(6)
        spammer()

elif option == 2:
    spammer()
if __name__ == '__main__':
        fetch_data()
