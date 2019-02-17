#!/usr/bin/env python3

from networktables import NetworkTables
from networktables.util import ntproperty
import time

NetworkTables.initialize(server='10.14.18.2')
table = NetworkTables.getTable()
print(table.getBoolean('robot/manual_lift_control', False))
