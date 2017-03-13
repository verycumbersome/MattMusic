import getNextChord
import json
import random
import writeMIDI
from collections import Counter

def Main(startingChord, complexity, length):
    topProbabilities = {}
    progression = []

    MIDInstance = writeMIDI.Midi()

    getNextChord.findProgression(startingChord)
    progression.append(startingChord)

    with open('chords.json') as chordsJSON:
        chordMIDI = json.load(chordsJSON)
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
        MIDInstance.writeMidiChord(chordMIDI[str(tempChord)]['root'], chordMIDI[str(tempChord)]['third'], chordMIDI[str(tempChord)]['fifth'], (chords-1)*2, chordMIDI[str(tempChord)]['colorTone'])
    MIDInstance.WriteMidiToFile()
Main(1, 5, 4)
