from abjad import *

duration = Duration(1, 4)
notes = [Note(pitch, duration) for pitch in range(8)]
staff = Staff(notes)
show(staff)
