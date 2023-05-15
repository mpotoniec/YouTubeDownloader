__version__ = '0.9.0'
import os
import platform
import PyQt5.QtWidgets as qtw

from YouTubeDownloader.gui.gui import MainWindow


def clear_console():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')


if __name__ == '__main__':
    clear_console()
    print('YouTubeDownloader ver:', __version__)
    app = qtw.QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
    clear_console()

