from tkinter import *
from backend import download_youtube_video 


window = Tk()
window.resizable(0,0)
window.title('Youtube Downloader')
window.geometry('1024x728')

youtube_download_link = StringVar()

Label(window, 
        text = 'Insert your video URL here:', font='arial').place(x=180, y=200)

Entry(window, width=20, textvariable=youtube_download_link).place(x=180, y=240)

def trigger_download():
    download_youtube_video(
            youtube_video_link=youtube_download_link.get(), 
            mime_type='audio/mp4', 
            adaptive=False)

Button(window,
        text = 'Download', 
        font = 'arial', 
        bg='green', 
        fg='white',
        padx=2,
        command=trigger_download).place(x=180, y=270)

window.mainloop()

