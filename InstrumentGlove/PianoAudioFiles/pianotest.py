from collections import OrderedDict
import time
import os
import smbus
import Adafruit_TCS34725

tcs = Adafruit_TCS34725.TCS34725()
tcs.set_interrupt(False)
sensedcolor = tcs.get_raw_data()
re, gr, bl, cl = tcs.get_raw_data()
lux = Adafruit_TCS34725.calculate_lux(re, gr, bl)

colorValues = {'green' : [[r for r in range(25, 51)], [g for g in range(70, 96)], [b for b in range(45, 81)], [c for c in range(175, 201)], [l for l in range(58, 90)]],
                'brown' : [[r for r in range(10, 36)], [g for g in range(10, 36)], [b for b in range(10, 36)], [c for c in range(55, 81)], [l for l in range(0, 26)]],
                'black' : [[r for r in range(20, 46)], [g for g in range(64, 90)], [b for b in range(85, 111)], [c for c in range(190, 216)], [l for l in range(25, 51)]],
                'blue' : [[r for r in range(7, 33)], [g for g in range(5, 31)], [b for b in range(14, 40)], [c for c in range(5, 31)], [l for l in range(0, 26)]],
                'orange' : [[r for r in range(80, 116)], [g for g in range(79, 115)], [b for b in range(57, 83)], [c for c in range(175, 201)], [l for l in range(25, 51)]],
                'yellow' : [[r for r in range(110, 136)], [g for g in range(115, 141)], [b for b in range(45, 71)], [c for c in range(305, 331)], [l for l in range(105, 131)]],
                'darkgreen' : [[r for r in range(-10, 11)], [g for g in range(-9, 10)], [b for b in range(-10, 11)], [c for c in range(0, 21)], [l for l in range(-9, 10)]],
                'magenta' : [[r for r in range(41, 62)], [g for g in range(25, 46)], [b for b in range(43, 64)], [c for c in range(127, 148)], [l for l in range(-10, 11)]],
                'darkpurple' : [[r for r in range(12, 32)], [g for g in range(13,34)], [b for b in range(15, 36)], [c for c in range(60, 81)], [l for l in range(0, 21)]],
                'pink' : [[r for r in range(76, 97)], [g for g in range(77, 98)], [b for b in range(78, 99)], [c for c in range(249, 260)], [l for l in range(34, 50)]],
                'darkblue' : [[r for r in range(10, 36)], [g for g in range(30, 56)], [b for b in range(35, 61)], [c for c in range(100, 126)], [l for l in range(10, 36)]],
                'red' : [[r for r in range(65, 91)], [g for g in range(45, 71)], [b for b in range(40, 66)], [c for c in range(170, 196)], [l for l in range(15, 41)]]}
                


pianoTunes = {'green' : 'aplay PianoC.wav', 'brown' : 'aplay PianoC#.wav', 'blue' : 'aplay PianoD.wav', 'black' : 'PianoD#', 'orange' : 'aplay PianoE.wav', 'yellow' : 'aplay PianoF.wav', 'darkgreen' : 'aplay PianoF#.wav', 'magenta':'aplay PianoG.wav', 'dark purple' : 'aplay PianoG#.wav', 'pink':'aplay PianoA.wav', 'darkblue': 'aplay PianoA#.wav', 'red' : 'PianoB.wav'}

guitarTunes = {'green' : 'aplay GuitarC.wav', 'brown' : 'aplay GuiarC#.wav', 'blue' : 'aplay GuitarD.wav', 'black' : 'aplay GuitarD#.wav', 'orange' : 'aplay GuitarE.wav', 'yellow' : 'aplay GuitarF.wav', 'darkgreen' : 'aplay GuitarF#.wav', 'magenta':'aplay GuitarG.wav', 'darkpurple' : 'aplay GuitarG#.wav', 'pink':'aplay GuitarA.wav', 'darkblue': 'aplay GuitarA#.wav', 'red' : 'GuitarB.wav'}

drumTunes = {'black':'DrumBass.wav', 'blue':'DrumTomLow.wav', 'pink': 'DrumTomHi.wav', 'brown':'DrumStick.wav', 'red':'DrumSnare.wav', 'orange':'DrumHiHat.wav', 'green':'DrumFloorTom.wav', 'yellow':'DrumCrashCymbal.wav'}

print('a')
print(sensedcolor)
print(lux)
for key in colorValues:
        print('b')
        if (sensedcolor[0] in colorValues[key][0]) and (sensedcolor[1] in colorValues[key][1]) and (sensedcolor[2] in colorValues[key][2]) and (sensedcolor[3] in colorValues[key][3]) and (lux in colorValues[key][4]):
                print(key)
                print(sensedcolor)
                print(lux)
                print(pianoTunes[key])
                os.system(pianoTunes[key])
