from tkinter import *
from tkinter import messagebox
from backend import YoutubeDownloader 


# TODO: Add download with audio, video and both options
class GUI:

    __window: Tk
    __x_axis: int = 180
    __user_youtube_url: str

    def __init__(self):
        self.__window = Tk()
        self.__window.resizable(0,0)
        self.__window.title('Youtube Video Downloader')
        self.__window.geometry('600x600')

        self.__user_youtube_url = StringVar()

        Label(self.__window, 
                text = 'YouTube URL:', 
                font='arial').place(x=self.__x_axis, y=200)

        Entry(self.__window, 
                width=40,
                textvariable=self.__user_youtube_url).place(x=self.__x_axis, y=230)

        Button(self.__window,
                text='Download', 
                font='arial', 
                bg='gray', 
                fg='white',
                padx=15,
                command=self.button_download_event).place(x=self.__x_axis, y=260)

    def button_download_event(self):
        try:
            if not self.__user_youtube_url.get():
                raise Exception('The URL field cannot be empty!')
            youtube_downloader = YoutubeDownloader(
                    self.__user_youtube_url.get(),
                    has_audio=True,
                    has_video=False,
                    custom_filename='')
            youtube_downloader.download_youtube_video()

            messagebox.showinfo(title='Success', message='Video was successfully downloaded!')
        except Exception as error:
            messagebox.showerror(title='error', message=str(error))

    def initialize(self):
        self.__window.mainloop()

gui = GUI()
gui.initialize()

