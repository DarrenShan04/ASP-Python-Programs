import time
import os
import smbus
import Adafruit_TCS34725
import math

tcs = Adafruit_TCS34725.TCS34725()

colorValues = {'green' : [[r for r in range(12, 52)], [g for g in range(44, 84)], [b for b in range(14, 54)], [c for c in range(111, 151)], [l for l in range(44, 84)]],
                'brown' : [[r for r in range(-3, 37)], [g for g in range(-3, 37)], [b for b in range(-4, 36)], [c for c in range(32, 82)], [l for l in range(-11, 29)]],
                'black' : [[r for r in range(7, 47)], [g for g in range(44, 84)], [b for b in range(60, 100)], [c for c in range(152, 192)], [l for l in range(12, 52)]],
                'blue' : [[r for r in range(-8, 32)], [g for g in range(-3, 37)], [b for b in range(-6, 34)], [c for c in range(25, 65)], [l for l in range(-8, 32)]],
                'orange' : [[r for r in range(56, 96)], [g for g in range(31, 75)], [b for b in range(13, 53)], [c for c in range(138, 178)], [l for l in range(11, 51)]],
                'yellow' : [[r for r in range(88, 136)], [g for g in range(96, 141)], [b for b in range(31, 71)], [c for c in range(261, 331)], [l for l in range(88, 128)]],
                'darkgreen' : [[r for r in range(2, 43)], [g for g in range(20, 60)], [b for b in range(5, 45)], [c for c in range(68, 108)], [l for l in range(18, 58)]],
                'magenta' : [[r for r in range(25, 66)], [g for g in range(12, 52)], [b for b in range(28, 68)], [c for c in range(103, 143)], [l for l in range(-20, 20)]],
                'darkpurple' : [[r for r in range(-4, 36)], [g for g in range(-2,38)], [b for b in range(-1, 39)], [c for c in range(35, 75)], [l for l in range(-12, 28)]],
                'pink' : [[r for r in range(60, 100)], [g for g in range(53, 93)], [b for b in range(49, 89)], [c for c in range(202, 242)], [l for l in range(19, 59)]],
                'darkblue' : [[r for r in range(-3, 37)], [g for g in range(10, 50)], [b for b in range(16, 56)], [c for c in range(64, 104)], [l for l in range(-6, 34)]],
                'red' : [[r for r in range(38, 48)], [g for g in range(10, 51)], [b for b in range(8, 48)], [c for c in range(93, 133)], [l for l in range(1, 41)]],
                'BGcolorpiano' : [[r for r in range(11, 51)], [g for g in range(67, 107)], [b for b in range(83, 123)], [c for c in range(202, 242)], [l for l in range(32, 72)], ['piano']],
                'BGcolorguitar' : [[r for r in range(29, 70)], [g for g in range(72, 112)], [b for b in range(45, 86)], [c for c in range(149, 189)], [l for l in range(71, 111)], ['guitar']],
                'BGcolorguitar' : [[r for r in range(78, 118)], [g for g in range(117, 157)], [b for b in range(113, 153)], [c for c in range(313, 353)], [l for l in range(76, 116)], ['drum']]}
               
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

#ravg, gavg, bavg, cavg, lavg = run5times()    

pianoTunes = {'green' : 'aplay PianoC.wav', 'brown' : 'aplay PianoC#.wav', 'blue' : 'aplay PianoD.wav', 'black' : 'PianoD#', 'orange' : 'aplay PianoE.wav', 'yellow' : 'aplay PianoF.wav', 'darkgreen' : 'aplay PianoF#.wav', 'magenta':'aplay PianoG.wav', 'dark purple' : 'aplay PianoG#.wav', 'pink':'aplay PianoA.wav', 'darkblue': 'aplay PianoA#.wav', 'red' : 'PianoB.wav'}
ravg, gavg, bavg, cavg, lavg = run5times()

while True:
    for key in colorValues:
        if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
            if key.startswith('BG'):
                instrument = colorValues[key][5]
            else:
                pass
    if instrument == 'piano':
        ravg, gavg, bavg, cavg, lavg = run5times()
        for key in colorValues:
            if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
                    os.system(pianoTunes[key])
                    time.sleep(0.5)
    
    if instrument == 'guitar':
        ravg, gavg, bavg, cavg, lavg = run5times()
        for key in colorValues:
            if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
                    os.system(guitarTunes[key])
                    time.sleep(0.5)
    if instrument == 'drum':
        ravg, gavg, bavg, cavg, lavg = run5times()
        for key in colorValues:
            if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
                    os.system(drumTunes[key])
                    time.sleep(0.5)
        
