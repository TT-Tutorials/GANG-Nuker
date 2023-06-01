<p align="center">
<img src="https://img.shields.io/github/languages/top/TT-Tutorials/GANG-Nuker?color=6d00c1&label-style=flat-square" </a>
</p>

<p align="center">
<a href="https://www.youtube.com/watch?v=QqLqglDPNCE">TOKEN GENERATOR SHOWCASE</a>

 
</p>
<p align="center">
<a href="https://github.com/TT-Tutorials/GANG-Nuker/releases/download/v1.0.0/GANG-Nuker.zip">Fast Download</a> ㅤ•ㅤ
<a href="https://discord.gg/F5eFWm2puM">Discord</a> ㅤ•ㅤ
<a href="https://www.youtube.com/watch?v=nVkysvMVk-M">Setup Tutorial Video</a>
</p>
</p>
<p align="center">
<a href="https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe">Python v3.10</a>ㅤㅤ 
<a href="https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe">Python v3.9</a>
</p>
<p align="center">
PREMIUM VERSION:
<a href="https://gangnuker.org/">WEBSITE</a>
</p>
 
---
![image](https://user-images.githubusercontent.com/94531396/171850124-c9800302-5bbc-4032-9509-a51e56228374.png)
![image](https://user-images.githubusercontent.com/94531396/171852766-688a51b4-957f-44a3-978b-c036c52a01bb.png)


<p align="center"> 
  <kbd>
<img src="https://media.discordapp.net/attachments/1105062508781387786/1113971492435267614/image.png?width=1330&height=662"></img>
  </kbd>
</p>

### Settings:
- [x] - **Windows 10 / 11**
- [x] - **Download Python:** [v3.10](https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe) **or** [v3.9](https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe)

- [x] - **100% Safe!**
- [x] - **Fequently Updating**
- [x] - **Might Have Some Bugs**
- [x] - **Python Provided**

> **WARNING:** Many people have been selling/distributing of GANG-Nuker!

> **DO NOT** Installing GANG-Nuker From Anyother Place Than This Page, Expect it be **Hacked/Scammed.**

## Installation

#### Source Code Version (More complicated but less buggy)
```sh-session
Download GANG-Nuker.zip
Extract File
Tap "Install.bat" in GANG Folder
Once All The Modules Have Been Installed GANG will Auto Launch!
Enjoy!

NOTE: When Opening GANG-Nuker Just Tap "start.bat" to Open Everytime!
NOTE: Make sure you have Python 3.9+ and Added to Path.
```

#### Compiled Version (Easier but more buggy)
```sh-session
Download: https://github.com/TT-Tutorials/GANG-Nuker/releases
Extract File
Download the latest release (GANG-Nuker.zip) and Extract The Executable
Launch Program and Enjoy!
```

---


### <a id="code-example"></a>💻〢Proxie Supoort Example:

```py
    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    proxysources = [
        ["http://spys.me/proxy.txt","%ip%:%port% "],
        ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
        ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
        ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
        ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
        ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
    ]
    threads = [] 
    for url in proxysources:
        t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp, "w") as f:
        for proxy in proxies:
            for i in range(random.randint(7, 10)):
                f.write(f"{proxy}\n")
    execution_time = (time.time() - startTime)
```
### <a id="code-example"></a>💻〢Auto Download Modules:

```py
import os 
import threading

try:
    import EXAMPLE v1
except:
    os.system("pip install EXAMPLE v1")
    import EXAMPLE v1

try:
    import EXAMPLE v2
except:
    os.system("pip install EXAMPLE v2")
    import EXAMPLE v2
```

