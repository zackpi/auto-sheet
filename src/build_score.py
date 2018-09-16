def func(num, den)
    num_dots = 3//2
    return 

def display(chord_seq, keysig="#", timesig=120):
    import abjad as abj
    
    sixteenth = abj.Duration(1, 16)
    # eighth = abj.Duration(1, 8)
    # quarter = abj.Duration(1, 4)
    # half = abj.Duration(1, 2)
    # whole = abj.Duration(1, 1)
    
    # prevchord = None
    melody = []
    for timestep, notes in enumerate(chord_seq):
        if len(notes):
            newchord = abj.Chord([note[0] if keysig == "#" else note[1] for note in notes], sixteenth)
            """
            if prevchord.written_pitches == newchord.written_pitches:
                prevchord = abj.Chord(prevchord.writtenpitches,
                                        abj.Duration(prevchord.numerator+1, 
                                                    prevchord.denominator))
            else:    
                melody.append(prevchord)
                prevchord = newchord
            """
            melody.append(newchord)
        else:
            melody.append(abj.Rest(duration))
            # prevchord = None
    # melody.append(prevchord)
    
    staff = abj.Staff(melody)
    abj.show(staff)

if __name__ == '__main__':
    display(("cs2", "bb7", "a0"))
