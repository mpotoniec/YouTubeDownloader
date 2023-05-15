import datetime
import pytube
import os

import PyQt5.QtWidgets as qtw

import YouTubeDownloader.src.video_audio_downloader as video_audio_downloader


class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.project_path = os.environ['PYTHONPATH']
        self.you_tube_object = None

        self.resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']
        self.audio_types = ['mp3', 'wav', 'ogg']

        self.download_path = f"{os.environ['PYTHONPATH']}/YouTubeDownloader/Downloads/"

        self.title = ''
        self.author = ''
        self.description = ''
        self.length = ''
        self.publish_date = ''
        self.vievs = ''
        self.rating = ''
        self.age_restricted = ''

        self.setGeometry(0, 0, 750, 20)
        self.setLayout(qtw.QGridLayout())

        self.video_link_label = qtw.QLabel('Video link:')
        self.layout().addWidget(self.video_link_label)

        self.video_link_entry = qtw.QLineEdit()
        self.layout().addWidget(self.video_link_entry, 0,1)

        self.load_link_button = qtw.QPushButton('Load link', clicked = lambda: self.load_link())
        self.layout().addWidget(self.load_link_button, 0,3)

        self.choose_download_folder = qtw.QPushButton('Download folder', clicked = lambda: self.select_download_folder())
        self.layout().addWidget(self.choose_download_folder, 1,3)

        self.statistic_title_name = qtw.QLabel('Title:')
        self.statistic_title = qtw.QLabel(self.title)
        self.layout().addWidget(self.statistic_title_name , 2,0)
        self.layout().addWidget(self.statistic_title, 2,1)

        self.statistic_author_name = qtw.QLabel('Author:')
        self.statistic_author = qtw.QLabel(self.title)
        self.layout().addWidget(self.statistic_author_name , 3,0)
        self.layout().addWidget(self.statistic_author, 3,1)

        self.statistic_length_name = qtw.QLabel('Length:')
        self.statistic_length = qtw.QLabel(self.title)
        self.layout().addWidget(self.statistic_length_name , 4,0)
        self.layout().addWidget(self.statistic_length, 4,1)

        self.statistic_publish_date_name = qtw.QLabel('Publish date:')
        self.statistic_publish_date = qtw.QLabel(self.title)
        self.layout().addWidget(self.statistic_publish_date_name , 5,0)
        self.layout().addWidget(self.statistic_publish_date, 5,1)

        self.resolution = qtw.QComboBox()
        self.resolution.addItems(self.resolutions)
        self.layout().addWidget(self.resolution, 6,0)

        self.audio_type = qtw.QComboBox()
        self.audio_type.addItems(self.audio_types)
        self.layout().addWidget(self.audio_type, 7,0)

        self.download_type = qtw.QComboBox()
        self.download_type.addItems(['Video', 'Audio'])
        self.layout().addWidget(self.download_type, 8,0)

        self.load_link_button = qtw.QPushButton('Download', clicked = lambda: self.download())
        self.layout().addWidget(self.load_link_button, 9,0)
        self.load_link_button = qtw.QPushButton('Save to file', clicked = lambda: self.save_statistics_to_file())
        self.layout().addWidget(self.load_link_button, 10,0)

        self.video_audio_download_status = qtw.QLabel("Can't download: Video not loaded")
        self.layout().addWidget(self.video_audio_download_status, 9,1)

        self.statistics_status = qtw.QLabel("Can't save statistics: Video not loaded")
        self.layout().addWidget(self.statistics_status, 10,1)

    def select_download_folder(self):
        self.download_path = qtw.QFileDialog.getExistingDirectory(self, 'Select floder to download') + '/'
        if self.download_path == '/': self.download_path = 'Downloads/'

    def load_link(self):
        if len(self.video_link_entry.text()) == 0:
            print('Add link to Video')
            return -1

        you_tube_object_tmp = video_audio_downloader.load_file(self.video_link_entry.text())

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

            self.video_audio_download_status.setText('Download available')
            self.statistics_status.setText('Statistics save available')

        elif you_tube_object_tmp == -1:
            print('ERROR! Wrong link')

    def show_statistics(self):
        self.statistic_title.setText(self.title)
        self.statistic_author.setText(self.author)
        self.statistic_length.setText(self.length)
        self.statistic_publish_date.setText(self.publish_date)

    def download(self):
        if self.download_type.currentText() == 'Video': self.download_video()
        else: self.download_audio()

    def download_video(self):
        if self.you_tube_object == None:
            print('No video loaded!')
            return -1

        self.video_audio_download_status.setText('Downloading video in ' + self.resolution.currentText())
        print('Downloading video in:', self.resolution.currentText(), ' to path: ', self.download_path)
        video_audio_downloader.download_file(self.you_tube_object, self.download_path, 'video', self.resolution.currentText(), self.audio_type.currentText())
        self.video_audio_download_status.setText('Video downloaded in ' + self.resolution.currentText())

    def download_audio(self):
        if self.you_tube_object == None:
            print('No video loaded!')
            return -1
        
        self.video_audio_download_status.setText('Downloading audio in ' + self.audio_type.currentText())
        print('Downloading audio in:', self.audio_type.currentText(), ' to path: ', self.download_path)
        video_audio_downloader.download_file(self.you_tube_object, self.download_path, 'audio', self.resolution.currentText(), self.audio_type.currentText())
        self.video_audio_download_status.setText('Audio downloaded in ' + self.audio_type.currentText())

    def save_statistics_to_file(self):
        if self.you_tube_object == None:
            print('No video loaded!')
            return -1

        file = open(f"{self.project_path}/YouTubeDownloader/Statistics/{self.title}.", 'w')

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
        self.statistics_status.setText('Statistics saved to file')


# app = qtw.QApplication([])
# app.exec_()
