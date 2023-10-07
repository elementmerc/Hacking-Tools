#File:mac_changer.py
#Author: Mercury
#Function: A script to change the ethernet MAC addres

#Importing the necessary libraries
import subprocess
from generate_mac import generate_mac

#setting up the function
if __name__ == "__main__":
	interface = "eth0" #Change this to whatever interface you want e.g wlan0
	new_mac = generate_mac.total_random()
	
	print("Shutting down the interface")
	subprocess.run(["ifconfig", interface, "down"])
	
	print(f"Changing the interface hw adsdress of {interface} to {new_mac}")
	subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])

	print(f"MAC address changed to {new_mac}")
	subprocess.run(["ifconfig", interface, "up"])
	print("Network interface turned on")