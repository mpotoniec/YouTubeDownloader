import os
import platform

if __name__ == '__main__':
    def clear_console():
        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

    if platform.system() == 'Linux':
        os.system('mkdir Downloads')
        os.system('mkdir Statistics')
        os.system('mkdir VideoOperationsFile')
        os.system('mkdir VideoOperationsFile/Audio')
        os.system('mkdir VideoOperationsFile/Video')
    elif platform.system() == 'Windows':
        os.system('mkdir Downloads')
        os.system('mkdir Statistics')
        os.system('mkdir VideoOperationsFile')
        os.system('mkdir VideoOperationsFile/Audio')
        os.system('mkdir VideoOperationsFile/Video')