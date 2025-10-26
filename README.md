# ASLP - SongEval (DEV)
## The following instructions are for the development version of the project. 

---

## Installation
I recommend using a virtual environment to install and manage the dependencies. Personally, I use [Anaconda](https://www.anaconda.com/products/individual).
A small guide for it is included below:

- After installing conda, open up the terminal in the project root and run the following commands
```bash
conda env create [env-name]
conda activate [env-name]
pip install -r requirements.txt
```
(you can choose any name for the environment)

- Alternatively, you can use the default python venv or any other venv for that matter - just make sure to run the last pip install command after activating the venv.
- ALSO MAKE SURE TO UPDATE THE REQUIREMENTS.TXT FILE WITH ANY NEW DEPENDENCIES THAT YOU ADD.

## Usage
- Data: Contains the dataset used for the project (limited to 100 songs).
- Analysis: Contains three python scripts for generating various analysis plots.
- More to be added.

## Project Structure
``` 
ASLP-SongEval/ 
│ 
├── Data/ # Dataset directory (SongEval benchmark) 
│ ├── mp3/ # Audio files (100 songs subset) 
│ ├── assets/ # Images and visual assets 
│ ├── metadata.jsonl # Song metadata and annotations  
│ └── README.md # Dataset documentation
│ 
├── Analysis/ # Exploratory Data Analysis scripts 
│ ├── AudioDuration.py # Duration distribution analysis 
│ ├── Spectograms.py # MFCC and spectrogram visualization 
│ └── Waveforms.py # Waveform plotting 
│ 
├── plots/ # Generated visualization outputs 
│ 
├── requirements.txt  
├── README.md  
└── .gitignore 
```

## Progress
### Assignment-1 (Analysis)
- [x] Waveforms
- [x] Spectograms (MFCCs)
- [x] Audio Durations
- [x] Report (EDA Summary + Plots)

### Assignment-2 (Pipelines)
- [ ] Data Loader & Preprocessing
- [ ] Baseline 1: CNN + MFCC Features
- [ ] Baseline 2: LSTM + Spectrograms
- [ ] Baseline 3: Wav2Vec2 / Whisper
- [ ] Training & Evaluation Pipeline
- [ ] Results & Comparison Tables
- [ ] Report (Pipeline & Results)

### Assignment-3 (Proposed Solution)
- [ ] Model Design (Improved Architecture / Augmentation)
- [ ] Experiment Setup & Hyperparameter Tuning
- [ ] Loss / Accuracy Curve Plots
- [ ] Confusion Matrix & Error Analysis
- [ ] Discussion, Limitations, Future Work
- [ ] Final ICASSP-style Report (Merged & Formatted)





