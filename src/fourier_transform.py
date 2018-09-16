import numpy as np
import scipy.fftpack

def fourier(audio, chunk_size=2500):
	chunks = [audio[i:i+chunk_size] for i in range(len(audio)//chunk_size)]
	return [np.absolute(np.fft.rfft(chunk)) for chunk in chunks] 

if __name__ == '__main__':    
    noise = np.fromstring(open("noise", "r").read()[1:-2], sep=", ")
    noise_fft = fourier(noise)
    open("noise_fft", "w").write(str(noise_fft[0].tolist()))
    
    sing = np.fromstring(open("sing", "r").read()[1:-2], sep=", ")
    sing_fft = fourier(sing)
    open("sing_fft", "w").write(str(sing_fft[0].tolist()))



