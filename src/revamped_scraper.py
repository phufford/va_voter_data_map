#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from selenium import webdriver

__appname__     = ""
__author__      = "Peter Hufford"
__copyright__   = ""
__credits__     = ["Peter Hufford", "Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "msirabel@gmail.com"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = ""

ELECTION_ID_FILENAME = 'election_ids.txt'
METADATA_FILENAME = 'metadata.json'
DRIVER_PATH = 'phantomjs-2.1.1-linux-x86_64/bin/phantomjs'
URL = 'http://historical.elections.virginia.gov'


def main():
    driver = webdriver.PhantomJS(DRIVER_PATH)
    driver.get(URL)


def get_years():
    years = tuple(year for year in
    driver.find_elements_by_css_selectors("#SearchYearFrom option" if year))
    return years

def office_urls(year_url):
