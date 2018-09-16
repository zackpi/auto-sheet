import numpy as np
import scipy.fftpack

def fourier(audio, chunk_size=2500):
	chunks = [audio[i:i+chunk_size] for i in range(len(audio)//chunk_size)]
	return [np.fft.rfft(chunk) for chunk in chunks] 

if __name__ == '__main__':
	audio = []
	fourier(audio)



