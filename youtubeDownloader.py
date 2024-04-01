import os
import threading
import tkinter as tk
from pytube import YouTube

def main():
    url = tk_entry.get()

    if "youtube.com" not in url:
        status_label.config(text="Enter a valid url", fg="red", font={"Arial", 15})
    else:
        status_label.config(text="Downloading...", fg="red")
        threading.Thread(target=Download_Thread, args=(url,)).start()

def Download_Thread(url):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    download_path = "C:\\Users\\outhman\\Desktop"
    stream.download(download_path)
    status_label.config(text="The video has been downloaded", fg="green")


root = tk.Tk()
root.title("Youtube Video Downloader")

tk_label = tk.Label(root, text="Video downloader")

tk_label.pack()

tk_entry = tk.Entry(root, width=70)

tk_entry.pack()

tk_button = tk.Button(root, text="Download", fg="blue", command=main)

tk_button.pack()

status_label = tk.Label(root, text="")

status_label.pack()


root.mainloop()