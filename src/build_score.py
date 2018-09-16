from abjad import *

def display(chord_seq, keysig="#", timesig=120):
    duration = Duration(1, 4)
    
    melody = []
    for timestep, notes in enumerate(chord_seq):
        chord = Chord()
        for note in notes:
            chord.append(note[0] if keysig == "#" else note[1])
        melody.append(chord)
    
    staff = Staff(notes)
    show(staff)

if __name__ == '__main__':
    display(("cs2", "bb7", "a0"))
