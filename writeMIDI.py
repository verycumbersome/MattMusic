from midiutil.MidiFile import MIDIFile

class Midi():
    def __init__(self):
        self.midiFile = MIDIFile(1)

    def writeMidiChord(self, root, third, fifth, chordStart, colorTone=None):
        track = 0   # the only track

        time = 0    # start at the beginning
        self.midiFile.addTrackName(track, time, "Sample Track")
        self.midiFile.addTempo(track, time, 120)

        channel = 0
        volume = 100

        pitch = root           # C4 (middle C)
        time = chordStart             # start on beat 0
        duration = 2         # 1 beat long
        self.midiFile.addNote(track, channel, pitch, time, duration, volume)

        pitch = third          # E4
        time = chordStart             # start on beat 2
        duration = 2         # 1 beat long
        self.midiFile.addNote(track, channel, pitch, time, duration, volume)

        pitch = fifth           # G4
        time = chordStart             # start on beat 4
        duration = 2         # 1 beat long
        self.midiFile.addNote(track, channel, pitch, time, duration, volume)

        if colorTone is not None:
            pitch = colorTone           # G4
            time = chordStart             # start on beat 4
            duration = 1         # 1 beat long
            self.midiFile.addNote(track, channel, pitch, time, duration, volume)

    def WriteMidiToFile(self):
        with open("output.mid", 'wb') as outf:
            self.midiFile.writeFile(outf)
