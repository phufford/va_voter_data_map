#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
from selenium import webdriver

__appname__     = ""
__author__      = "phufford"
__copyright__   = ""
__credits__     = ["phufford", "Marco Sirabella"]  # Authors and bug reporters
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

def add_election_id(row):
    election_id = row.get_property('id').split('-')[-1]
    print (election_id)
    if election_id:
        election_ids.append(election_id)

def add_metadata(row):
    election_id = row.get_property('id').split('-')[-1]
    if election_id:
        discriptors = row.find_elements_by_css_selector('td')
        data = {'year': discriptors[0].text,
                'office': discriptors[1].text,
                'district': discriptors[2].text,
                'stage': discriptors[3].text,
                'discription': discriptors[4].text}
        metadata[election_id] = data


def build_office_urls(year_url):
    office_urls = []
    for office_id in office_ids:
        office_url = year_url + '/office_id:' + office_id
        office_urls.append(office_url)
    return office_urls

def build_search_url(year):
    return URL + '/elections/search/year_from:' + year + '/year_to:' + year

def get_office_ids():
    office_ids = []
    for option in driver.find_elements_by_css_selector(
            '#SearchOfficeId optgroup option'):
        office_ids.append(option.get_property('value'))
    return office_ids

def get_results_length():
    try:
        div = driver.find_element_by_css_selector('#search_results_table_info')
        length = div.text
        if length == "Showing 600 items":
            return 600
        else:
            return length
    except:
        return 0


def get_years():
    years = []
    for year in driver.find_elements_by_css_selector(
            "#SearchYearFrom option"):
        year = year.text
        if year is not u'':
            years.append(year)
    return years

def get_years_search_urls():
    urls = []
    for year in years:
        urls.append(build_search_url(year))
    return urls

def scrape_page():
    if get_results_length() == 0:
        return
    show_all()
    for row in driver.find_elements_by_css_selector(
            '#search_results_table tbody tr'):
        add_election_id(row)
        add_metadata(row)

def scrape_year(url):
    print ('Scraping: ' + url)
    driver.get(url)
    if get_results_length() == 600:
        scrape_year_by_office(url)
    else:
        scrape_page()

def scrape_year_by_office(url):
    print ('Search by year returns more than 600 results.')
    print ('Searching year by office as well...')
    office_urls = build_office_urls(url)
    for url in office_urls:
        print ('Scraping: ' + url)
        driver.get(url)
        scrape_page()

def show_all():
    show_all = driver.find_element_by_xpath(
        '//*[@id="search_results_table_length"]/label/select/option[4]')
    show_all.click()

def write_election_ids_to_file():
    with open(ELECTION_ID_FILENAME, 'w') as f:
        for election_id in election_ids:
            f.write(election_id + '\n')

def write_metadata_to_file():
    with open(METADATA_FILENAME, 'w') as f:
        json.dump(metadata, f)

driver = webdriver.PhantomJS(DRIVER_PATH)
driver.get(URL)

years = get_years()
office_ids = get_office_ids()
years_search_urls = get_years_search_urls()

election_ids = []
metadata = {}
for year_url in years_search_urls:
    scrape_year(year_url)
election_ids.sort()
write_election_ids_to_file()
write_metadata_to_file()
