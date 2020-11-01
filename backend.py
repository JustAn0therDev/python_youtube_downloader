from pytube import YouTube
from utils import Utils

class YoutubeDownloader:

    __youtube_video_link: str
    __mime_type: str
    __has_audio: bool
    __has_video: bool
    __custom_filename: str

    # TODO: Create enumerator for video resolution
    def __init__(self, youtube_video_link: str, 
            has_audio: bool, 
            has_video: bool, 
            custom_filename: str):
        self.__youtube_video_link = youtube_video_link
        self.__has_audio = has_audio
        self.__has_video = has_video
        self.__custom_filename = custom_filename

    def download_youtube_video(self) -> bool:
        download_was_successful = False
        youtube_video = YouTube(self.__youtube_video_link)

        # TODO: Remove log. Maybe pass the window by reference to this class
        # and show messages on labels and message boxes.
        Utils.log_debug_message('Title: {}. Amount of views on video: {}'.format(
            youtube_video.title, 
            youtube_video.views))

        video_stream = self.get_stream_object(youtube_video)
        self.download_video_from_stream(video_stream)
        download_was_successful = True
        
        return download_was_successful

    def get_stream_object(self, youtube_video) -> any:
        if self.__has_audio and not self.__has_video:
            stream_to_download = youtube_video.streams\
            .filter(only_audio=True).first()
        elif self.__has_video and not self.__has_audio:
            stream_to_download = youtube_video.streams\
            .filter(only_video=True).first()
            # Progressive is the old way of downloading video stream data.
            # It downloads both audio and video, different from adaptive where
            # we can download specific parts of the media
        else:
            stream_to_download = youtube_video.streams\
            .filter(progressive=True).first()

        return stream_to_download

    def download_video_from_stream(self, video_stream: any) -> None:
        if self.__custom_filename:
            video_stream.download(filename=self.__custom_filename)
        else:
            video_stream.download()
