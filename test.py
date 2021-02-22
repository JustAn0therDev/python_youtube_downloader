import unittest
from os import path, remove
from unittest import TestCase
from backend import YoutubeDownloader
from enums.streamoption import StreamOption


class Tests(TestCase):
    __youtube_downloader: YoutubeDownloader

    def setUp(self):
        self.__youtube_downloader = YoutubeDownloader(
            youtube_video_link='https://www.youtube.com/watch?v=5IXQ6f6eMxQ', 
            stream_option=StreamOption.VIDEO_AND_AUDIO,
            stream_quality='360p', 
            custom_filename='test_video', 
            directory='')

    def test_video_should_exist_in_directory(self):
        video_directory = './test_video.mp4'
        self.__youtube_downloader.download_youtube_video()
        self.assertTrue(path.exists(video_directory))
        remove(video_directory) 


if __name__ == '__main__':
    unittest.main()
