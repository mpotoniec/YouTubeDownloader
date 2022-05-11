from pytube import YouTube
import pytube

import video_downloader
import audio_downloader

def load_file(link):
    try:
        you_tube_object = YouTube(link)

    except pytube.exceptions.RegexMatchError:
        print('ERROR! Cannot load video')
        return -1

    else: return you_tube_object


def download_file(you_tube_object, object_type, res, codec):
    if object_type == 'video': video_downloader.download_video(you_tube_object, res)
    elif object_type == 'audio': audio_downloader.download_audio(you_tube_object, codec, False)
    return 0

#moviepy
#audioconverter 