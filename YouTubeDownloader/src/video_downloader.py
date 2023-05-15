import pytube
import os

import YouTubeDownloader.src.audio_downloader as audio_downloader
import YouTubeDownloader.src.video_audio_merge as video_audio_merge


def download_video(youtube_object, download_path, res='720p') -> None:
    streams = youtube_object.streams.filter(res=res)
    if len(streams) == 0: 
        print('ERROR: Video has not given resolution, Try other one')
        return -1
    
    my_streams = []
    for stream in streams:
        if stream.abr != None: my_streams.append(stream)

    stream_to_download = None
    quality = 0
    for stream in my_streams:
        if int(stream.abr.split('k')[0]) > quality:
            stream_to_download = stream
            quality = int(stream.abr.split('k')[0])

    if stream_to_download == None:
        try:
            video_name = streams.first().download(f"{os.environ['PYTHONPATH']}/YouTubeDownloader/src/VideoOperationsFile/Video/")
            audio_name = audio_downloader.download_audio(youtube_object=youtube_object, download_path=download_path, codec='mp3',audio_for_video=True)

        except pytube.exceptions.LiveStreamError:
            print('ERROR! Live stream cannot be downloaded')
            return -1

        else: 
            video_audio_merge.merge_video_audio(video_name, audio_name, download_path)
            print(f'Downloaded video to path: {download_path}')
            return 0 
    else:
        try: 
            streams.get_by_itag(stream_to_download.itag).download(download_path)
        
        except pytube.exceptions.LiveStreamError:
            print('ERROR! Live stream cannot be downloaded')
            return -1

        else: 
            print(f'Downloaded video to path: {download_path}')
            return 0 


#print(f"Audio itag : {stream.itag} Quality : {stream.abr} ")
#print(stream_to_download)