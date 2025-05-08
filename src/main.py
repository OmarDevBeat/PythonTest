from pytube import YouTube
import librosa
import numpy as np


def download_audio_from_youtube(url):
    # Descargar audio del video de YouTube
    print(f"Descargando audio de: {url}")
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(filename="audio.mp4")
    return "audio.mp4"

def get_video_info(url):
    # Obtener información del video de YouTube
    yt = YouTube(url)
    title = yt.title
    description = yt.description
    length = yt.length  # en segundos
    views = yt.views

    print(f"Título: {title}")
    print(f"Descripción: {description[:100]}...")  # Mostrar solo los primeros 100 caracteres
    print(f"Duración: {length} segundos")
    print(f"Vistas: {views}")


def analyze_audio(file_path):
    # Cargar archivo de audio
    print(f"Cargando audio desde: {file_path}")
    y, sr = librosa.load(file_path, sr=None)

    # Extraer tempo y frames de beat
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # Extraer características de cromatografía
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)

    print(f"Tempo: {tempo} BPM")
    print(f"Chroma shape: {chroma.shape}")

    return tempo, chroma


if __name__ == "__main__":
    # Enlace del video de YouTube
    youtube_url = "https://www.youtube.com/watch?v=8ZP5eqm4JqM"

    # Obtener información del video
    get_video_info(youtube_url)

    # Descargar y analizar audio
    # audio_file = download_audio_from_youtube(youtube_url)
    # analyze_audio(audio_file)
