# Hacking-Tools
A repository of customized hacking tools

NOTE: These were configured for Linux. You may need to tweak the code a bit if you want to use them on Linux

## arp_spoofer.py

### Requirements
+ Python

### Usage
```
usage: python3 arp_spoofer.py victim_ip router_ip

options:
victim_ip    IP address of the target system
router_ip    IP address of the router
```

## arp_spoofing_detecter.py

### Requirements
+ Python
+ Packages :
  + Scapy


### Usage
```
usage: python3 arp_spoofer.py
```

## duolingo_data.py

### Requirements
+ Python
+ Packages :
  + iso-639
  + pycountry

### Usage

```
usage: python3 duoling_data.py [-h] (-m MAIL | -u USERNAME)

options:
  -h, --help            show this help message and exit
  -m MAIL, --mail MAIL  Target mail address
  -u USERNAME, --username USERNAME Target Duolinguo username
```

Inspired by [Emmanuel Ajuelos](https://github.com/ajuelosemmanuel/duolingOSINT)'s work

## lsb_steganography.py

### Requirements
+ Python
+ Packages :
  + stego_lsb
  + tkinter

### Usage
```
usage: python3 lsb_steganography.py
```
## mac_changer.py

### Requirements
+ Python
+ Packages :
  + subprocess 
  + python-generate-mac

### Usage

```
Edit line 11 of the script to the interface then run:
python3 mac_changer.py
```


## mac_flooder.py

### Requirements
+ Python
+ Packages :
  + Scapy

### Usage

```
Edit line 10 of the script to the interface for flooding then run:
python3 mac_flooder.py
```
