import requests
import html.parser
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import sys

if sys.argv[1] == "yt":
    if sys.argv[2] == "non_root":
        for i in (requests.get('https://raw.githubusercontent.com/revanced/revanced-patches/main/patches.json')).json():
            if i['name'] == 'theme':
                appver = ((((i['compatiblePackages'])[0])['versions'])[-1])
                break
    elif sys.argv[2] == "root":
        appver = (sys.argv[3])
    elif sys.argv[2] == "patches":
        open("youtube-patches.txt", "w").close()
        for i in (requests.get('https://raw.githubusercontent.com/revanced/revanced-patches/main/patches.json')).json():
            if (((i['compatiblePackages'])[0])['name']) == "com.google.android.youtube" and i['deprecated'] != True:
                with open("youtube-patches.txt", "a") as p:
                    p.write(str(i['name']) + " " + "on" + "\n")
        sys.exit()

    appurl = "".join(["https://www.apkmirror.com/apk/google-inc/youtube/youtube-", appver.replace(".","-"), "-release/"])

    apppage1= "".join(["https://apkmirror.com", ((((BeautifulSoup((urlopen(Request(url=appurl, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(["span"], text="APK")).parent).find(["a"], class_="accent_color")['href'])])

elif sys.argv[1] == "ytm":
    if sys.argv[2] == "non_root":
        for i in (requests.get('https://raw.githubusercontent.com/revanced/revanced-patches/main/patches.json')).json():
            if i['name'] == 'compact-header':
                appver = ((((i['compatiblePackages'])[0])['versions'])[-1])
                break
    elif sys.argv[2] == "root":
        appver = sys.argv[4]
    elif sys.argv[2] == "patches":
        open("youtubemusic-patches.txt", "w").close()
        for i in (requests.get('https://raw.githubusercontent.com/revanced/revanced-patches/main/patches.json')).json():
            if (((i['compatiblePackages'])[0])['name']) == "com.google.android.apps.youtube.music" and i['deprecated'] != True:
                with open("youtubemusic-patches.txt", "a") as p:
                    p.write(str(i['name']) + " " + "on" + "\n")
        sys.exit()

    appurl = "".join(["https://www.apkmirror.com/apk/google-inc/youtube-music/youtube-music-", appver.replace(".","-"), "-release/"])

    if sys.argv[3] == "arm64":
        apppage1 = "".join(["https://www.apkmirror.com", (((((BeautifulSoup((urlopen(Request(url=appurl, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(["div"], text="arm64-v8a")).parent).find(["a"], class_="accent_color"))['href'])])
    elif sys.argv[3] == "armeabi":
        apppage1 = "".join(["https://www.apkmirror.com", (((((BeautifulSoup((urlopen(Request(url=appurl, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(["div"], text="armeabi-v7a")).parent).find(["a"], class_="accent_color"))['href'])])


elif sys.argv[1] == "twitter":
    for a in ((BeautifulSoup((urlopen(Request(url="https://www.apkmirror.com/apk/twitter-inc/", headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find_all(["a"], class_="fontBlack", text=re.compile("^.*.release*"))):
        appver = ((a.string).split(' ')[1])
        break
    appurl = "".join(["https://www.apkmirror.com/apk/twitter-inc/twitter/twitter-", appver.replace(".","-"), "-release/"])

    apppage1= "".join(["https://apkmirror.com", ((((BeautifulSoup((urlopen(Request(url=appurl, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(["span"], text="APK")).parent).find(["a"], class_="accent_color")['href'])])

elif sys.argv[1] == "reddit":
    for a in ((BeautifulSoup((urlopen(Request(url="https://www.apkmirror.com/apk/redditinc/", headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find_all(["a"], class_="fontBlack")): 
        appver = ((a.string).split(' ')[1])
        break
    appurl = "".join(["https://www.apkmirror.com/apk/reddditinc/reddit/reddit-", appver.replace(".","-"), "-release/"])

    apppage1= "".join(["https://apkmirror.com", ((((BeautifulSoup((urlopen(Request(url=appurl, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(["span"], text="APK")).parent).find(["a"], class_="accent_color")['href'])])
elif sys.argv[1] == "tiktok":
    for a in ((BeautifulSoup((urlopen(Request(url="https://www.apkmirror.com/apk/tiktok-pte-ltd/tik-tok/",headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find_all(["a"], class_="fontBlack")):
        appver = ((a.string).split(' ')[1])
        break

    appurl = "".join(["https://www.apkmirror.com/apk/tiktok-pte-ltd/tik-tok/tik-tok-", appver.replace(".","-"), "-release/"])

    apppage1= "".join(["https://apkmirror.com", ((((BeautifulSoup((urlopen(Request(url=appurl, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(["span"], text="APK")).parent).find(["a"], class_="accent_color")['href'])])

apppage2= "".join(["https://apkmirror.com", ((BeautifulSoup((urlopen(Request(url=apppage1, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(["a"], { 'class' : re.compile("accent_bg btn btn-flat downloadButton")})['href'])])

appdllink = "".join(["https://apkmirror.com", (((BeautifulSoup((urlopen(Request(url=apppage2, headers={'User-Agent': 'Mozilla/5.0'})).read()), 'html.parser')).find(rel="nofollow"))['href'])])

with open("latest-app.txt", "w") as f:
        f.write('\n'.join([appver, appdllink]))

