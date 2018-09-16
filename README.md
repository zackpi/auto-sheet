pip install -r pip_reqs
sudo apt install lilypond
python3 main.py

As you can see in the entry file "main.py", there are four modules 
1) Take a recording and convert it to a flat array of amplitudes
2) Split the array into chunks, and apply Fourier Transform onto each chunk
3) Identify the prominent peaks from each chunk, then identify what notes they are 
4) Plot the score programmatically from the note array we generated using LilyPond




