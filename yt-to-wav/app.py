import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from pydub import AudioSegment
import os

class YouTubeToWavApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube to WAV Converter")

        # Set customtkinter appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create main frame with customtkinter style
        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # YouTube URL input
        self.label_url = ctk.CTkLabel(master=self.frame, text="YouTube URL:", font=("Helvetica", 14, "bold"))
        self.label_url.grid(row=0, column=0, pady=5, padx=10, sticky="w")
        self.entry_url = ctk.CTkEntry(master=self.frame, placeholder_text="Enter YouTube URL", font=("Helvetica", 12))
        self.entry_url.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        # Output path selection button and label
        self.label_output_path = ctk.CTkLabel(master=self.frame, text="Output Path:", font=("Helvetica", 14, "bold"))
        self.label_output_path.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        self.entry_output_path = ctk.CTkEntry(master=self.frame, placeholder_text="Browse or enter output directory", font=("Helvetica", 12))
        self.entry_output_path.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        self.button_browse_output = ctk.CTkButton(master=self.frame, text="Browse", command=self.browse_output_path)
        self.button_browse_output.grid(row=1, column=2, pady=5, padx=10, sticky="w")

        # Convert button
        self.button_convert = ctk.CTkButton(master=self.frame, text="Convert to WAV", command=self.download_and_convert)
        self.button_convert.grid(row=2, column=1, pady=20)

        # Status label
        self.status_label = ctk.CTkLabel(master=self.frame, text="", font=("Helvetica", 12))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

    def browse_output_path(self):
        output_path = filedialog.askdirectory()
        if output_path:
            self.entry_output_path.delete(0, tk.END)
            self.entry_output_path.insert(0, output_path)

    def download_and_convert(self):
        youtube_url = self.entry_url.get()
        output_path = self.entry_output_path.get()

        if not youtube_url:
            self.status_label.configure(text="Please enter a YouTube URL.")
            return

        if not output_path:
            output_path = 'output'

        try:
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            yt = YouTube(youtube_url)
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(output_path)

            base, ext = os.path.splitext(downloaded_file)
            wav_file = base + '.wav'
            AudioSegment.from_file(downloaded_file).export(wav_file, format='wav')

            os.remove(downloaded_file)

            self.status_label.configure(text=f"Downloaded and converted to WAV: {wav_file}")
        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = YouTubeToWavApp(root)
    root.mainloop()
