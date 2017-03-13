import getNextChord
import json
import random
import writeMIDI
import time
import argparse

from collections import Counter

parser = argparse.ArgumentParser(description='argparser for MattMusic code')
parser.add_argument('-c', '--complexity', help='complexity of progression', type=int, default=7)
parser.add_argument('-l', '--length', help='length in measures of progression', type=int, default=4)
args = parser.parse_args()

def Main(startingChord, complexity, length):
    topProbabilities = {}
    progression = []

    MIDInstance = writeMIDI.Midi()

    getNextChord.findProgression(startingChord)
    progression.append(startingChord)

    with open('config/chords.json') as chordsJSON:
        chordMIDI = json.load(chordsJSON)

    #finds top most probable chord selections
    for chords in range(length):
        with open('config/chordProbabilities.json') as probabilities:
            chordProbability = json.load(probabilities)

        for items in range(complexity):
            topProbabilities[chordProbability[items]['chord_ID']] = chordProbability[items]['probability']
            nextChords = Counter(topProbabilities)

        tempChord = random.choice(list(nextChords))
        getNextChord.findProgression(tempChord)
        print tempChord

        topProbabilities = {}
        MIDInstance.writeMidiChord(chordMIDI[str(tempChord)]['root'], chordMIDI[str(tempChord)]['third'], chordMIDI[str(tempChord)]['fifth'], (chords-1)*4, chordMIDI[str(tempChord)]['colorTone'])

        time.sleep(0.1)           #this is to stop the "Too many requests" issue

    MIDInstance.WriteMidiToFile()

Main(1, args.complexity, args.length)             #Main(Starting Chord, Compleity of Progression, Length of Progression)
