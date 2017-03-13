from midiutil.MidiFile import MIDIFile

class Midi():
    def __init__(self):
        self.midiFile = MIDIFile(1)

    def writeMidiChord(self, root, third, fifth, chordStart, colorTone=None):
        track = 0

        time = 0
        self.midiFile.addTrackName(track, time, "Sample Track")
        self.midiFile.addTempo(track, time, 120)

        channel = 1
        volume = 100

        pitch = root-24
        time = chordStart
        duration = 2
        self.midiFile.addNote(track, channel, pitch, time, duration, volume)

        pitch = root
        time = chordStart
        duration = 2
        self.midiFile.addNote(track, channel, pitch, time, duration, volume)

        pitch = third
        time = chordStart
        duration = 2
        self.midiFile.addNote(track, channel, pitch, time, duration, volume)

        pitch = fifth
        time = chordStart
        duration = 2
        self.midiFile.addNote(track, channel, pitch, time, duration, volume)

        if colorTone is not None:
            pitch = colorTone
            time = chordStart
            duration = 2
            self.midiFile.addNote(track, channel, pitch, time, duration, volume)

    def WriteMidiToFile(self):
        with open("MIDI/output.mid", 'wb') as outf:
            self.midiFile.writeFile(outf)
