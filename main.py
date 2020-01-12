import sys
import json

from scapy.all import *


# open config.json into global config obj
try:
    with open('config.json') as config_file:
        config = json.load(config_file)
    print("[*] Config Loaded")
except:
    print("failed to load config")


def q_sniff():
    try:
        interface = config.input
    except Exception as e:
        print(e)
        print("assuming int wasn't found")


def main():
    

if __name__ == '__main__':
    main()
