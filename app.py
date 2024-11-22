from flask import Flask, render_template, request, redirect, url_for, flash
import os
from yt_dlp import YoutubeDL

app = Flask(__name__)
app.secret_key = "your_secret_key"  # For flashing messages
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'output')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def download_youtube_video_as_wav(youtube_url, output_path=UPLOAD_FOLDER):
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
        return "Download Successful!"
    except Exception as e:
        return f"Error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")
        if not youtube_url:
            flash("Please enter a valid YouTube URL.", "danger")
            return redirect(url_for("index"))

        message = download_youtube_video_as_wav(youtube_url)
        if "Error" in message:
            flash(message, "danger")
        else:
            flash(message, "success")
        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
