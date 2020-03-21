#!/usr/bin/env python
# -*- coding: utf-8 -*-
import OPi_pcd8544.lcd as lcd
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

try:
  lcd.init()
  lcd.cls()
  lcd.centre_text(2,"contrast")
  for i in range(150,200,5):
      lcd.set_contrast(i)
      lcd.centre_text(3,"%d" % i)
      time.sleep(1)
  for i in range(200,150,-5):
      lcd.set_contrast(i)
      lcd.centre_text(3,"%d" % i)
      time.sleep(1)
except KeyboardInterrupt:
  pass
finally:
  lcd.cls()

