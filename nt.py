#!/usr/bin/env python3
from networktables import NetworkTables
import time
import socket
from termcolor import colored

REFRESH_RATE = 0.5  # Hertz

my_ip = socket.gethostbyname(socket.getfqdn())
ip_bytes = my_ip.split('.')
ip_bytes[-1] = 2
rio_ip = '.'.join(ip_bytes)
NetworkTables.initialize(server=rio_ip)

def log(key, value, isNew):
    print('{key} => {value}'.format(key=colored(key, 'cyan'),
                                    value=colored(value, 'green'))

NetworkTables.addEntryListener(log)
while True:
    time.sleep(1/REFRESH_RATE)
