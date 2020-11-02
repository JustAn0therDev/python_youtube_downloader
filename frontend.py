from utils import Utils
from tkinter.ttk import Combobox
from backend import YoutubeDownloader 
from streamoptions import StreamOptions
from tkinter import Tk, StringVar, Label, Entry, Button, messagebox


class GUI:

    __window: Tk
    __x_axis: int = 180
    __user_youtube_url: str

    def __init__(self):
        self.__window = Tk()
        self.__window.resizable(0,0)
        self.__window.title('Youtube Video Downloader')
        self.__window.geometry('700x700')

        self.__user_youtube_url = StringVar()
        self.__stream_quality = StringVar()
        self.__stream_option = StringVar()
        self.__custom_filename = StringVar()
        self.__directory = StringVar()

        self.create_labels()
        self.create_buttons()
        self.create_entries()
        self.create_comboboxes()

    def create_labels(self) -> None:
        Label(self.__window, 
                text = 'YouTube URL:', 
                font='arial').place(x=self.__x_axis, y=200)
        Label(self.__window, 
                text = 'Select stream quality:', 
                font='arial').place(x=self.__x_axis, y=260)
        Label(self.__window,
                text='Select stream option:',
                font='arial').place(x=self.__x_axis, y=320)
        Label(self.__window,
                text='Insert a custom file name if you want to:',
                font='arial').place(x=self.__x_axis, y=380)
        Label(self.__window,
                text='Insert the desired directory from the root:',
                font='arial').place(x=self.__x_axis, y=450)

    def create_buttons(self) -> None:
        Button(self.__window,
                text='Download', 
                font='arial', 
                bg='gray', 
                fg='white',
                padx=15,
                command=self.download_video).place(x=self.__x_axis, y=520)

    def create_entries(self) -> None:
        Entry(self.__window, 
                width=40,
                textvariable=self.__user_youtube_url).place(x=self.__x_axis, y=230)
        Entry(self.__window, 
                width=40,
                textvariable=self.__custom_filename).place(x=self.__x_axis, y=410)
        Entry(self.__window, 
                width=40,
                textvariable=self.__directory).place(x=self.__x_axis, y=480)

    def create_comboboxes(self) -> None:
        self.__res_combobox = Combobox(self.__window, 
                values=['Auto', '144p', '240p', '360p', '480p', '720p', '1080p'], 
                state='readonly', textvariable=self.__stream_quality).place(x=self.__x_axis, y=290)
        self.__stream_combobox = Combobox(self.__window,
                values=[StreamOptions.ONLY_VIDEO, StreamOptions.ONLY_AUDIO, StreamOptions.VIDEO_AND_AUDIO],
                state='readonly', textvariable=self.__stream_option).place(x=self.__x_axis, y=350)

    def download_video(self) -> None:
        try:
            self.validate_required_values()
            youtube_downloader = YoutubeDownloader(
                    self.__user_youtube_url.get(),
                    self.__stream_option.get(),
                    self.__stream_quality.get(),
                    self.__custom_filename.get(),
                    self.__directory.get())

            youtube_downloader.download_youtube_video()
            messagebox.showinfo(title='Success', message='Video was successfully downloaded!')
        except Exception as error:
            messagebox.showerror(title='error', message=str(error))

    def validate_required_values(self) -> None:
            if not self.__user_youtube_url.get():
                raise Exception('The URL field cannot be empty!')

            if not self.__stream_quality.get():
                raise Exception('Select a stream quality')

            if not self.__stream_option.get():
                raise Exception('Select a stream option')

    def initialize(self) -> None:
        self.__window.mainloop()

gui = GUI()
gui.initialize()
