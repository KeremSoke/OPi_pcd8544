#!/usr/bin/env python
# -*- coding: utf-8 -*-
import OPi_pcd8544.lcd as lcd
import os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

lcd.init()
lcd.cls()
