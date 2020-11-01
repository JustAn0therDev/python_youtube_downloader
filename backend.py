from pytube import YouTube
from utils import Utils
from streamoptions import StreamOptions

class YoutubeDownloader:

    __youtube_video_link: str
    __stream_option: str
    __stream_quality: str
    __directory: str
    __custom_filename: str

    def __init__(self, youtube_video_link: str, stream_option: str, stream_quality: str, custom_filename: str, directory: str):
        self.__youtube_video_link = youtube_video_link
        self.__stream_option = stream_option
        self.__stream_quality = stream_quality
        self.__custom_filename = custom_filename
        self.__directory = directory

    def download_youtube_video(self) -> bool:
        download_was_successful = False
        youtube_video = YouTube(self.__youtube_video_link)
        video_stream = self.get_stream_object(youtube_video)

        if not video_stream:
            raise Exception('Video quality not found!')

        self.download_video_from_stream(video_stream)
        download_was_successful = True
        
        return download_was_successful

    def get_stream_object(self, youtube_video) -> any:
        if self.__stream_option == StreamOptions.ONLY_AUDIO:
            stream_to_download = youtube_video.streams\
            .filter(only_audio=True).first()
        elif self.__stream_option == StreamOptions.ONLY_VIDEO:
            stream_to_download = youtube_video.streams\
            .filter(only_video=True, res=self.__stream_quality).first()

            """ Progressive is the old way of downloading video stream data.
                It downloads both audio and video, unlike adaptive where
                we can download specific types of data from the current stream
            """
        else:
            stream_to_download = youtube_video.streams\
            .filter(progressive=True, res=self.__stream_quality).first()

        return stream_to_download

    def download_video_from_stream(self, video_stream: any) -> None:
        if self.__custom_filename and not self.__directory:
            video_stream.download(filename=self.__custom_filename)
        elif self.__directory and not self.__custom_filename: 
            video_stream.download(output_path=self.__directory)
        elif self.__custom_filename and self.__directory:
            video_stream.download(filename=self.__custom_filename, output_path=self.__directory)
        else:
            video_stream.download()

