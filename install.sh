#!/bin/bash

echo "Installing and verifying dependencies."

sudo apt install python-pip python-dev python-setuptools -y
sudo -H pip install spidev
sudo -H pip install OPi.GPIO

echo "------------------OPi_pcd8544------------------"

sudo python setup.py install
