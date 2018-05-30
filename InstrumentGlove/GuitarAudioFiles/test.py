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

colorValues = {'green' : [[r for r in range(20, 46)], [g for g in range(45, 81)], [b for b in range(25, 51)], [c for c in range(115, 141)], [l for l in range(50, 76)]],
                'brown' : [[r for r in range(5, 31)], [g for g in range(5, 31)], [b for b in range(5, 31)], [c for c in range(38, 64)], [l for l in range(0, 26)]],
                'black' : [[r for r in range(5, 26)], [g for g in range(10, 31)], [b for b in range(10, 31)], [c for c in range(35, 61)], [l for l in range(5, 26)]],
                'blue' : [[r for r in range(15, 41)], [g for g in range(45, 71)], [b for b in range(65, 81)], [c for c in range(155, 181)], [l for l in range(15, 41)]],
                'orange' : [[r for r in range(65, 86)], [g for g in range(35, 66)], [b for b in range(20, 46)], [c for c in range(130, 156)], [l for l in range(10, 36)]],
                'yellow' : [[r for r in range(90, 116)], [g for g in range(90, 116)], [b for b in range(35, 61)], [c for c in range(240, 266)], [l for l in range(80, 106)]],
                'darkgreen' : [[r for r in range(10, 35)], [g for g in range(20, 46)], [b for b in range(10, 31)], [c for c in range(65, 91)], [l for l in range(35, 61)]],
                'magenta' : [[r for r in range(30, 56)], [g for g in range(15, 41)], [b for b in range(25, 51)], [c for c in range(90, 126)], [l for l in range(-10, 11)]],
                'darkpurple' : [[r for r in range(10, 36)], [g for g in range(10, 36)], [b for b in range(10, 36)], [c for c in range(35, 61)], [l for l in range(-5, 21)]],
                'pink' : [[r for r in range(65, 86)], [g for g in range(50, 76)], [b for b in range(50, 76)], [c for c in range(185, 211)], [l for l in range(15, 46)]],
                'darkblue' : [[r for r in range(10, 36)], [g for g in range(15, 36)], [b for b in range(18, 41)], [c for c in range(60, 86)], [l for l in range(0, 26)]],
                'red' : [[r for r in range(50, 71)], [g for g in range(20, 41)], [b for b in range(17, 36)], [c for c in range(95, 121)], [l for l in range(0, 16)]],
                'grey' : [[r for r in range(65, 91)], [g for g in range(85, 111)], [b for b in range(75, 101)], [c for c in range(247, 274)], [l for l in range(50, 76)]]}
colorsValues = OrderedDict()

pianoTunes = {'green' : 'aplay PianoC.wav', 'brown' : ' aplay PianoC#.wav', 'blue' : 'aplay PianoD.wav', 'black' : 'aplay PianoD#.wav', 'orange' : 'aplay PianoE.wav', 'yellow' : 'aplay PianoF.wav', 'dark green' : 'aplay PianoF#.wav', 'magenta':'aplay PianoG.wav', 'dark purple' : 'aplay PianoG#.wav', 'pink':'aplay PianoA.wav', 'dark blue': 'aplay PianoA#.wav', 'red' : 'PianoB.wav', 'grey' : 'PianoC.wav' }
pianoTunes = OrderedDict()

guitarTunes = {'green' : 'aplay GuitarC.wav', 'brown' : ' aplay GuitarC#.wav', 'blue' : 'aplay GuitarD.wav', 'black' : 'aplay GuitarD#.wav', 'orange' : 'aplay GuitarE.wav', 'yellow' : 'aplay GuitarF.wav', 'dark green' : 'aplay GuitarF#.wav', 'magenta':'aplay GuitarG.wav', 'dark purple' : 'aplay GuitarG#.wav', 'pink':'aplay GuitarA.wav', 'dark blue': 'aplay GuitarA#.wav', 'red' : 'GuitarB.wav', 'grey' : 'GuitarC.wav' }
guitarTunes = OrderedDict()

drumTunes = {'black':'DrumBass.wav', 'blue':'DrumTomLow.wav', 'pink': 'DrumTomHi.wav', 'brown':'DrumStick.wav', 'red':'DrumSnare.wav', 'orange':'DrumHiHat.wav', 'green':'DrumFloorTom.wav', 'yellow':'DrumCrashCymbal.wav'}
drumTunes = OrderedDict()

for key in colorValues:
        if sensedcolor[0] in colorValues[key][0] and sensedcolor[1] in colorValues[key][1] and sensedcolor[2] in colorValues[key][2] and sensedcolor[3] in colorValues[key][3] and lux in colorValues[key][4]:
            os.system(guitarTunes[key])
