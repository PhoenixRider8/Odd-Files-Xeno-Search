from pygame import mixer 
from scripts.music.musicList import *

class Music:
    def __init__(self):
        mixer.init() 
        self.stopPlaying = False
    
    def play(self):
        
        # Setting the volume 
        mixer.music.set_volume(0.7) 
    
        # Start playing the song 
        mixer.music.play() 

    def pickMusic(self,name):
        if(name=='dialogue'):
            mixer.music.load(DIALOGUE)
        elif(name=='mainMenu'):
            mixer.music.load(MAIN_MENU)
        elif(name=='virus'):
            mixer.music.load(VIRUS)
        elif(name=='mice'):
            mixer.music.load(MICE)
        elif(name=='joker'):
            mixer.music.load(JOKER)

    def stop(self):
        if(self.stopPlaying):
            mixer.music.stop() 