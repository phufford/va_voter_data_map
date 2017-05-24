#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import selenium.webdriver
import PIL.Image
import urllib.request
import io
import os
import logging

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


DRIVER_PATH = 'include/phantomjs/phantomjs'
URL = 'http://historical.elections.virginia.gov'
logger = logging.Logger('root')
logging.basicConfig(level=logging.INFO)


def debug(driver):
    PIL.Image.open(io.BytesIO(driver.get_screenshot_as_png())).show()


if os.path.exists(DRIVER_PATH):
    browser = selenium.webdriver.PhantomJS(DRIVER_PATH)
    logging.info('Using local installation of phantomjs')
else:
    browser = selenium.webdriver.PhantomJS()
    logging.info('Using default installation of phantomjs')

browser.get(URL)
logging.info(f'Going to page `{URL}`')

findelement = browser.find_element_by_css_selector
findelements = browser.find_elements_by_css_selector

browser.find_element_by_css_selector(
    '''#search_form_elections>div>#SearchIndexForm>div>input.splashy.tan'''
).click()
logging.info(f'Clicking on search button to get all results')


def curl(url):
    """
    http://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
    """
    logger.debug(f'Downloading {url}')
    response = urllib.request.urlopen(url)
    data = response.read()
    return data.decode()


downloadURL = URL + '/elections/download/'


def getCSV(tablerow):
    tr_id = row.get_attribute('id')
    tr_id = tr_id.replace('election-id-', '')
    assert tr_id.isdigit()
    url = downloadURL + tr_id
    return curl(url)


def pages(driver):
    old = False
    new = True
    while old != new:
        print(old == new)
        old = driver.find_element_by_css_selector('body').get_attribute(
            'innerHTML'
        )
        logging.info('Fetching new page')
        driver.find_element_by_css_selector(
            '#search_results_table_next'
        ).click()
        yield driver
        new = driver.find_element_by_css_selector('body').get_attribute(
            'innerHTML'
        )


for i in pages(browser):
    i.find_element_by_css_selector(
        '#search_results_table_next'
    ).get_attribute('class')
    for row in browser.find_elements_by_css_selector('tr.election_item'):
        getCSV(row)
