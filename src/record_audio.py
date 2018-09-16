# input: builtin microphone 

def flatten_array(array): 
	output = [] 
	for elem in array: 
		output.append(elem[0])
	return output

def record(duration=5, fs=40000):
	import sounddevice as sd
	recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
	sd.wait()
	return flatten_array(recording)
 
if __name__ == "__main__":
	arr = record(duration=1/16)
	print(arr)
