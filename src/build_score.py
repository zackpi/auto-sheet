def display(chord_seq, keysig="#", timesig=120):
    import abjad as abj
    
    duration = abj.Duration(1, 4)
    
    melody = []
    for timestep, notes in enumerate(chord_seq):
        if len(notes):
            chord = abj.Chord([note[0] if keysig == "#" else note[1] for note in notes], duration)
            melody.append(chord)
        else:
            melody.append(abj.Rest(duration))
    
    staff = abj.Staff(melody)
    abj.show(staff)

if __name__ == '__main__':
    display(("cs2", "bb7", "a0"))
