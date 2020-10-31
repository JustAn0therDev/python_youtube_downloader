from pytube import YouTube
from utils import log_debug_message, log_error_message


def download_youtube_video(youtube_video_link: str, mime_type: str, adaptive: bool) -> bool:
    download_was_successful = False
    try:
        youtube_video = YouTube(youtube_video_link)

        log_debug_message('Title: {}. Amount of views on video: {}'.format(
            youtube_video.title, 
            youtube_video.views))

        stream_to_download = youtube_video.streams.filter(adaptive=adaptive).filter(mime_type=mime_type).first()
        stream_to_download.download()
        download_was_successful = True
    except Exception as exception: 
        log_error_message(str(exception))
    
    return download_was_successful

