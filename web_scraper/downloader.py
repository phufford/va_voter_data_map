import logging
import sys
import urllib2

DIRECTORY = './data/'
ELECTION_ID_FILENAME = 'election_ids.txt'
LOG_FILENAME = 'downloads.log'

logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)
ids = open(ELECTION_ID_FILENAME, 'r')

def build_url(election_id):
    return ('http://historical.elections.virginia.gov/elections/download/' \
        + election_id)

election_id = 'foo'
while election_id:
    election_id = ids.readline()[0:-1] # Remove /n
    print ('downloading: ' + election_id)
    try:
        with open(DIRECTORY + election_id + '.csv', 'w') as csv:
            response = urllib2.urlopen(build_url(election_id))
            csv.write(response.read())
        with open(DIRECTORY + election_id + '_precinct' + '.csv', 'w') as csv:
            response = urllib2.urlopen(
                build_url(election_id) + '/precincts_include:1/')
            csv.write(response.read())
    except:
        log.warning('Failed to download ' + election_id 
                    + '/n' + sys.exc_info()[0])

print ('done')
