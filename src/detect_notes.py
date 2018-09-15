import numpy as np
from scipy.signal import find_peaks

# notes. If len == 2, 
note_lut = [('c0',), ('c#0', 'db0'), ('d0',), ('d#0', 'eb0'), ('e0',), ('f0',), ('f#0', 'gb0'), ('g0',), ('g#0', 'ab0'), ('a0',), ('a#0', 'bb0'), ('b0',), ('c1',), ('c#1', 'db1'), ('d1',), ('d#1', 'eb1'), ('e1',), ('f1',), ('f#1', 'gb1'), ('g1',), ('g#1', 'ab1'), ('a1',), ('a#1', 'bb1'), ('b1',), ('c2',), ('c#2', 'db2'), ('d2',), ('d#2', 'eb2'), ('e2',), ('f2',), ('f#2', 'gb2'), ('g2',), ('g#2', 'ab2'), ('a2',), ('a#2', 'bb2'), ('b2',), ('c3',), ('c#3', 'db3'), ('d3',), ('d#3', 'eb3'), ('e3',), ('f3',), ('f#3', 'gb3'), ('g3',), ('g#3', 'ab3'), ('a3',), ('a#3', 'bb3'), ('b3',), ('c4',), ('c#4 db4',), ('d4',), ('d#4', 'eb4'), ('e4',), ('f4',), ('f#4', 'gb4'), ('g4',), ('g#4', 'ab4'), ('a4',), ('a#4', 'bb4'), ('b4',), ('c5',), ('c#5', 'db5'), ('d5',), ('d#5', 'eb5'), ('e5',), ('f5',), ('f#5', 'gb5'), ('g5',), ('g#5', 'ab5'), ('a5',), ('a#5', 'bb5'), ('b5',), ('c6',), ('c#6', 'db6'), ('d6',), ('d#6', 'eb6'), ('e6',), ('f6',), ('f#6', 'gb6'), ('g6',), ('g#6', 'ab6'), ('a6',), ('a#6', 'bb6'), ('b6',), ('c7',), ('c#7', 'db7'), ('d7',), ('d#7', 'eb7'), ('e7',), ('f7',), ('f#7', 'gb7'), ('g7',), ('g#7', 'ab7'), ('a7',), ('a#7', 'bb7'), ('b7',), ('c8',), ('c#8', 'db8'), ('d8',), ('d#8', 'eb8')]

# fundamental frequencies of notes
freq_lut = [16, 17, 18, 19, 20, 21, 23, 24, 25, 27, 29, 30, 32, 34, 36, 38, 41, 43, 46, 49, 51, 55, 58, 61, 65, 69, 73, 77, 82, 87, 92, 98, 103, 110, 116, 123, 130, 138, 146, 155, 164, 174, 185, 196, 207, 220, 233, 246, 261, 277, 293, 311, 329, 349, 369, 392, 415, 440, 466, 493, 523, 554, 587, 622, 659, 698, 739, 783, 830, 880, 932, 987, 1046, 1108, 1174, 1244, 1318, 1396, 1479, 1567, 1661, 1760, 1864, 1975, 2093, 2217, 2349, 2489, 2637, 2793, 2959, 3135, 3322, 3520, 3729, 3951, 4186, 4434, 4698, 4978]


# return the peaks in the frequency domain
def peak_freq(fft, **kwargs):
    peaks,_ = find_peaks(fft, **kwargs)
    return peaks


# map peak freq to closest note
def freq_to_note(freq):
    index = 0
    while freq_lut[index] < freq:
        index += 1
    
    if freq_lut[index] - freq > freq - freq_lut[index-1]:
        index -= 1
    return note_lut[index]


# convert all chunks' peaks to notes
def convert_chunks_to_notes():


if __name__=="__main__":
    from scipy.misc import electrocardiogram as ec
    
    peaks = peak_find(ec()[2000:4000])
    #notes = note_map(peaks)
    print(peaks)

