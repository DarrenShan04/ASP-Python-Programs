import pygame
import time, random
import numpy as np
from pygame import mixer
# play a WAV file
class NotePlayer:
    # constructor
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 2048)
        #pygame.init()
        mixer.init()
        # dictionary of notes
        self.notes = {}
        # add a note
    def add(self, fileName):
        self.notes[fileName] = pygame.mixer.Sound(fileName)
        # play a note
    def play(self, fileName):
        try:
            self.notes[fileName].play()
        except:
            print(fileName + ' not found!')
    def playRandom(self):
        """play a random note"""
        index = random.randint(0, len(self.notes)-1)
        note = list(self.notes.values())[index]
        note.play()


nplayer=NotePlayer()
wavFilesListPiano=[]
wavFilesListPiano.append("piano/a1.wav")
wavFilesListPiano.append("piano/a1s.wav")
wavFilesListPiano.append("piano/b1.wav")
wavFilesListPiano.append("piano/c1.wav")
wavFilesListPiano.append("piano/c1s.wav")
wavFilesListPiano.append("piano/d1.wav")
wavFilesListPiano.append("piano/d1s.wav")
wavFilesListPiano.append("piano/e1.wav")
wavFilesListPiano.append("piano/f1.wav")
wavFilesListPiano.append("piano/f1s.wav")
wavFilesListPiano.append("piano/g1.wav")
wavFilesListPiano.append("piano/g1s.wav")

for pianoFile in wavFilesListPiano:
    nplayer.add(pianoFile)
# play a random tune

while True:
    try:
        nplayer.playRandom()
        # rest - 1 to 8 beats
        rest = np.random.choice([1, 2, 4, 8], 1,p=[0.15, 0.7, 0.1, 0.05])
        time.sleep(0.25*rest[0])
    except KeyboardInterrupt:
        exit()
