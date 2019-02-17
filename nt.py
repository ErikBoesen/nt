#!/usr/bin/env python3
from networktables import NetworkTables
import time

REFRESH_RATE = 0.5  # Hertz

NetworkTables.initialize(server='10.14.18.2')

def log(key, value, isNew):
    print(f'{key} => {value}')

NetworkTables.addEntryListener(log)
while True:
    time.sleep(1/REFRESH_RATE)
