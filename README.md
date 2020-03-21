# OPi_pcd8544
Orange Pi PCD8544 python Module
https://github.com/XavierBerger/pcd8544 edited for Orange Pi 

# EDITING
You must edit /src/lcd.py line 46 to select spi address

# WIRING
Pin numbers --> GPIO.BOARD

DC   = 16

RST  = 18

SCE  = 24 

SCLK = 23

DIN  = 19


# INSTALLING

You can install it directly with install.sh.

sh install.sh
or 
sudo sh install.sh

You can install it manuel.

python-pip python-dev python-setuptools packages must be installed.

sudo apt install python-pip python-dev python-setuptools -y

Spidev and OPi.GPIO modules must be installed

sudo -H pip install spidev

sudo -H pip install OPi.GPIO
