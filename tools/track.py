#!/bin/python
# Coded By TripleHat
# Github https://github.com/TripleHat
# Instagram https://instagram.com/wh0ami_1
# Instagram https://instagram.com/triple_hat3
#╺┳╸┏━┓╻┏━┓╻  ┏━╸╻ ╻┏━┓╺┳╸
# ┃ ┣┳┛┃┣━┛┃  ┣╸ ┣━┫┣━┫ ┃
# ╹ ╹┗╸╹╹  ┗━╸┗━╸╹ ╹╹ ╹ ╹

import os
import sys
import time
import requests
import random
import string
import json
import argparse

red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
close = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

reqError = [320, 400, 401, 404, 422, 500, 501, 502, 503, 504]
reqsuccess = [200, 201, 202, 203]
api_key="9af5ff383bff499f91a052e074284663"
bg_key="ititzKSaRNcWmAvuEVdJ4A3R"
dist = [ 'AIX', 'Alpine', 'AlterLinux', 'Anarchy', 'Android', 'Antergos', 'antiX', 'Apricity', 'ArcoLinux', 'ARCHlabs', 'ArchStrike', 'XFerience', 'ArchMerge', 'Arch', 'Artix', 'BlackArch', 'CentOS', 'windows10', 'Windows7', 'chrom', 'kali', 'Debian', 'Ubuntu',]
web = [
        'https://www.facebook.com/',
        'https://www.twitter.com/',
        'https://www.instagram.com/',
        'https://www.tiktok.com/@',
        'https://www.linkedin.com/in/',
        'https://www.github.com/',
        'https://www.reddit.com/u/',
        'https://www.pinterest.com/',
        'https://www.vsco.co/',
        'https://www.soundcloud.com/',
        'https://www.snapchat.com/add/',
        'https://www.quora.com/profile/',
        'https://www.flickr.com/people/',
        'https://www.linktr.ee/',
        'https://ask.fm/',
]
useragent = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)',
    'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36',
    'Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; ja) Opera 11.00',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24',
    'Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11',
    'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5',
    'Mozilla/5.0 (X11; FreeBSD amd64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.56 Safari/1EA69',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10',
    'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)',
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
    'Mozilla/5.0 (X11; CrOS i686 1660.57.0) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.46 Safari/535.19',
    'Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01',
    'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)',
    'Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
    'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)',
    'Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51',
]

def banner():
   os.system("neofetch --logo --ascii_distro "+ random.choice(dist))

def track_ip():
   try:
      banner()
      ip=input(green+"inter ip: "+cyan)

      response = "https://api.ipgeolocation.io/ipgeo?apiKey={}&ip={}&fields=geo&include=useragent".format(str(api_key), ip)

      re=requests.get(response, headers={'User-Agent': random.choice(useragent)}).json()

      print(green+"Target Ip: ", cyan+re["ip"])
      print(green+"Country Code: ", cyan+re["country_code2"])
      print(green+"Country Name: ", cyan+re["country_name"])
      print(green+"Region Name: ", cyan+re["city"])
      print(green+"District Name: ", cyan+re["district"]+close)
   except:
         print(red+"\nError Occured, Maybe no Internet Connection\n")
         exit()

def me_info():

   dev = os.system("neofetch --ascii_distro "+ random.choice(dist))
   print("\n")
   try:
      req=requests.get("https://ifconfig.me").text
      print(green+"Your public ip: ", cyan+req,)
   except:
         print(red+"Cant show public Ip... May be no Internet Connection\n")
         time.sleep(2)
   print(green, os.system("echo Device Name: $(getprop ro.transsion.device.name)"))
   exit()

def menu():
   parser = argparse.ArgumentParser(description='Wt u wanna Do')
   parser.add_argument('-t','--tool', help='Choose Tool', required=True)
   args = vars(parser.parse_args())
   if args['tool'] == "sms":
    SMS()
   elif args['tool'] == "trackuser":
    track_user()
   elif args['tool'] == "trackip":
    track_ip()
   elif args['tool'] == "mydevice":
    me_info()
   else:
       print(red+"idk wt the hell u wnt here😑")
       exit()

def SMS():
   try:
      os.system("clear")
      banner()
      number = input(green+"Enter Phone number: "+cyan)
      print("")
      msg = input(green+"Enter Message: "+cyan)
      print("")
      send = requests.post("https://textbelt.com/text", data={'phone': number, 'message': msg, 'key': 'textbelt'}).json()
      if send['success'] == "True":
       print(green+"Message Sent")
       print(green+"You remained with: " + req['quotaRemaining'])
       print("")
      else:
          print(red+"Message Not Sent")
          print(green+send['error'])
          print("")
   except:
          print(red+"Failed to Start, maybe Internet problem!")

def track_user():
   os.system("neofetch --logo --ascii_distro " + random.choice(dist))
   user = input(green+"Enter Usename: "+cyan)
   print("\n")
   #check facebook
   try:
      fb = requests.get("https://www.facebook.com/" + user, headers={'User-Agent': 'your bot 0.1'})
      if fb.status_code in reqsuccess:
       print(green+"User Found in FB")
       print(green+"Profile Link -->: " + cyan+web[0] + user)
      else:
          print(red+"User Not Found in FB")
      print("\n")
      ig = requests.get("https://www.instagram.com/" + user, headers={'User-Agent': 'your bot 0.1'})
      if ig.status_code in reqsuccess:
       print(green+"User Found in InstaGram")
       print(green+"Profile Link -->: " + cyan+web[2] + user)
      else:
          print(red+"User Not Found in Instagram")
      print("\n")
      twt = requests.get("https://www.twitter.com/" + user, headers={'User-Agent': 'your bot 0.1'})
      if twt.status_code in reqsuccess:
       print(green+"User Found in Twitter")
       print(green+"Profile Link -->: " + cyan+web[1] + user)
      else:
          print(red+"User Not Found in Twitter")
      print("\n")
      tiktok = requests.get("https://www.tiktok.com/@" + user, headers={'User-Agent': 'your bot 0.1'})
      if tiktok.status_code in reqsuccess:
       print(green+"User Found in TikTok")
       print(green+"Profile Link -->: " + cyan+web[3] + user)
      else:
          print("User Not Found in TikTok")
      print("\n")
      linkdin = requests.get(web[4] + user, headers={'User-Agent': 'your bot 0.1'})
      if linkdin.status_code in reqsuccess:
       print(green+"User Found in Linkedin")
       print(green+"Profile link -->: " + cyan+web[4] + user)
      else:
          print(red+"User Not Found in Linkedin")
      print("\n")
      github = requests.get(web[5] + user, headers={'User-Agent': 'your bot 0.1'})
      if github in reqsuccess:
       print(green+"User Found in Github")
       print(green+"Profile Link -->: " + cyan+web[5] + user)
      else:
          print(red+"User Not Found in Github")
      print("\n")
      redd = requests.get(web[6] + user, headers={'User-Agent': 'your bot 0.1'})
      if redd.status_code in reqsuccess:
       print(green+"User Found in Reddit")
       print(green+"Profile Link -->: " + cyan+web[6] + user)
      else:
          print(red+"User Not Found in Reddit")
      print("\n")
      pint = requests.get(web[7] + user, headers={'User-Agent': 'your bot 0.1'})
      if pint.status_code in reqsuccess:
       print(green+"User Found in Pinterest")
       print(green+"Profile Link -->: " + cyan+web[7] + user)
      else:
          print(red+"User Not Found in Pinterest")
      print("\n")
      vsco = requests.get(web[8] + user, headers={'User-Agent': 'your bot 0.1'})
      if vsco.status_code in reqsuccess:
       print(green+"User Found in Vsco")
       print(green+"Profile Link -->: " + cyan+web[8] + user)
      else:
          print(red+"User Not Found in Vsco")
      print("\n")
      sc = requests.get(web[9] + user, headers={'User-Agent': 'your bot 0.1'})
      if sc.status_code in reqsuccess:
       print(green+"User Found in SoundCloud")
       print(green+"Profile Link -->: " + cyan+web[9] + user)
      else:
          print(red+"User Not Found in SoundCloud")
      print("\n")
      snap = requests.get(web[10] + user, headers={'User-Agent': 'your bot 0.1'})
      if snap.status_code in reqsuccess:
       print(green+"User Found in Snapchat")
       print(green+"Profile Link -->: " + cyan+web[10] + user)
      else:
          print(red+"User Not Found in Snapchat")
      print("\n")
      quora = requests.get(web[11] + user, headers={'User-Agent': 'your bot 0.1'})
      if quora.status_code in reqsuccess:
       print(green+"User Found In Quora")
       print(green+"Profile link -->: " + cyan+web[11] + user)
      else:
          print(red+"User Not Found in Quora")
      print("\n")
      flick = requests.get(web[12] + user, headers={'User-Agent': 'your bot 0.1'})
      if flick.status_code in reqsuccess:
       print(green+"User Found in Flickr")
       print(green+"Profile Link -->: " + cyan+web[12] + user)
      else:
          print(red+"User Not Found in Flickr")
      print("\n")
      linktr = requests.get(web[13] + user, headers={'User-Agent': 'your bot 0.1'})
      if linktr.status_code in reqsuccess:
       print(green+"User Found in Linktr")
       print(green+"Profile Link -->: " + cyan+web[13] + user)
      else:
          print(red+"User Not Found in Linktr")
      print("\n")
      ask = requests.get(web[14] + user, headers={'User-Agent': 'your bot 0.1'})
      if ask.status_code in reqsuccess:
       print(green+"User Found in Ask")
       print(green+"Profile Link -->: " + cyan+web[14] + user)
      else:
          print(red+"User Not Found in Ask")
      print("\n")
   except:
         print(red+"Error Occured, Maybe Internet Problem!")
         exit()

menu()
