from pytube import YouTube, Stream


class YoutubeDownloader:
    __youtube_video_link: str
    __stream_option: str
    __stream_quality: str
    __directory: str
    __custom_filename: str

    def __init__(self, youtube_video_link: str, stream_option: str, stream_quality: str, custom_filename: str,
                 directory: str):
        self.__youtube_video_link = youtube_video_link
        self.__stream_option = stream_option
        self.__stream_quality = stream_quality
        self.__custom_filename = custom_filename
        self.__directory = directory

    def download_youtube_video(self) -> None:
        youtube_video = YouTube(self.__youtube_video_link)
        stream = self.__get_stream_object(youtube_video)

        self.__download_video_from_stream(stream)

    def __get_stream_object(self, youtube_video: YouTube) -> Stream:
        stream_with_chosen_quality: Stream

        if self.__stream_option == 'Only audio':
            stream_with_chosen_quality = youtube_video.streams \
                .filter(only_audio=True).first()
        elif self.__stream_option == 'Only video':
            stream_with_chosen_quality = youtube_video.streams \
                .filter(only_video=True, res=self.__stream_quality).first()
        elif self.__stream_option == 'Video and audio':
            stream_with_chosen_quality = youtube_video.streams \
                .filter(progressive=True, res=self.__stream_quality).first()
        else:
            raise Exception('Stream option not implemented')

        if not stream_with_chosen_quality:
            raise Exception('Video quality not found!')

        return stream_with_chosen_quality

    def __download_video_from_stream(self, stream: Stream) -> None:
        if self.__custom_filename and not self.__directory:
            stream.download(filename=self.__custom_filename)
        elif self.__directory and not self.__custom_filename:
            stream.download(output_path=self.__directory)
        elif self.__custom_filename and self.__directory:
            stream.download(filename=self.__custom_filename, output_path=self.__directory)
        else:
            stream.download()
