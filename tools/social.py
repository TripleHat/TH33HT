#!/bin/python
# Coded By TripleHat
# Github https://github.com/TripleHat
# Instagram https://instagram.com/wh0ami_1
# Instagram https://instagram.com/triple_hat3
#╺┳╸┏━┓╻┏━┓╻  ┏━╸╻ ╻┏━┓╺┳╸
# ┃ ┣┳┛┃┣━┛┃  ┣╸ ┣━┫┣━┫ ┃
# ╹ ╹┗╸╹╹  ┗━╸┗━╸╹ ╹╹ ╹ ╹

import bs4
import requests
import sys
from bs4 import BeautifulSoup
import json
import random
import string
import argparse
import web
from re import findall
from urllib.request import urlopen, HTTPError

red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
close = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
r_color = ['\033[31m', '\033[93m', '\033[96m', '\033[95m']

url = ["https://instagram.com/", "https://twitter.com/"]
reqSuc = [200, 201, 202, 203]
reqErr = [320, 400, 401, 404, 422, 500, 501, 502, 503, 504]
useragent = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_0) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36',
]

def shorten_url(link):
        apiurl = "http://tinyurl.com/api-create.php?url="
        tinyurl = urlopen(apiurl + link).read()
        return tinyurl.decode("utf-8")

def instagram(username):
 try:
    print(random.choice(r_color)+"")
    profile = requests.get(str(url[0]) + str(username), headers={'User-Agent': random.choice(useragent)})
    soup = BeautifulSoup(profile.text, 'html.parser')
    TH_script = soup.find_all('script', attrs={'type': 'text/javascript'})
    TH_script_Js = str(TH_script[3])
    TH_script_Js = TH_script_Js[51:-10]
    Hacker = json.loads(TH_script_Js)
    Hacked = Hacker['entry_data']['ProfilePage'][0]['graphql']['user']

    TH33HT = '''
                        [TH33HT]

         [TH3HT]--> Username                [•] {}
         [TH3HT]--> Name                    [•] {}
         [TH3HT]--> Url                     [•] {}
         [TH3HT]--> Followers               [•] {}
         [TH3HT]--> Following               [•] {}
         [TH3HT]--> Number of posts         [•] {}
         [TH3HT]--> Biography               [•] {}
         [TH3HT]--> External url            [•] {}
         [TH3HT]--> Private                 [•] {}
         [TH3HT]--> Verified                [•] {}
         [TH3HT]--> Business account        [•] {}
         [TH3HT]--> Connected To Facebook   [•] {}
         [TH3HT]--> Joined recently         [•] {}
         [TH3HT]--> Business category       [•] {}
         [TH3HT]--> Profile Picture         [•] {}

                     [Coded by TripleHat]
     '''.format(str(Hacked['username']), str(Hacked['full_name']),
             str("instagram.com/%s" % username), str(Hacked['edge_followed_by']['count']),
             str(Hacked['edge_follow']['count']), str(Hacked['edge_owner_to_timeline_media']['count']),
             str(Hacked['biography']), str(Hacked['external_url']),
             str(Hacked['is_private']), str(Hacked['is_verified']), str(Hacked['is_business_account']),
             str(Hacked['connected_fb_page']), str(Hacked['is_joined_recently']),
             str(Hacked['business_category_name']), shorten_url(str(Hacked['profile_pic_url_hd'])))
    if profile.status_code in reqSuc:
     print(TH33HT)
     print("")
    if profile.status_code in reqErr:
     print(red+"Username is Not Found😑😑")
     print("")
     exit()

 except:
       print(red+"Ooops!!! Error Occured😑")
       print("")
parser = argparse.ArgumentParser(description='No Help Here, Execute THT.sh')
parser.add_argument('-u','--url', help='shorten your malicious link', required=False)
parser.add_argument('-i','--instagram', help='Spy on Instagram UserName', required=False)
parser.add_argument('-t','--tool', help='choose tool', required=False)
args = vars(parser.parse_args())
#if args['tool'] == "instagram":
#user = args['instagram']
#instagram(args['instagram'])
if args['instagram']:
 instagram(args['instagram'])
if args['url']:
 TH_url =  shorten_url(args['url'])
 print(TH_url)

