import numpy as np
from scipy.signal import find_peaks

# notes. If len == 2, 
note_lut = [('c0', 'c0'), ('cs0', 'db0'), ('d0', 'd0'), ('ds0', 'eb0'), ('e0', 'e0'), ('f0', 'f0'),
            ('fs0', 'gb0'), ('g0', 'g0'), ('gs0', 'ab0'), ('a0', 'a0'), ('as0', 'bb0'), ('b0', 'b0'),
            ('c1', 'c1'), ('cs1', 'db1'), ('d1', 'd1'), ('ds1', 'eb1'), ('e1', 'e1'), ('f1', 'f1'),
            ('fs1', 'gb1'), ('g1', 'g1'), ('gs1', 'ab1'), ('a1', 'a1'), ('as1', 'bb1'), ('b1', 'b1'), 
            ('c2', 'c2'), ('cs2', 'db2'), ('d2', 'd2'), ('ds2', 'eb2'), ('e2', 'e2'), ('f2', 'f2'), 
            ('fs2', 'gb2'), ('g2', 'g2'), ('gs2', 'ab2'), ('a2', 'a2'), ('as2', 'bb2'), ('b2', 'b2'), 
            ('c3', 'c3'), ('cs3', 'db3'), ('d3', 'd3'), ('ds3', 'eb3'), ('e3', 'e3'), ('f3', 'f3'), 
            ('fs3', 'gb3'), ('g3', 'g3'), ('gs3', 'ab3'), ('a3', 'a3'), ('as3', 'bb3'), ('b3', 'b3'), 
            ('c4', 'c4'), ('cs4', 'cs4'), ('d4', 'd4'), ('ds4', 'eb4'), ('e4', 'e4'), ('f4', 'f4'), 
            ('fs4', 'gb4'), ('g4', 'g4'), ('gs4', 'ab4'), ('a4', 'a4'), ('as4', 'bb4'), ('b4', 'b4'), 
            ('c5', 'c5'), ('cs5', 'db5'), ('d5', 'd5'), ('ds5', 'eb5'), ('e5', 'e5'), ('f5', 'f5'), 
            ('fs5', 'gb5'), ('g5', 'g5'), ('gs5', 'ab5'), ('a5', 'a5'), ('as5', 'bb5'), ('b5', 'b5'), 
            ('c6', 'c6'), ('cs6', 'db6'), ('d6', 'd6'), ('ds6', 'eb6'), ('e6', 'e6'), ('f6', 'f6'), 
            ('fs6', 'gb6'), ('g6', 'g6'), ('gs6', 'ab6'), ('a6', 'a6'), ('as6', 'bb6'), ('b6', 'b6'), 
            ('c7', 'c7'), ('cs7', 'db7'), ('d7', 'd7'), ('ds7', 'eb7'), ('e7', 'e7'), ('f7', 'f7'), 
            ('fs7', 'gb7'), ('g7', 'g7'), ('gs7', 'ab7'), ('a7', 'a7'), ('as7', 'bb7'), ('b7', 'b7'), 
            ('c8', 'c8'), ('cs8', 'db8'), ('d8', 'd8'), ('ds8', 'eb8')]

# fundamental frequencies of notes
freq_lut = [16, 17, 18, 19, 20, 21, 23, 24, 25, 27, 29, 30, 
            32, 34, 36, 38, 41, 43, 46, 49, 51, 55, 58, 61, 
            65, 69, 73, 77, 82, 87, 92, 98, 103, 110, 116, 
            123, 130, 138, 146, 155, 164, 174, 185, 196, 207, 220, 
            233, 246, 261, 277, 293, 311, 329, 349, 369, 392, 415, 
            698, 739, 783, 830, 880, 932, 987, 1046, 1108, 1174, 1244, 
            1318, 1396, 1479, 1567, 1661, 1760, 1864, 1975, 2093, 2217, 2349, 
            2489, 2637, 2793, 2959, 3135, 3322, 3520, 3729, 3951, 4186, 4434, 
            4698, 4978]

# return the peaks in the frequency domain
def peak_freqs(fft, **kwargs):
    peaks,_ = find_peaks(fft, **kwargs)
    return peaks

def identify_peaks(fft_chunks, **kwargs): 
    return [peak_freqs(chunk, **kwargs) for chunk in fft_chunks]

# map peak frequency to closest note
def freq_to_note(freq):
    index = 0
    while index < len(freq_lut) and freq_lut[index] < freq:
        index += 1

    if index == len(freq_lut):
        return ('',)

    if freq_lut[index] - freq > freq - freq_lut[index-1]:
        index -= 1
    return note_lut[index]

# convert all chunks' peaks to notes
def identify_notes(peak_chunks):
    melody = []
    for peak_chunk in peak_chunks:
        chord = []
        for peak in peak_chunk:
            chord.append(freq_to_note(peak))
        melody.append(chord)
    return melody
        
if __name__ == "__main__":
    from scipy.misc import electrocardiogram as ec
    peaks = peak_find(ec()[2000:4000])
    #notes = note_map(peaks)
    print(peaks)

