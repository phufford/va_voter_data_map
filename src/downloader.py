#!/usr/bin/env python3

import sys
import urllib.request

DIRECTORY = './data/'
ELECTION_ID_FILENAME = 'src/election_ids.txt'
LOG_FILENAME = 'downloads.log'

ids = open(ELECTION_ID_FILENAME, 'r')

def build_url(election_id):
    return ('http://historical.elections.virginia.gov/elections/download/' \
        + election_id)

election_id = 'foo'
while election_id:
    z = ids.readline()

    election_id = ids.readline().strip() # Remove /n
    print('downloading: ' + election_id)
    try:
        with open(DIRECTORY + election_id + '.csv', 'wb') as csv:
            response = urllib.request.urlopen(build_url(election_id))
            csv.write(response.read())
        with open(DIRECTORY + election_id + '_precinct' + '.csv', 'wb') as csv:
            response = urllib.request.urlopen(
                build_url(election_id) + '/precincts_include:1/')
            csv.write(response.read())

    except Exception as e:
        print(e)
        print ('Failed to download ' + election_id + '/n')
        with open(LOG_FILENAME, 'w') as log:
            log.write('Failed to download ' + election_id + '/n')

print ('done')
