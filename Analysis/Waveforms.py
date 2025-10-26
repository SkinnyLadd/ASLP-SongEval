import librosa, librosa.display, matplotlib.pyplot as plt

y, sr = librosa.load('../Data/mp3/21.mp3')
plt.figure(figsize=(25,4))
librosa.display.waveshow(y, sr=sr)
plt.title('Waveform')
plt.savefig('Plots/waveform_21.pdf')

