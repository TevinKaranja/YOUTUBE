from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video():
    try:
        yt = YouTube(url_entry.get())
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        save_path = filedialog.askdirectory()
        video.download(output_path=save_path)
        status_label.config(text="Video downloaded successfully!")
    except:
        status_label.config(text="Error downloading video.")

root = tk.Tk()
root.title("YouTube Video Downloader")

url_label = tk.Label(root, text="Enter YouTube video URL:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()