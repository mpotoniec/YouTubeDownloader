__version__ = '1.0.0'
print('YouTubeDownloader ver:', __version__)
import pytube
print('pytube ver:', pytube.__version__)
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
import datetime

import video_audio_downloader

from kivy.core.window import Window

class AppGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.you_tube_object = None

        self.title = ''
        self.author = ''
        self.description = ''
        self.length = ''
        self.publish_date = ''
        self.vievs = ''
        self.rating = ''
        self.age_restricted = ''

        self.resolution_type_var = '1080p'
        self.audio_type_var = 'mp3'

        self.cols = 2

        self.video_link_input = TextInput(multiline=False)

        self.video_loading_status = Label(text="YouTube link not loaded")
        self.video_link = Label(text="YouTube link")
        self.video_audio_download_status = Label(text='Video/Audio not downloaded')

        self.statistic_title_name = Label(text='Video title')
        self.statistic_title = Label(text=self.title)
        self.statistic_author_name = Label(text='Video author')
        self.statistic_author = Label(text=self.author)
        self.statistic_length_name = Label(text='Video length: hh:mm:ss')
        self.statistic_length = Label(text=self.length)
        self.statistic_publish_date_name = Label(text='Video publish date: yyyy:mm:dd')
        self.statistic_publish_date = Label(text=self.publish_date)

        self.load_video_button = Button(text='Load YouTube link')
        self.load_video_button.bind(on_press=self.load_video)
        self.toFile = Button(text='Save statistics to file')
        self.toFile.bind(on_press=self.save_statistics_to_file)
        self.download_video_button = Button(text='Download video')
        self.download_video_button.bind(on_press=self.download_video)
        self.download_audio_button = Button(text='Download audio')
        self.download_audio_button.bind(on_press=self.download_audio)

        self.resolution_type = Spinner(
            text='1080p',
            values=('1080p', '720p', '480p', '360p', '240p', '144p')
        )
        self.resolution_type.bind(text=self.set_resolution)
        self.audio_type = Spinner(
            text='mp3',
            values=('mp3','wav')
        )
        self.audio_type.bind(text=self.set_audio_type)

        self.load_video_grid = GridLayout()
        self.load_video_grid.cols = 2
        self.load_video_grid.add_widget(self.video_link)
        self.load_video_grid.add_widget(self.video_link_input)

        self.video_loading_status_grid = GridLayout()
        self.video_loading_status_grid.cols = 2
        self.video_loading_status_grid.add_widget(self.video_loading_status)
        self.video_loading_status_grid.add_widget(self.load_video_button)

        self.video_audio_download_grid = GridLayout()
        self.video_audio_download_grid.cols = 4
        self.video_audio_download_grid.add_widget(self.download_video_button)
        self.video_audio_download_grid.add_widget(self.resolution_type)
        self.video_audio_download_grid.add_widget(self.download_audio_button)
        self.video_audio_download_grid.add_widget(self.audio_type)

        self.video_audio_download_status_grid = GridLayout()
        self.video_audio_download_status_grid.cols = 1
        self.video_audio_download_status_grid.add_widget(self.video_audio_download_status)
        
        self.left_grid = GridLayout()
        self.left_grid.cols = 1
        self.left_grid.add_widget(self.load_video_grid)
        self.left_grid.add_widget(self.video_loading_status_grid)
        self.left_grid.add_widget(self.video_audio_download_grid)
        self.left_grid.add_widget(self.video_audio_download_status_grid)
        
        self.add_widget(self.left_grid)

        self.right_grid = GridLayout()
        self.right_grid.cols = 1
        self.right_grid.add_widget(self.toFile)
        self.right_grid.add_widget(self.statistic_title_name)
        self.right_grid.add_widget(self.statistic_title)
        self.right_grid.add_widget(self.statistic_author_name)
        self.right_grid.add_widget(self.statistic_author)
        self.right_grid.add_widget(self.statistic_length_name)
        self.right_grid.add_widget(self.statistic_length)
        self.right_grid.add_widget(self.statistic_publish_date_name)
        self.right_grid.add_widget(self.statistic_publish_date)

        self.add_widget(self.right_grid)


    def load_video(self, instance):
        if len(self.video_link_input.text) == 0:
            print('Add link to Video')
            return -1

        self.video_loading_status.text='YouTube link loading'
        you_tube_object_tmp = video_audio_downloader.load_file(self.video_link_input.text)

        if type(you_tube_object_tmp) == pytube.__main__.YouTube:
            print('link loaded')
            self.you_tube_object = you_tube_object_tmp
            self.title = str(self.you_tube_object.title)
            self.author = str(self.you_tube_object.author)
            self.description = str(self.you_tube_object.description)
            self.length = str(datetime.timedelta(seconds=self.you_tube_object.length))
            self.publish_date = str(self.you_tube_object.publish_date).split(' ')[0]
            self.vievs = str(self.you_tube_object.views)
            self.rating = str(self.you_tube_object.rating)
            self.age_restricted = str(self.you_tube_object.age_restricted)
            self.show_statistics()

            self.video_loading_status.text='YouTube link loaded'

        elif you_tube_object_tmp == -1:
            self.video_loading_status.text='Wrong link'
            print('ERROR! Wrong link')

    def save_statistics_to_file(self, instance):
        if self.you_tube_object == None:
            print('No video loaded!')
            return -1
        
        file = open('Statistics/'+self.title+'.txt','w')

        file.write('Title:\n')
        file.write(self.title)
        file.write('\n')
        file.write('\n')
        file.write('Author:\n')
        file.write(self.author)
        file.write('\n')
        file.write('\n')
        file.write('Description:\n')
        file.write(self.description)
        file.write('\n')
        file.write('\n')
        file.write('Length: hh:mm:ss\n')
        file.write(self.length)
        file.write('\n')
        file.write('\n')
        file.write('Publish date:\n')
        file.write(self.publish_date)
        file.write('\n')
        file.write('\n')
        file.write('Vievs:\n')
        file.write(self.vievs)
        file.write('\n')
        file.write('\n')
        file.write('Rating:\n')
        file.write(self.rating)
        file.write('\n')
        file.write('\n')
        file.write('Age restricted:\n')
        file.write(self.age_restricted)
        file.write('\n')
        file.write('\n')
      
        file.close()

    def show_statistics(self):
        self.statistic_title.text = self.title
        self.statistic_author.text = self.author
        self.statistic_length.text = self.length
        self.statistic_publish_date.text = self.publish_date

    def download_video(self, instance):
        if self.you_tube_object == None:
            print('No video loaded!')
            return -1

        self.video_audio_download_status.text = 'Downloading video in ' + self.resolution_type_var
        print('Downloading video in:', self.resolution_type_var)
        video_audio_downloader.download_file(self.you_tube_object, 'video', self.resolution_type_var, self.audio_type_var)
        self.video_audio_download_status.text = 'Video downloaded in ' + self.resolution_type_var

    def download_audio(self, instance):
        if self.you_tube_object == None:
            print('No video loaded!')
            return -1

        self.video_audio_download_status.text = 'Downloading audio in ' + self.audio_type_var
        print('Downloading audio in:', self.audio_type_var)
        video_audio_downloader.download_file(self.you_tube_object, 'audio', self.resolution_type_var, self.audio_type_var)
        self.video_audio_download_status.text = 'Audio downloaded in ' + self.audio_type_var

    def set_resolution(self, resolution_type, text):
        self.resolution_type_var = text

    def set_audio_type(self, audio_type, text):
        self.audio_type_var = text

class YouTubeDownloader(App):
    Window.size = (1500, 800)
    def build(self):
        super().build()
        return AppGridLayout()

if __name__ == '__main__':
    YouTubeDownloader().run()