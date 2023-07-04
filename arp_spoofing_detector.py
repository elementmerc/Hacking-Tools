#File:arp_detector.py
#Author: Mercury
#Function: A script to detect arp poisoning

#Importing the necessary libraries
from scapy.all import sniff

#Setting up the map
IP_MAC_MAP = {}

#The engine
def process_packet(packet):
    src_IP = packet['ARP'].psrc
    src_MAC = packet['Ether'].src

    if src_MAC in IP_MAC_MAP.keys():
        if IP_MAC_MAP[src_MAC] != src_IP:
            try:
                old_IP = IP_MAC_MAP[src_MAC]
            except:
                old_IP = 'unknown'
            message = ('\n Possible ARP attack detected \n'
                       + 'It is possible that the machine with IP address \n'
                       + str(old_IP) + ' is pretending to be ' + str(src_IP))
            return message
    else:
    	IP_MAC_MAP[src_MAC] = src_IP

#Kicking off    
sniff(count=0, filter="arp", store=0, prn = process_packet)
