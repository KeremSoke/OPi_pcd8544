#!/usr/bin/env python
# -*- coding: utf-8 -*-
import OPi_pcd8544.lcd as lcd
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

try:
  lcd.init()
  lcd.cls()
  lcd.centre_text(0," Orange Pi")
  while 1:
     lcd.centre_text(2,time.strftime("  %d %b %Y     ", time.localtime()))
     lcd.centre_text(4,time.strftime("  %H:%M:%S", time.localtime()))
     time.sleep(0.25)
except KeyboardInterrupt:
  pass
finally:
  lcd.cls()

