from record_audio import * 
from fourier_transform import * 
from identify_notes import * 
from build_score import * 

# record audio 
recording = record(duration=5) 
# print('recording =', recording[250:500])

# fourier transform 
transformed = fourier(recording) 
# print('transformed =', transformed[250:500])

# identify_notes
peaks = identify_peaks(transformed)
notes = identify_notes(peaks)
print('notes =', notes)

# transcribe 
# display(notes)


 