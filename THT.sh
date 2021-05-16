#!/bin/bash
# Coded By TripleHat
# Github https://github.com/TripleHat
# Instagram https://instagram.com/wh0ami_1
# Instagram https://instagram.com/triple_hat3
#╺┳╸┏━┓╻┏━┓╻  ┏━╸╻ ╻┏━┓╺┳╸
# ┃ ┣┳┛┃┣━┛┃  ┣╸ ┣━┫┣━┫ ┃
# ╹ ╹┗╸╹╹  ┗━╸┗━╸╹ ╹╹ ╹ ╹

blank='\e[0m'
black='\e[1;90m'
red='\e[1;91m'
green='\e[1;92m'
yellow='\e[1;93m'
blue='\e[1;94m'
pink='\e[1;95m'
ocen='\e[1;96m'
white='\e[1;97m'

load() {
function ProgressBar {

    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done

    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")

printf "\e[1;96m \r [${_fill// /▇}${_empty// / }] ${_progress}%%\e[0m"

}

_start=1

_end=100

for number in $(seq ${_start} ${_end})
do
    sleep 0.0
    ProgressBar ${number} ${_end}
done
printf "\n"
}

banner() {

toilet -f slant TH3 -F gay
echo "████████╗██╗  ██╗██████╗ ██████╗ ██╗  ██╗████████╗ 
╚══██╔══╝██║  ██║╚════██╗╚════██╗██║  ██║╚══██╔══╝
   ██║   ███████║ █████╔╝ █████╔╝███████║   ██║ Coded by
   ██║   ██╔══██║ ╚═══██╗ ╚═══██╗██╔══██║   ██║     TripleHat
   ██║   ██║  ██║██████╔╝██████╔╝██║  ██║   ██║ IG-->wh0ami_1
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝" | lolcat

}

background() {
clear
neofetch --logo windows7
echo ""
echo -e "$ocen BEFORE USING THIS MAKE SURE YOU COPIED YOUR IMAGES FILE TO$green TH3HT$blank$ocen FOLDER IN YOUR FILE MANAGER$blank"
printf "\n"

api_key="ititzKSaRNcWmAvuEVdJ4A3R"

printf "\e[1;95m [\e[1;92m Enter Picture Name \e[1;93m(eg. th3.jpg) \e[1;95m]\e[0m\n"
read -p $'\e[1;95m [TH3HT]->\e[0m\e[1;96m ' picture
printf "\n"
echo "$picture" > temp
default_name="No-Bg"

printf "\e[1;95m [\e[1;92m Enter Name for new Pic \e[1;95m]\e[0m\n"
read -p $'\e[1;95m [TH3HT]->\e[0m\e[1;96m ' name
printf "\n"

name="${name:-${default_name}}"
file="image_file=@$picture"
url() {
curl -s -H 'X-API-Key: ititzKSaRNcWmAvuEVdJ4A3R'  -F "image_file=@$picture" -f https://api.remove.bg/v1.0/removebg -o $name.png
}

check=$(grep -o "[1-9a-zA-Z]*\.jpg" temp || grep -o "[1-9a-zA-Z]*\.png" temp)

if [[ $(cat temp) != "$check" ]]; then
printf "\e[1;91m [!] Enter Valid Pic Name with Extension!\e[0m"
printf "\n"
background
else
cd $EXTERNAL_STORAGE/TH33HT/
url
if [[ -e $name.png ]]; then
printf "\e[92m[√]:Image saved as \e[96m$name.png\e[0m"
echo ""
else
printf "\e[91m[×]:Error occured!\e[0m"
echo ""
fi
fi

}

extra_banner() {
printf "\n"
printf "\e[93m[\e[92m01\e[93m]\e[94m : \e[96mRemove Image Background\e[0m"
printf "\n"
printf "\e[93m[\e[92m02\e[93m]\e[94m : \e[96mTrack IP Address\e[0m"
printf "\n"
printf "\e[93m[\e[92m03\e[93m]\e[94m : \e[96mTrace Username\e[0m"
printf "\n"
printf "\e[93m[\e[92m04\e[93m]\e[94m : \e[96mSend SMS (worldwide)\e[0m"
printf "\n"
printf "\e[93m[\e[92m05\e[93m]\e[94m : \e[96mGet Profile Info [Instagram]\e[0m"
printf "\n"
printf "\e[93m[\e[92m06\e[93m]\e[94m : \e[96mShow Your Device info\e[0m"
printf "\n"
printf "\e[93m[\e[92m00\e[93m]\e[94m : \e[91mExit Tool\e[0m"
echo ""
}

choice() {
printf "\n"
read -p $'\e[1;95m [TH3HT]->\e[0m\e[1;96m ' option
printf "\n"

if [[ $option == "1" || $option == "01" ]]; then
load
background
extra_banner
choice
elif [[ $option == "2" || $option == "02" ]]; then
load
clear
python3 tools/track.py --tool trackip
extra_banner
choice
elif [[ $option == "3" || $option == "03" ]]; then
load
clear
python3 tools/track.py --tool trackuser
extra_banner
choice
elif [[ $option == "4" || $option == "04" ]]; then
load
clear
python3 tools/track.py --tool sms
extra_banner
choice
elif [[ $option == "6" || $option == "06" ]]; then
load
clear
python3 tools/track.py --tool mydevice
extra_banner
choice
elif [[ $option == "5" || $option == "05" ]]; then
echo ""
printf "\e[92m[Enter Instagram Username]\e[0m"
read -p $'\e[1;95m [TH3HT]->\e[0m\e[1;96m ' inf
if [[ $inf == "" ]]; then
echo ""
printf "\e[91m😑😑No blank Username in Social Network😑😑\e[0m"
sleep 3
clear; menu
else
echo " "
load
python3 tools/social.py -i $inf
extra_banner
choice
fi
elif [[ $option == "0" || $option == "00" ]]; then
toilet -f future -F gay Coded by TripleHat
toilet -f slant -F metal Bye Bye
load
exit 0
else
echo -e "$red $(toilet -f mono12 404)"
sleep 2
load
choice
fi
}

#update() {
#echo -e "$green [!]Checking for Updates$blank"
#fuck=$(wget https://raw.githubusercontent.com/TripleHat/TH33HT/master/tools/update -q && grep -o "1" v1)
#if [[ $fuck == "1" ]]; then
#echo -e "$green [√]No update Found$blank"
#sleep 1
#rm v1
#else
#echo -e "$yellow [!]New Version Found$blank"
#rm v1
#echo " "
#read -p "Do you want to update (Y/n): " update
#case $update in
#Y | y)
#echo " "
#N | n)
#echo -e "$yellow Make sure to update, new features are added and issues are fixed$blank"
#read -p "press enter to continue"
#sleep 1 ;;
#esac
#fi
#}

main() {
clear
banner
printf "\n"
printf "\e[93m[\e[92m01\e[93m]\e[94m : \e[96mRemove Image Background\e[0m"
printf "\n"
printf "\e[93m[\e[92m02\e[93m]\e[94m : \e[96mTrack IP Address\e[0m"
printf "\n"
printf "\e[93m[\e[92m03\e[93m]\e[94m : \e[96mTrace Username\e[0m"
printf "\n"
printf "\e[93m[\e[92m04\e[93m]\e[94m : \e[96mSend SMS (worldwide)\e[0m"
printf "\n"
printf "\e[93m[\e[92m05\e[93m]\e[94m : \e[96mGet Profile Info [Instagram]\e[0m"
printf "\n"
printf "\e[93m[\e[92m06\e[93m]\e[94m : \e[96mShow Your Device info\e[0m"
printf "\n"
printf "\e[93m[\e[92m00\e[93m]\e[94m : \e[91mExit Tool\e[0m"
echo ""
choice
}

main
