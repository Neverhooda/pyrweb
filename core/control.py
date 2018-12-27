"""@package Core for control over Yprick
serial
"""

# !/usr/bin/env python
# -*- coding: UTF-8 -*-

import serial


class Core(object):
    def __init__(self):
        self.serial = serial.Serial()
        self.serial.baudrate = 9600
        self.port('/dev/ttyUSB0')
        self.serial.open()

    def send_command(self, action, parameters=[]):
        pass

