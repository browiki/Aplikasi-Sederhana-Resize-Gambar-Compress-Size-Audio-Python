import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from pydub import AudioSegment

class ImageAudioProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Audio Processor")

        # UI Elements
        self.btn_open_image = tk.Button(root, text="Open Image", command=self.open_image)
        self.btn_open_image.pack()

        self.btn_open_audio = tk.Button(root, text="Open Audio", command=self.open_audio)
        self.btn_open_audio.pack()

        self.btn_resize_image = tk.Button(root, text="Resize Image", command=self.resize_image)
        self.btn_resize_image.pack()

        self.btn_compress_audio = tk.Button(root, text="Compress Audio", command=self.compress_audio)
        self.btn_compress_audio.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image_path = file_path
            messagebox.showinfo("Info", "Image opened successfully!")

    def open_audio(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
        if file_path:
            self.audio_path = file_path
            messagebox.showinfo("Info", "Audio opened successfully!")

    def resize_image(self):
        try:
            image = Image.open(self.image_path)
            resized_image = image.resize((300, 300))  # Resize to 300x300, you can change as needed
            save_path = filedialog.asksaveasfilename(defaultextension=".png")
            resized_image.save(save_path)
            messagebox.showinfo("Info", "Image resized and saved successfully!")
        except AttributeError:
            messagebox.showerror("Error", "Please open an image first!")

    def compress_audio(self):
        try:
            audio = AudioSegment.from_file(self.audio_path)
            compressed_audio = audio.set_frame_rate(16000)  # Compress to 16 kHz, you can change as needed
            save_path = filedialog.asksaveasfilename(defaultextension=".mp3")
            compressed_audio.export(save_path, format="mp3")
            messagebox.showinfo("Info", "Audio compressed and saved successfully!")
        except AttributeError:
            messagebox.showerror("Error", "Please open an audio file first!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageAudioProcessorApp(root)
    root.mainloop()
