import pytube
import os

import YouTubeDownloader.src.video_to_audio_converter as video_to_audio_converter


def download_audio(youtube_object, download_path, codec='mp3', audio_for_video = False) -> None: 
    streams = youtube_object.streams.filter(only_audio=True)
    stream_to_download = None
    quality = 0
    for stream in streams:
        if int(stream.abr.split('k')[0]) > quality:
            stream_to_download = stream
            quality = int(stream.abr.split('k')[0])

    if audio_for_video == True:
        try:
            downloaded_file_name = streams.get_by_itag(stream_to_download.itag).download(f"{os.environ['PYTHONPATH']}/YouTubeDownloader/src/VideoOperationsFile/Audio/")

        except pytube.exceptions.LiveStreamError:
            print('ERROR! Live stream cannot be downloaded')
            return -1
            
        else: return downloaded_file_name

    elif audio_for_video == False:
        try:
            downloaded_file_name = streams.get_by_itag(stream_to_download.itag).download(f"{os.environ['PYTHONPATH']}/YouTubeDownloader/src/VideoOperationsFile/")

        except pytube.exceptions.LiveStreamError:
            print('ERROR! Live stream cannot be downloaded')
            return -1

        else: video_to_audio_converter.convert_video_to_audio(downloaded_file_name, codec, download_path)

    print(f'Downloaded audio to path: {download_path}')
    return 0


#print(f"Audio itag : {stream.itag} Quality : {stream.abr} ")
#print(stream_to_download)