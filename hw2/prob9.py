#!/usr/bin/env python
import numpy as np
import wave
import struct

file = '10612150.wav'
frq = {'C4': 261.6, 'D4': 293.7, 'E4': 329.6,
       'F4': 349.2, 'G4': 392.0, 'A4': 440.0,
       'B4': 493.9, 'quiet': 0}

chorus = {'C': ['C4', 'E4', 'G4'],
          'F': ['C4', 'F4', 'A4'],
          'G': ['D4', 'G4', 'B4'],
          'n': []} # null

QAQ = ['C4', 'C4', 'G4', 'G4', 'A4', 'A4', 'G4', 'quiet',
       'F4', 'F4', 'E4', 'E4', 'D4', 'D4', 'C4', 'quiet',
       'G4', 'G4', 'F4', 'F4', 'E4', 'E4', 'D4', 'quiet',
       'G4', 'G4', 'F4', 'F4', 'E4', 'E4', 'D4', 'quiet',
      ]
chorusQAQ = ['C', 'n', 'C', 'n','F', 'n', 'C', 'n',
            'F', 'n', 'C', 'n', 'G', 'n', 'C', 'n',
            'C', 'n', 'F', 'n', 'C', 'n', 'G', 'n',
            'C', 'n', 'F', 'n', 'C', 'n', 'C', 'n',
        ]

amplitude = 5000
frequency = 440
duration = 1
fs = 44100
num_samples = duration * fs

num_channels = 1
sampwidth = 2
num_frames = num_samples
comptype = 'NONE'
compname = "not compressed"

wav_file = wave.open(file, 'w')
wav_file.setparams((num_channels, sampwidth, fs, num_frames, comptype, compname))

t = np.linspace(0, duration, num_samples, endpoint=False)

for i in range(0, 2):
    for note in list(zip(QAQ, chorusQAQ)):
        x = amplitude * np.exp(-t) * np.cos(2 * np.pi * frq[note[0]] * t)

        for note_chorus in chorus[note[1]]:
            x += amplitude * np.exp(-t) * np.cos(2 * np.pi * frq[note_chorus] * t)

        for s in x:
            wav_file.writeframes(struct.pack('h', int(s)))

wav_file.close()

