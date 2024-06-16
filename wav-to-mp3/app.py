import customtkinter as ctk
from pydub import AudioSegment
import os
import tkinter as tk
from tkinter import filedialog, messagebox

class AudioConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Converter")

        # Set customtkinter appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create main frame with customtkinter style
        self.frame = ctk.CTkFrame(master=root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Conversion type selection
        self.conversion_type = tk.StringVar(value="wav_to_mp3")
        self.label_conversion = ctk.CTkLabel(master=self.frame, text="Select Conversion Type:", font=("Helvetica", 14, "bold"))
        self.label_conversion.grid(row=0, column=0, pady=5, padx=10, sticky="w")

        self.radio_wav_to_mp3 = ctk.CTkRadioButton(master=self.frame, text="WAV to MP3", variable=self.conversion_type, value="wav_to_mp3")
        self.radio_wav_to_mp3.grid(row=0, column=1, pady=5, padx=10, sticky="w")

        self.radio_mp3_to_wav = ctk.CTkRadioButton(master=self.frame, text="MP3 to WAV", variable=self.conversion_type, value="mp3_to_wav")
        self.radio_mp3_to_wav.grid(row=0, column=2, pady=5, padx=10, sticky="w")

        # File input path
        self.label_input_path = ctk.CTkLabel(master=self.frame, text="Select File to Convert:", font=("Helvetica", 14, "bold"))
        self.label_input_path.grid(row=1, column=0, pady=5, padx=10, sticky="w")
        self.entry_input_path = ctk.CTkEntry(master=self.frame, placeholder_text="Browse file to convert", font=("Helvetica", 12))
        self.entry_input_path.grid(row=1, column=1, pady=5, padx=10, sticky="w")
        self.button_browse_input = ctk.CTkButton(master=self.frame, text="Browse", command=self.browse_input_file)
        self.button_browse_input.grid(row=1, column=2, pady=5, padx=10, sticky="w")

        # Output path
        self.label_output_path = ctk.CTkLabel(master=self.frame, text="Select Output Path:", font=("Helvetica", 14, "bold"))
        self.label_output_path.grid(row=2, column=0, pady=5, padx=10, sticky="w")
        self.entry_output_path = ctk.CTkEntry(master=self.frame, placeholder_text="Browse save location", font=("Helvetica", 12))
        self.entry_output_path.grid(row=2, column=1, pady=5, padx=10, sticky="w")
        self.button_browse_output = ctk.CTkButton(master=self.frame, text="Browse", command=self.browse_output_path)
        self.button_browse_output.grid(row=2, column=2, pady=5, padx=10, sticky="w")

        # Convert button
        self.button_convert = ctk.CTkButton(master=self.frame, text="Convert", command=self.convert_audio)
        self.button_convert.grid(row=3, column=1, pady=20)

        # Status label
        self.status_label = ctk.CTkLabel(master=self.frame, text="", font=("Helvetica", 12))
        self.status_label.grid(row=4, column=0, columnspan=3, pady=10)

    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        self.entry_input_path.delete(0, tk.END)
        self.entry_input_path.insert(0, file_path)

    def browse_output_path(self):
        default_extension = ".mp3" if self.conversion_type.get() == "wav_to_mp3" else ".wav"
        file_types = [("MP3 files", "*.mp3"), ("WAV files", "*.wav")]
        save_path = filedialog.asksaveasfilename(defaultextension=default_extension, filetypes=file_types)
        self.entry_output_path.delete(0, tk.END)
        self.entry_output_path.insert(0, save_path)

    def convert_audio(self):
        input_file = self.entry_input_path.get()
        output_file = self.entry_output_path.get()

        if not input_file or not output_file:
            self.status_label.configure(text="Please select both input file and output path.")
            return

        try:
            if self.conversion_type.get() == "wav_to_mp3":
                audio = AudioSegment.from_wav(input_file)
                audio.export(output_file, format="mp3")
            else:
                audio = AudioSegment.from_mp3(input_file)
                audio.export(output_file, format="wav")

            self.status_label.configure(text=f"Conversion successful! Saved to: {output_file}")
        except Exception as e:
            self.status_label.configure(text=f"Error: {str(e)}")
            messagebox.showerror("Conversion Error", f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = AudioConverterApp(root)
    root.mainloop()
