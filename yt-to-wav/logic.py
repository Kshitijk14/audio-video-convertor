import os
from yt_dlp import YoutubeDL

def download_youtube_video_as_wav(youtube_url, output_path="../output"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Downloaded and converted to WAV in: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

youtube_url = input("Enter the YouTube URL: ")
download_youtube_video_as_wav(youtube_url)
