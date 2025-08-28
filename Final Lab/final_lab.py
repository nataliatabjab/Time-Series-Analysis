import librosa
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('/Users/nataliatabja/opt/anaconda3/lib/python3.9/site-packages')

comfortably_numb = 'Comfortably Numb.mp3'
audio_data, sampling_rate = librosa.load(comfortably_numb)

# Create time array
time = np.arange(0, len(audio_data)) / sampling_rate

# Plot audio data
plt.figure(figsize=(10, 4))
plt.plot(time, audio_data, color='b')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal Over Time')
plt.show()
