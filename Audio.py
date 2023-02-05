import librosa
import numpy as np

class Audio:
    def __init__(self, audio_file):
        self.time_series, self.sample_rate = librosa.load(audio_file)
        self.stft = np.abs(librosa.stft(self.time_series, hop_length=512, n_fft=2048*4))
        self.spectrogram = librosa.amplitude_to_db(self.stft, ref=np.max)
        self.frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  # getting an array of frequencies
        self.times = librosa.core.frames_to_time(np.arange(self.spectrogram.shape[1]), sr=self.sample_rate, hop_length=512, n_fft=2048*4)
        self.time_index_ratio = len(self.times)/self.times[len(self.times) - 1]
        self.frequencies_index_ratio = len(self.frequencies)/self.frequencies[len(self.frequencies)-1]
        self.min = self.spectrogram.min()

    def get_dbs(self, target_time, freq):
        # try:
        return self.spectrogram[int(freq*self.frequencies_index_ratio)-1][int(target_time*self.time_index_ratio)]
        # except IndexError:
        #     print("Caught!")
        #     return self.spectrogram[int(freq*self.frequencies_index_ratio)-1][int(target_time*self.time_index_ratio)]

audio = Audio("Alone.mp3")