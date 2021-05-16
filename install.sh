#!/bin/bash
# Coded By TripleHat
# Github https://github.com/TripleHat
# Instagram https://instagram.com/wh0ami_1
# Instagram https://instagram.com/triple_hat3
#╺┳╸┏━┓╻┏━┓╻  ┏━╸╻ ╻┏━┓╺┳╸
# ┃ ┣┳┛┃┣━┛┃  ┣╸ ┣━┫┣━┫ ┃
# ╹ ╹┗╸╹╹  ┗━╸┗━╸╹ ╹╹ ╹ ╹

red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
blue='\033[1;34m'
light_cyan='\033[1;96m'
reset='\033[0m'
clear
printf "${blue}\n[*] Checking package dependencies...${reset}\n"
    apt update -y &> /dev/null

for i in curl wget toilet ruby python python3 ; do
        if [ -e $PREFIX/bin/$i ]; then
            echo -e "$light_cyan  $i is OK"
sleep 1
	else
	printf "Installing ${i}...\n"
	apt install -y $i || {
                printf "${red}ERROR: Failed to install packages.\n Exiting.\n${reset}"
                exit
            }
        fi
    done
    apt upgrade -y

gem install lolcat
pip install -r triplehat.txt
toilet -f future Use bash THT.sh 
toilet -f future To start This Tool
sleep 3
if [[ -e $EXTERNAL_STORAGE ]]; then
 if [[ -e /sdcard/TH33HT ]]; then
   echo " "
 else
   mkdir /sdcard/TH33HT
 fi
else
termux-setup-storage
mkdir /sdcard/TH33HT
fi
chmod +x THT.sh
./THT.sh
