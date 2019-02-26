#!/usr/bin/env python3
from networktables import NetworkTables
import time
import socket
from termcolor import colored
import argparse

"""
def calculate_robot_ip():
    my_ip = socket.gethostbyname(socket.getfqdn())
    ip_bytes = my_ip.split('.')
    ip_bytes[-1] = 2
    rio_ip = '.'.join(ip_bytes)
"""

parser = argparse.ArgumentParser(description='Interact with NetworkTables')
parser.add_argument('--robot', nargs=1, default='localhost')
parser.add_argument('--refresh-rate', nargs=1, default=0.5)
parser.add_argument('--target', default=None)
parser.add_argument('--put', nargs=2, default=None)
args = parser.parse_args()

NetworkTables.initialize(server=args.robot)

def log(key, value, isNew):
    if args.target is not None:
        if not key.startswith(args.target):
            return False
    print('{key} => {value}'.format(key=colored(key, 'cyan'),
                                    value=colored(value, 'green')))

if args.put is not None:
    key, value = tuple(args.put)
    table = NetworkTables.getTable('/')
    table.putValue(key, value)
else:
    NetworkTables.addEntryListener(log)
    while True:
        time.sleep(1/args.refresh_rate)
