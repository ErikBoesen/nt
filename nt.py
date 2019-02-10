#!/usr/bin/env python3

from networktables import NetworkTables
from networktables.util import ntproperty
import time

TEAM = 1418

class Interface:
    def __init__(self):
        NetworkTables.initialize(server='roborio-%d-frc.local')
        self.value = NetworkTables.getGlobalAutoUpdateValue('/vision/targets_seen', 0, writeDefault=False)

    def log(self):
        print(self.value.value)

if __name__ == '__main__':
    interface = Interface()
    while True:
        interface.log()
        time.sleep(0.5)
