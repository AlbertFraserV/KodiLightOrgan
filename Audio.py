import librosa
import numpy as np

class Audio:
    def __init__(self, audio_file):
        self.time_series, self.sample_rate = librosa.load("Alone.mp3")
        self.stft = np.abs(librosa.stft(self.time_series, hop_length=512, n_fft=2048*4))
        self.spectrogram = librosa.amplitude_to_db(self.stft, ref=np.max)
        self.frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # getting an array of frequencies
