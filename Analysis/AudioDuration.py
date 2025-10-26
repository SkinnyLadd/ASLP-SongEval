import librosa, librosa.display, os, matplotlib.pyplot as plt

durations = []

# slicing files upto the 30th song
files = sorted(os.listdir('../Data/mp3'))

for f in files: # scanning length and updating array
    path = os.path.join('../Data/mp3', f)
    y, sr = librosa.load(path)
    durations.append(len(y)/sr)

plt.figure(figsize=(8, 4))
plt.hist(durations, bins=20)
plt.title('Audio Duration Distribution (First 30 Songs)')
plt.xlabel('Duration (seconds)')
plt.ylabel('Count')
plt.tight_layout()

plt.savefig('Plots/duration_hist_all.pdf')
