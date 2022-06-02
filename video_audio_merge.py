import moviepy.editor as mp
import os

def merge_video_audio(video_name, audio_name, download_path):
    output_name = video_name.split('VideoOperationsFile/Video/')
    #output_name = output_name[0] + download_path + output_name[1]
    output_name = download_path + output_name[1]

    video_file = mp.VideoFileClip(video_name)
    audio_file = mp.AudioFileClip(audio_name)

    video_audio_file = video_file.set_audio(audio_file)
    video_audio_file.write_videofile(output_name)

    video_file.close()
    audio_file.close()
    video_audio_file.close()

    os.remove(video_name)
    os.remove(audio_name)