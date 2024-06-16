from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video_as_wav(youtube_url, output_path='output'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    yt = YouTube(youtube_url)
    video = yt.streams.filter(only_audio=True).first()
    downloaded_file = video.download(output_path)
    
    base, ext = os.path.splitext(downloaded_file)
    wav_file = base + '.wav'
    AudioSegment.from_file(downloaded_file).export(wav_file, format='wav')
    
    os.remove(downloaded_file)
    
    print(f"Downloaded and converted to WAV: {wav_file}")

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube URL: ")
    download_youtube_video_as_wav(youtube_url)
