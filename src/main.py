from record_audio import * 
from fourier_transform import * 
from identify_notes import * 
from build_score import * 

import matplotlib.pyplot as plt

def show_recording(rec):
    plt.plot(rec)
    plt.show()

def show_transformed(fft):
    for chunk in fft:
        plt.plot(chunk)
        plt.show()

def show_peaks(ffts, peaks):
    for fft_chunk, peak_chunk in list(zip(ffts, peaks))[::16]:
        plt.plot(fft_chunk)
        plt.plot(peak_chunk, fft_chunk[peak_chunk], "x")
        plt.show()

# record audio 
recording = record(duration=5) 
print('recording =', recording[:10])
print('length =', len(recording))
show_recording(recording)

# fourier transform 
transformed = fourier(recording) 
print('transformed =', transformed[:10])
print('length =', len(transformed))
# show_transformed(transformed)

# identify peak frequencies
peaks = identify_peaks(transformed, prominence=40)
show_peaks(transformed, peaks)

# convert to sheet music
notes = identify_notes(peaks)
print('notes =', notes)
print('length =', len(notes))
display(notes) # transcribe notes


 
