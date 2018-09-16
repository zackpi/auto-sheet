from record_audio import * 
from fourier_transform import * 
from identify_notes import * 
from build_score import * 

# record audio 
recording = record(duration=1) 
print('recording =', recording[:10])
print('length =', len(recording))

# fourier transform 
transformed = fourier(recording, ) 
print('transformed =', transformed[:10])
print('length =', len(transformed))

# identify_notes
peaks = identify_peaks(transformed, prominence=250)
notes = identify_notes(peaks)
print('notes =', notes)
print('length =', len(notes))

# transcribe 
display(notes)


 
