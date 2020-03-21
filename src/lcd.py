#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import time
import OPi.GPIO as GPIO
import spidev
from PIL import Image,ImageDraw,ImageFont
from font import FONT

GPIO.setmode(GPIO.BOARD)

# White backlight
CONTRAST = 0xaa

ROWS = 6
COLUMNS = 14
PIXELS_PER_ROW = 6

#gpio's :
DC   = 16
RST  = 18

# SPI connection
SCE  = 24 
SCLK = 23
DIN  = 19


CLSBUF=[0]*(ROWS * COLUMNS * PIXELS_PER_ROW)

ORIGINAL_CUSTOM = FONT['\x7f']

def bit_reverse(value, width=8):
  result = 0
  for _ in xrange(width):
    result = (result << 1) | (value & 1)
    value >>= 1

  return result

BITREVERSE = map(bit_reverse, xrange(256))

spi = spidev.SpiDev()

def init(speed=4000000, contrast=CONTRAST):
    spi.open(1,0) ######################################################################
    spi.max_speed_hz=speed

    # Set pin directions.
    GPIO.setup(DC, GPIO.OUT)
    GPIO.setup(RST, GPIO.OUT)

    # Toggle RST low to reset.
    GPIO.output(RST, GPIO.LOW)
    time.sleep(0.100)
    GPIO.output(RST, GPIO.HIGH)
    # Extended mode, bias, vop, basic mode, non-inverted display.
    set_contrast(contrast)

 


def lcd_cmd(value):
    GPIO.output(DC, GPIO.LOW)
    spi.writebytes([value])


def lcd_data(value):
    GPIO.output(DC, GPIO.HIGH)
    spi.writebytes([value])


def cls():
    gotoxy(0, 0)
    GPIO.output(DC, GPIO.HIGH)
    spi.writebytes(CLSBUF)



def set_contrast(contrast):
    if ( 0x80 <= contrast < 0xFF):
        GPIO.output(DC, GPIO.LOW)
        spi.writebytes([0x21, 0x14, contrast, 0x20, 0x0c])


def gotoxy(x, y):
    if ( (0 <= x < COLUMNS) and (0 <= y < ROWS)):
        GPIO.output(DC, GPIO.LOW)
        spi.writebytes([x+128,y+64])


def gotorc(r, c):
    gotoxy(c*6,r)


def text(string, font=FONT):
    for char in string:
        display_char(char, font)


def centre_text(r, word):
    gotorc(r, max(0, (COLUMNS - len(word)) // 2))
    text(word)


def show_custom_char(font=FONT):
    display_char('\x7f', font)


def define_custom_char(values):
    FONT['\x7f'] = values


def restore_custom_char():
    define_custom_char(ORIGINAL_CUSTOM)


def alt_custom_char():
    define_custom_char([0x00, 0x50, 0x3C, 0x52, 0x44])


def pi_custom_char():
    define_custom_char([0x19, 0x25, 0x5A, 0x25, 0x19])


def display_char(char, font=FONT):
    try:
        GPIO.output(DC, GPIO.HIGH)
        spi.writebytes(font[char]+[0])

    except KeyError:
        pass # Ignore undefined characters.


def load_bitmap(filename, reverse=False):
    mask = 0x00 if reverse else 0xff
    gotoxy(0, 0)
    with open(filename, 'rb') as bitmap_file:
        for x in xrange(6):
          for y in xrange(84):
            bitmap_file.seek(0x3e + y * 8 + x)
            lcd_data(BITREVERSE[ord(bitmap_file.read(1))] ^ mask)


def show_image(im):
    # Rotate and mirror the image
    rim = im.rotate(-90).transpose(Image.FLIP_LEFT_RIGHT)

    # Change display to vertical write mode for graphics
    GPIO.output(DC, GPIO.LOW)
    spi.writebytes([0x22])

    # Start at upper left corner
    gotoxy(0, 0)
    # Put GPIO.HIGH display with reversed bit order
    GPIO.output(DC, GPIO.HIGH)
    spi.writebytes( [ BITREVERSE[ord(x)] for x in list(rim.tostring()) ] )

    # Switch back to horizontal write mode for text
    GPIO.output(DC, GPIO.LOW)
    spi.writebytes([0x20])
