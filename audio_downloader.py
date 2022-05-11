import pytube

import video_to_audio_converter

def download_audio(youtube_object, codec='mp3', audio_for_video = False) -> None: 
    streams = youtube_object.streams.filter(only_audio=True)
    stream_to_download = None
    quality = 0
    for stream in streams:
        if int(stream.abr.split('k')[0]) > quality:
            stream_to_download = stream
            quality = int(stream.abr.split('k')[0])

    if audio_for_video == True:
        try:
            downloaded_file_name = streams.get_by_itag(stream_to_download.itag).download('VideoOperationsFile/Audio/')

        except pytube.exceptions.LiveStreamError:
            print('ERROR! Live stream cannot be downloaded')
            return -1
            
        else: return downloaded_file_name

    elif audio_for_video == False:
        try:
            downloaded_file_name = streams.get_by_itag(stream_to_download.itag).download('VideoOperationsFile/')

        except pytube.exceptions.LiveStreamError:
            print('ERROR! Live stream cannot be downloaded')
            return -1

        else: video_to_audio_converter.convert_video_to_audio(downloaded_file_name, codec)

    print('Done')
    return 0


#print(f"Audio itag : {stream.itag} Quality : {stream.abr} ")
#print(stream_to_download)