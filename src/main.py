# src/main.py
import librosa
import numpy as np

def analyze_audio(file_path):
    # Load audio file
    y, sr = librosa.load(file_path, sr=None)
    
    # Extract tempo and beat frames
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    
    # Extract chroma features
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    
    print(f'Tempo: {tempo} BPM')
    print(f'Chroma shape: {chroma.shape}')
    
    return tempo, chroma

if __name__ == "__main__":
    # Example audio file path
    audio_file = 'path_to_your_audio_file.mp3'
    analyze_audio(audio_file)
