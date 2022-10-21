# Coded / Dev / Owner: ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################


import os
import re
import sys
import time
import emoji
import ctypes
import random
import string
import shutil
import zipfile
import datetime
import colorama
import requests
import threading
import easygui, os
from os import system
import random, string
from json import loads
from time import sleep
from json import dumps
from colorama import *
import base64, pyperclip
from typing import Union
import webbrowser, base64
from colorama import Fore
import requests, threading
from tasksio import TaskPool
from tqdm import tqdm, trange
from websocket import WebSocket
from os.path import isfile, join
from discord.ext import commands
from colorama import Back, Fore, Style
from concurrent.futures import ThreadPoolExecutor
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get
try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama
try:
    import discord
except:
    os.system("pip install discord")
    import discord
from discord.ext import commands
try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui
try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client
try:
    import json
except:
    os.system('pip install json')
    import json
try:
    import base64
except:
    os.system('pip install base64')
    import base64
try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej
try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket
try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio
try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')
try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager
try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image
try:
    import discum
except:
    os.system('pip install discum')
    import discum
try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver
    
    
lock = threading.Lock()
os.system('mode 120,30')
threads = 3

ur = 'https://discord.com/api/v9/channels/messages'
#latest = 'https://discord.com/api/v10/channels/messages'
tokens = open('tokens.txt', 'r').read().splitlines()

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}
