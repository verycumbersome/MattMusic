import json
import urllib2

def findProgression(chord):
    with open('config/credentials.json') as data_file:
       data = json.load(data_file)

    req = urllib2.Request("https://api.hooktheory.com/v1/users/auth", json.dumps(data), headers={'Content-type': 'application/json', 'Accept': 'application/json'})
    response = urllib2.urlopen(req)
    the_page = json.loads(response.read())

    trends = urllib2.Request("https://api.hooktheory.com/v1/trends/nodes?cp=" + str(chord), headers={'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer ' + the_page["activkey"]})
    openTrends = urllib2.urlopen(trends)
    nextChord = openTrends.read()

    with open('config/chordProbabilities.json', 'w') as chordProbabilities:
        json.dump(json.loads(nextChord), chordProbabilities, indent=4, sort_keys=True)
