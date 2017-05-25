#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from scraper import *
import time

__appname__     = ""
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

year = 2016
f = os.fork()
while f != 0 and year > 1900:
    time.sleep(1)
    year -= 1
    f = os.fork()

browser = init()
for year in years(browser, [str(year)]):
    for i in pages(browser):
        for row in browser.find_elements_by_css_selector('tr.election_item'):
            getCSV(row)
