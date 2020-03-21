#!/usr/bin/env python
# -*- coding: utf-8 -*-
import OPi_pcd8544.lcd as lcd
import time, os, sys

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

try:
  lcd.init()
  lcd.cls()
  # Test a custom character for 0x7f (supposed to be a bell)
  # . . . - - - - -
  # . . . - - X - -
  # . . . - X X X -
  # . . . - X - X -
  # . . . X - - - X
  # . . . X X X X X
  # . . . - - X X -
  # . . . - - - - -
  lcd.define_custom_char([0x30,0x2c,0x66,0x6c,0x30])
  lcd.text("\x7f \x7f \x7f \x7f \x7f \x7f \x7f ")
  lcd.text("    Hello     ")
  lcd.text(" Raspberry Pi")
  time.sleep(10);
except KeyboardInterrupt:
  pass
finally:
  lcd.cls()

