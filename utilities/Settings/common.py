# Coded / Dev / Owner: ††#1792 | https://github.com/TT-Tutorials | https://gangnuker.org
# GANG Discord Nuker / Multi Tool ©
# Copyright © 2023
######################################## 

import os
import re
import io
import sys
import time
import json
import shutil
import ctypes
import random
import zipfile
import requests
import threading
import subprocess
import pylibcheck
from pystyle import *
from time import sleep
from colorama import Fore
from bs4 import BeautifulSoup
from distutils.version import LooseVersion
from urllib.request import urlopen, urlretrieve
from multiprocessing.spawn import spawn_main
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil

##########################################

THIS_VERSION = "2.5.1"

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
# r = Fore.RESET

google_target_ver = 0
edge_target_ver = 0

counttokens = len(open('tokens.txt').readlines())
os.system("title PRESS ENTER")

def GANGLIST():
  os.system('cls' if os.name=='nt' else 'clear')
  global yeslist
  yeslist = ["yes", "y", "yer", "yeah","yessir","ye","okay","yep","yea","ok","k","yh","sure"]

########################################

class Chrome_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://chromedriver.storage.googleapis.com/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if google_target_ver:
            self.target_version = google_target_ver

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "chromedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_chromedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open(self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect

    def get_release_version_number(self):
        path = (
            "LATEST_RELEASE"
            if not self.target_version
            else f"LATEST_RELEASE_{self.target_version}"
        )
        return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())

    def fetch_chromedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract(self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Edge_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://msedgedriver.azureedge.net/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if edge_target_ver:
            self.target_version = edge_target_ver

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "edgedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_edgedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open("ms"+self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect


    def get_release_version_number(self):
        path = (
            "LATEST_STABLE"
            if not self.target_version
            else f"LATEST_RELEASE_{str(self.target_version).split('.', 1)[0]}"
        )
        urlretrieve(
            f"{self.__class__.DL_BASE}{path}",
            filename=f"{getTempDir()}\\{path}",
        )
        with open(f"{getTempDir()}\\{path}", "r+") as f:
            _file = f.read().strip("\n")
            content = ""
            for char in [x for x in _file]:
                for num in ("0","1","2","3","4","5","6","7","8","9","."):
                    if char == num:
                        content += char
        return LooseVersion(content)

    def fetch_edgedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract("ms"+self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Opera_Installer(object):
    DL_BASE = "https://github.com"
    def __init__(self, *args, **kwargs):
        self.platform = sys.platform
        self.links = ""

        r = requests.get(self.__class__.DL_BASE+"/operasoftware/operachromiumdriver/releases")
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            if "operadriver" in link.get('href'):
                self.links += f"{link.get('href')}\n"

        for i in self.links.split("\n")[:4]:
            if self.platform in i:
                self.fetch_edgedriver(i)

    def fetch_edgedriver(self, driver):
        executable = "operadriver.exe"
        driver_name = driver.split("/")[-1]
        cwd = os.getcwd() + os.sep

        urlretrieve(self.__class__.DL_BASE+driver, filename=driver_name)
        with zipfile.ZipFile(driver_name) as zf:
            zf.extractall()
        shutil.move(cwd+driver_name[:-4]+os.sep+executable, cwd+executable)
        os.remove(driver_name)
        shutil.rmtree(driver_name[:-4])

def getDriver():
    drivers = ["chromedriver.exe", "msedgedriver.exe", "operadriver.exe"]
    Write.Print("\nChecking Downloaded Drivers!", Colors.purple_to_blue, interval=0.015)
    sleep(0.5)
    for driver in drivers:
        if os.path.exists(os.getcwd() + os.sep + driver):
            Write.Print("\nChromeDriver is Already Installed...", Colors.purple_to_blue, interval=0.015)
            sleep(0.5)
            return driver
    else:
        Write.Print("\nInstalling Drivers!\n\n", Colors.purple_to_blue, interval=0.015)
        if os.path.exists(os.getenv('localappdata') + '\\Google'):
            Chrome_Installer()
            Write.Print("\nChromeDriver.exe Has Been Installed Successfully!", Colors.purple_to_blue, interval=0.015)
            return "chromedriver.exe"
        elif os.path.exists(os.getenv('appdata') + '\\Opera Software\\Opera Stable'):
            Opera_Installer()
            Write.Print("\nOperaDriver.exe Has Been Installed Successfully!\n\n", Colors.purple_to_blue, interval=0.015)
            return "operadriver.exe"
        elif os.path.exists(os.getenv('localappdata') + '\\Microsoft\\Edge'):
            Edge_Installer()
            Write.Print("\nMsedgeDriver.exe Has Been Installed Successfully!\n\n", Colors.purple_to_blue, interval=0.015)
            return "msedgedriver.exe"
        else:
            Write.Print("\nERROR | No Compatible Driver Found... Proceeding with ChromeDriver!\n\n", Colors.purple_to_blue, interval=0.015)
            Chrome_Installer()
            Write.Print("\nTrying ChromeDriver.exe\n\n", Colors.purple_to_blue, interval=0.015)
            return "chromedriver.exe"

#######################  Driver Downloads / AutoLogin  #########################
################################################################################

def filegrabbertitle():
    print(f"")

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def transition():
    clear()
    Spinner()
    clear()

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def SlowPrint(_str):
    for letter in _str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'

def validateToken(token):
    '''validate the token by contacting the discord api'''
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform this action."

    r = requests.get(base_url, headers=getheaders(token))
    if r.status_code != 200:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    j = requests.get(f'{base_url}/billing/subscriptions', headers=getheaders(token)).json()
    try:
        if j["message"] == message:
            print(f"\n{Fore.RED}Phone Locked Token!{Fore.RESET}")
            sleep(1)
            __import__("spammer").main()
    except (KeyError, TypeError, IndexError):
        pass

def validateWebhook(hook):
    if not "api/webhooks" in hook:
        print(f"\n{Fore.RED}Invalid Webhook!{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    try:
        responce = requests.get(hook)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        print(f"\n{Fore.RED}Invalid Webhook!{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    try:
        j = responce.json()["name"]
    except (KeyError, json.decoder.JSONDecodeError):
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        sleep(1)
        __import__("spammer").main()
    print(f"{Fore.GREEN}Valid webhook! ({j})")

def installPackage(dependencies):
    print(f'{Fore.CYAN}Checking Packages...{Fore.RESET}')
    if sys.argv[0].endswith('.exe'):
            reqs = subprocess.check_output(['python', '-m', 'pip', 'freeze'])
            installed_packages = [r.decode().split('==')[0].lower() for r in reqs.split()]

            for lib in dependencies:
                if lib not in installed_packages:
                    print(f"{w}{lib}{Fore.RED} NOT FOUND! Installing it for you...{Fore.RESET}")
                    try:
                        subprocess.check_call(['python', '-m', 'pip', 'install', lib])
                    except Exception as e:
                        print(f"{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : {e}")
                        sleep(0.5)
                        pass
    else:
        for i in dependencies:
            if not pylibcheck.checkPackage(i):
                print(f"{w}{i}{Fore.RED} NOT FOUND! Installing it for you...{Fore.RESET}")
                pylibcheck.installPackage(i)

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    Write.Print(f"\r                                       {prefix} |{bar}| {percent}% {suffix}", Colors.purple_to_blue, interval=0.000)
    if iteration == total:
        print()

items = list(range(0, 37))
l = len(items)

def proxy_scrape(): 
    startTime = time.time()
    temp = getTempDir()+"\\gang_proxies"                               
#    Write.Print("\n\n\n\n\n\n\n\n\n\n                                          Collecting Proxies | Please Wait... \n", Colors.purple_to_blue, interval=0.010)


    execution_time = (time.time() - startTime)
#    Write.Print(f"                                                        Opening Menu", Colors.purple_to_blue, interval=0.000)

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}GANG-Nuker FREE    |    Made by ††#1792    |    Tokens: [{counttokens}]")
    elif system == 'posix':
        sys.stdout.write(f"{_str}GANG-Nuker FREE    |    Made by ††#1792    |    Tokens: [{counttokens}]")
    else:
        pass

def proxy():
    temp = getTempDir()+"\\gang_proxies"
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[0]

    with open(temp, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
    return ({'http://': f'http://{proxy}', 'https://': f'https://{proxy}'})

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

gang = r'''

  /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
 /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$
| $$  \__/| $$  \ $$| $$$$| $$| $$  \__/
| $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$
| $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$
| $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$
|  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/
 \______/ |__/  |__/|__/  \__/ \______/


        Github.com/TT-Tutorials
'''
System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(gang), Colors.purple_to_blue, Colorate.Vertical, interval=0.030, enter=True)
