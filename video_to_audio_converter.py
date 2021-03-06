import moviepy.editor as mp
import os

def convert_video_to_audio(video_name, codec, download_path) -> None:
    audio_name = video_name.split('VideoOperationsFile/')
    #audio_name = audio_name[0] + download_path + audio_name[1]
    #audio_name = audio_name.split('.')[0] + '.' + codec
    audio_name = download_path + audio_name[1] + '.' + codec

    file_to_convert = mp.AudioFileClip(video_name)
    file_to_convert .write_audiofile(audio_name)

    file_to_convert .close()

    os.remove(video_name)
