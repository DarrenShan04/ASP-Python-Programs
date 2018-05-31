import time
import os
import smbus
import Adafruit_TCS34725
import math

tcs = Adafruit_TCS34725.TCS34725()

colorValues = {'green' : [[r for r in range(22, 42)], [g for g in range(54, 74)], [b for b in range(24, 44)], [c for c in range(121, 141)], [l for l in range(54, 74)]],
                'blue' : [[r for r in range(17, 37)], [g for g in range(54, 74)], [b for b in range(70, 90)], [c for c in range(162, 182)], [l for l in range(22, 42)]],
                
                'orange' : [[r for r in range(66, 86)], [g for g in range(41, 65)], [b for b in range(23, 43)], [c for c in range(148, 168)], [l for l in range(21, 41)]],
                'yellow' : [[r for r in range(98, 126)], [g for g in range(106, 131)], [b for b in range(41, 61)], [c for c in range(261, 301)], [l for l in range(98, 118)]],
                'darkgreen' : [[r for r in range(12, 33)], [g for g in range(30, 53)], [b for b in range(15, 35)], [c for c in range(78, 98)], [l for l in range(28, 48)]],
                'magenta' : [[r for r in range(35, 56)], [g for g in range(22, 42)], [b for b in range(38, 58)], [c for c in range(113, 133)], [l for l in range(-10, 10)]],
                
                'pink' : [[r for r in range(70, 90)], [g for g in range(63, 83)], [b for b in range(59, 79)], [c for c in range(212, 250)], [l for l in range(9, 29)]],
                
                'red' : [[r for r in range(48, 68)], [g for g in range(20, 41)], [b for b in range(18, 38)], [c for c in range(103, 130)], [l for l in range(11, 31)]],
                'BGcolorpiano' : [[r for r in range(21, 41)], [g for g in range(77, 97)], [b for b in range(93, 113)], [c for c in range(212, 232)], [l for l in range(22, 62)], ['piano']],
                'BGcolorguitar' :  [[r for r in range(12, 33)], [g for g in range(30, 53)], [b for b in range(15, 35)], [c for c in range(78, 98)], [l for l in range(28, 48)], ['guitar']],
                'BGcolordrum' : [[r for r in range(88, 108)], [g for g in range(127, 147)], [b for b in range(123, 143)], [c for c in range(343, 375)], [l for l in range(86, 106)], ['drum']]}
               
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

pianoTunes = {'green' : 'aplay PianoC.wav', 'blue' : 'aplay PianoD.wav', 'orange' : 'aplay PianoE.wav', 'yellow' : 'aplay PianoF.wav',  'magenta':'aplay PianoG.wav', 'pink':'aplay PianoA.wav', 'red' : 'aplay PianoB.wav'}
guitarTunes = {'green' : 'aplay GuitarC.wav', 'blue' : 'aplay GuitarD.wav', 'orange' : 'aplay GuitarE.wav', 'yellow' : 'aplay GuitarF.wav', 'magenta':'aplay GuitarG.wav', 'pink':'aplay GuitarA.wav', 'red' : 'aplay GuitarB.wav'}
drumTunes = {'magenta':'aplay DrumBass.wav', 'blue':'aplay DrumTomLow.wav', 'pink': 'aplay DrumTomHi.wav', 'brown':'aplay DrumStick.wav', 'red':'aplay DrumSnare.wav', 'orange':'aplay DrumHiHat.wav', 'green':'aplay DrumFloorTom.wav', 'yellow':'aplay DrumCrashCymbal.wav'}

instrument = 'piano'

while True:
    averagevalues=run5times()   
    ravg, gavg, bavg, cavg, lavg = averagevalues
    for key in colorValues:
        if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
            if key.startswith('B'):
                instrument = colorValues[key][5]
                print('a')
            else:
                pass
    if instrument == 'piano':
        averagevalues=run5times()   
        ravg, gavg, bavg, cavg, lavg = averagevalues
        for key in colorValues:
            if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
                    os.system(pianoTunes[key])
                    time.sleep(0.5)
                    continue
    
    if instrument == 'guitar':
        averagevalues=run5times()    
        ravg, gavg, bavg, cavg, lavg = averagevalues
        for key in colorValues:
            if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
                    os.system(guitarTunes[key])
                    time.sleep(0.5)
                    continue
    if instrument == 'drum':
        averagevalues=run5times()   
        ravg, gavg, bavg, cavg, lavg = averagevalues
        for key in colorValues:
            if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
                    os.system(drumTunes[key])
                    time.sleep(0.5)
                    continue
