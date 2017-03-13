import getNextChord
import json
import random
from collections import OrderedDict
from collections import Counter

def Main(startingChord, complexity, length):
    topProbabilities = {}
    progression = []

    getNextChord.findProgression(startingChord)
    progression.append(startingChord)

    #finds top most probable chord selections
    for chords in range(length):
        with open('chordProbabilities.json') as probabilities:
            chordProbability = json.load(probabilities)

        for items in range(complexity):
            topProbabilities[chordProbability[items]['chord_ID']] = chordProbability[items]['probability']
            nextChords = Counter(topProbabilities)

        tempChord = random.choice(list(nextChords))
        getNextChord.findProgression(tempChord)
        print tempChord
        topProbabilities = {}
Main(1, 4, 4)
