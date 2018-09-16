from abjad import *

def display(): 
	duration = Duration(1, 4)
	notes = [Note(pitch, duration) for pitch in range(8)]
	# [1, 2, 3, 4, 5, 6, 7]

	staff = Staff(notes)
	show(staff)

if __name__ == '__main__':
	print('duration =', duration)
	print('notes =', notes)
	print('show(staff) =', show(staff))