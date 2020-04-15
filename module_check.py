import pip


def install(package):
    pip.main(['install', package])

install('mutagen')

#install('gTTS')

#from gtts import gTTS
from mutagen.mp3 import MP3
