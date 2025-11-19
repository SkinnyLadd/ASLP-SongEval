# ASLP - SongEval 

## Automatic Song Aesthetics Evaluation — ICASSP 2026 Challenge (Track 2)

This repository contains the development code for our semester project on **Automatic Song Aesthetics Evaluation**, aligned with the **ICASSP 2026 Grand Challenge (Track 2)**.

## Installation

### 1. Setup Environment

It is recommended to use a virtual environment. (We use **Anaconda**.)

```
conda env create -n songeval python=3.9
conda activate songeval
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

**Note:** Ensure you have **ffmpeg** installed on your system for audio processing.

## Project Structure


```
ASLP-SongEval/
│
├── Data/                     
│   ├── mp3/                  # (Not included) Main Audio files
│   ├── mp3-subset/           # Subset for quick testing
│   └── README.md             
│
├── Analysis/                 
│   ├── AudioDuration.py      
│   ├── Spectograms.py        
│   └── Waveforms.py          
│
├── Baselines/                
│   ├── Baseline_1.ipynb      # Random Forest + Librosa features
│   ├── Baseline_2.ipynb    # Wav2Vec2 (Speech-domain)
│   └── Baseline_3.ipynb     # AST (Audio-domain)
│
├── Proposed_Solution/        
│   ├── AST_Model.ipynb      # Final scalable pipeline + MERT training
│   └── generate_plots.py        
│
├── Reports/                  
│   ├── Assignment-1.pdf
│   ├── Assignment-2.pdf
│   └── Assignment-3.pdf
│
├── Utils/
│   └── DownloadDataset.py    
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Key Features & Progress

### Assignment 1: Problem Understanding (Completed)

- [x] Exploratory Data Analysis (Waveforms, Spectrograms)  
- [x] Dataset Statistics (Duration, Metadata)  
- [x] Initial Report  

### Assignment 2: Baseline Pipelines (Completed)

We implemented and compared three baseline models on a memory-constrained subset:

- [x] Baseline 1: Random Forest + hand-crafted features (MFCCs, Chroma, Contrast)  
- [x] Baseline 2: Wav2Vec2 (Speech-Pretrained) + regression head  
- [x] Baseline 3: Audio Spectrogram Transformer (AST) (Audio-Pretrained)  
- [x] Key Finding: Audio-domain pre-training (AST) significantly outperforms speech-domain pre-training (Wav2Vec2)

### Assignment 3: Proposed Solution (Completed)

We solved memory limitations and built a full scalable system:

- [x] Scalable Pipeline: Out-of-core processing that streams data, chunks audio on-the-fly, and serializes to JSONL — enabling full dataset training without RAM crashes.
- [x] Proposed Model: Implemented MERT (Music-Pretrained) and compared it against AST.
- [x] Result: AST achieved the highest performance (SRCC 0.837).

## Acknowledgments

- Dataset provided by ASLP-Lab for the ICASSP 2026 Challenge.  
- Models used: MIT/ast-finetuned-audioset-10-10-0.4593, facebook/wav2vec2-base, m-a-p/MERT-v1-95M.
