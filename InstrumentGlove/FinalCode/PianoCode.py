import time
import os
import smbus
import Adafruit_TCS34725
import math

tcs = Adafruit_TCS34725.TCS34725()

colorValues = {'green' : [[r for r in range(22, 42)], [g for g in range(54, 74)], [b for b in range(24, 44)], [c for c in range(121, 141)], [l for l in range(54, 74)]],
                'brown' : [[r for r in range(7, 27)], [g for g in range(7, 27)], [b for b in range(6, 26)], [c for c in range(42, 72)], [l for l in range(-1, 19)]],
                'blue' : [[r for r in range(17, 37)], [g for g in range(54, 74)], [b for b in range(70, 90)], [c for c in range(162, 182)], [l for l in range(22, 42)]],
                'black' : [[r for r in range(2, 22)], [g for g in range(7, 27)], [b for b in range(4, 24)], [c for c in range(35, 55)], [l for l in range(2, 22)]],
                'orange' : [[r for r in range(66, 86)], [g for g in range(41, 65)], [b for b in range(23, 43)], [c for c in range(148, 168)], [l for l in range(21, 41)]],
                'yellow' : [[r for r in range(98, 126)], [g for g in range(106, 131)], [b for b in range(41, 61)], [c for c in range(261, 301)], [l for l in range(98, 118)]],
                'darkgreen' : [[r for r in range(12, 33)], [g for g in range(30, 50)], [b for b in range(15, 35)], [c for c in range(78, 98)], [l for l in range(28, 48)]],
                'magenta' : [[r for r in range(35, 56)], [g for g in range(22, 42)], [b for b in range(38, 58)], [c for c in range(113, 133)], [l for l in range(-10, 10)]],
                'darkpurple' : [[r for r in range(6, 26)], [g for g in range(8,28)], [b for b in range(9, 29)], [c for c in range(45, 65)], [l for l in range(-2, 18)]],
                'pink' : [[r for r in range(70, 90)], [g for g in range(63, 83)], [b for b in range(59, 79)], [c for c in range(212, 232)], [l for l in range(9, 29)]],
                'darkblue' : [[r for r in range(7, 27)], [g for g in range(20, 40)], [b for b in range(26, 46)], [c for c in range(74, 94)], [l for l in range(4, 24)]],
                'red' : [[r for r in range(48, 68)], [g for g in range(20, 41)], [b for b in range(18, 38)], [c for c in range(103, 123)], [l for l in range(11, 31)]],
                'BGcolorpiano' : [[r for r in range(21, 41)], [g for g in range(77, 97)], [b for b in range(93, 113)], [c for c in range(212, 232)], [l for l in range(22, 62)], ['piano']],
                'BGcolorguitar' : [[r for r in range(39, 60)], [g for g in range(82, 102)], [b for b in range(55, 76)], [c for c in range(159, 179)], [l for l in range(81, 101)], ['guitar']],
                'BGcolordrum' : [[r for r in range(88, 108)], [g for g in range(127, 147)], [b for b in range(123, 143)], [c for c in range(323, 343)], [l for l in range(86, 106)], ['drum']]}
               
sensedcolor = tcs.get_raw_data()
re, gr, bl, cl = tcs.get_raw_data()
lux = Adafruit_TCS34725.calculate_lux(re, gr, bl)

def run5times():
    lis = []
    lislux = []
    x = 0
    while x < 5:
        sensedcolor = tcs.get_raw_data()
        lis.append(sensedcolor)
        lislux.append(lux)
        x += 1
    b = 0
    red = []
    green = []
    blue = []
    clear = []
    luxvalues = []
    while b < 4:
        red.append(lis[b][0])
        green.append(lis[b][1])
        blue.append(lis[b][2])
        clear.append(lis[b][3])
        luxvalues.append(lislux[b])
        b += 1
    avgr = sum(red) / 5
    avgg = sum(green) / 5
    avgb = sum(blue) / 5
    avgc = sum(clear) / 5
    avgl = sum(luxvalues) / 5
    avgr = math.floor(avgr)
    avgg = math.floor(avgg)
    avgb = math.floor(avgb)
    avgc = math.floor(avgc)
    avgl = math.floor(avgl)

    return avgr, avgg, avgb, avgc, avgl

pianoTunes = {'green' : 'aplay PianoC.wav', 'brown' : 'aplay PianoC#.wav', 'blue' : 'aplay PianoD.wav', 'black' : 'aplay PianoD#.wav', 'orange' : 'aplay PianoE.wav', 'yellow' : 'aplay PianoF.wav', 'darkgreen' : 'aplay PianoF#.wav', 'magenta':'aplay PianoG.wav', 'darkpurple' : 'aplay PianoG#.wav', 'pink':'aplay PianoA.wav', 'darkblue': 'aplay PianoA#.wav', 'red' : 'aplay PianoB.wav'}

while True:
    ravg, gavg, bavg, cavg, lavg = run5times()
    for key in colorValues:
        if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
            os.system(pianoTunes[key])
            time.sleep(0.05)
        continue
