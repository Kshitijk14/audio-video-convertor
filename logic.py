from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_mp3(youtube_url, output_path='output'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    downloaded_file = video.download(output_path)
    
    base, ext = os.path.splitext(downloaded_file)
    mp3_file = base + '.mp3'
    AudioSegment.from_file(downloaded_file).export(mp3_file, format='mp3')
    
    os.remove(downloaded_file)
    
    print(f"Downloaded and converted to MP3: {mp3_file}")

def convert_mp3_to_wav(mp3_file, output_path='output'):
    if not os.path.exists(mp3_file):
        print(f"File {mp3_file} does not exist.")
        return
    
    wav_file = os.path.splitext(mp3_file)[0] + '.wav'
    AudioSegment.from_mp3(mp3_file).export(wav_file, format='wav')
    
    print(f"Converted to WAV: {wav_file}")

def convert_wav_to_mp3(wav_file, output_path='output'):
    if not os.path.exists(wav_file):
        print(f"File {wav_file} does not exist.")
        return
    
    mp3_file = os.path.splitext(wav_file)[0] + '.mp3'
    AudioSegment.from_wav(wav_file).export(mp3_file, format='mp3')
    
    print(f"Converted to MP3: {mp3_file}")

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=z0pzzkp85-Q'
download_youtube_video_as_mp3(youtube_url)

mp3_file = 'output/example.mp3'
convert_mp3_to_wav(mp3_file)

wav_file = 'output/example.wav'
convert_wav_to_mp3(wav_file)
