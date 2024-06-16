import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import sounddevice as sd

sampling_rate, data = wav.read('../resource/voice1.wav')
print('sampling rate:', sampling_rate)
print('data type:', data.dtype)
print('data shape:', data.shape)
N, no_channels = data.shape
print('signal length:', N)
channel0 = data[:, 0]
channel1 = data[:, 1]

def save_wav(filename, data, samplerate):
    wav.write(filename, samplerate, data)   

def play_audio(data, samplerate):
    sd.play(data, samplerate)
    sd.wait()
    
def volume_Increment(data, ratio):
    return data[:,:] * ratio

def main():
    linear_data = data
    save_wav('linear_pcm.wav', linear_data, sampling_rate)
    play_audio(linear_data, sampling_rate)
    print('Playing Linear PCM')
    
    incremented_data = volume_Increment(data, 2)
    play_audio(incremented_data, sampling_rate)
    save_wav('X2.wav', incremented_data, sampling_rate)
    
    incremented_data = volume_Increment(data, 4)
    play_audio(incremented_data, sampling_rate)
    save_wav('X4.wav', incremented_data, sampling_rate)
    
if __name__ == "__main__":
    main()