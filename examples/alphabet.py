#!/usr/bin/env python
# -*- coding: utf-8 -*-
import OPi_pcd8544.lcd as lcd
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

try:
    lcd.init()
    lcd.cls()
    for i in xrange(32, 116):
        lcd.display_char(chr(i))
    time.sleep(10)
except KeyboardInterrupt:
  pass
finally:
  lcd.cls()

