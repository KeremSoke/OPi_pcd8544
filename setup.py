#!/usr/bin/env python

from distutils.core import setup
setup(
    name = "OPi_pcd8544",
    version = "0.1.0",
    author = "Kerem Soeke",
    author_email = "keremsoke@gmail.com",
    description = ("A small library to drive the PCD8544 LCD using OPi.GPIO"),
    license = "GPLv3",
    keywords = "orange pi opi pcd 8544 lcd nokia 3310 5110",
    url = "https://github.com/KeremSoke/OPi_pcd8544",
    packages=['OPi_pcd8544'],
    package_dir={'OPi_pcd8544': 'src'}
)
