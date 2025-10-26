import librosa, librosa.display, matplotlib.pyplot as plt, numpy as np


y, sr = librosa.load('../Data/mp3/21.mp3')
D = librosa.amplitude_to_db(abs(librosa.stft(y)), ref=np.max) # USE ABSOLUTE FOR COMPARISON
# np.max normalizes the amplitude | converting to dB makes it so that 0dB is the loudest

plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', cmap='magma')
plt.title('Spectrogram (dB)')
plt.colorbar(format='%+2.0f dB')
plt.tight_layout()

plt.savefig('plots/mfcc_21_dB.pdf')