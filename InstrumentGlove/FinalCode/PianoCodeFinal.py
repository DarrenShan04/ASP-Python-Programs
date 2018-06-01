import time
import os
import smbus
import Adafruit_TCS34725
import math

tcs = Adafruit_TCS34725.TCS34725()

colorValues = {'green' : [[r for r in range(20, 42)], [g for g in range(40, 70)], [b for b in range(20, 44)], [c for c in range(100, 140)], [l for l in range(54, 74)]],               
                'blue' : [[r for r in range(17, 37)], [g for g in range(40, 70)], [b for b in range(60, 90)], [c for c in range(100, 150)], [l for l in range(22, 42)]],                
                'orange' : [[r for r in range(60, 86)], [g for g in range(35, 65)], [b for b in range(20, 43)], [c for c in range(120, 160)], [l for l in range(21, 41)]],
                'yellow' : [[r for r in range(88, 126)], [g for g in range(70, 100)], [b for b in range(30, 61)], [c for c in range(210, 245)], [l for l in range(98, 118)]],                
                'magenta' : [[r for r in range(30, 56)], [g for g in range(15, 32)], [b for b in range(30, 58)], [c for c in range(90, 130)], [l for l in range(-10, 10)]],                
                'pink' : [[r for r in range(70, 90)], [g for g in range(50, 80)], [b for b in range(50, 80)], [c for c in range(190, 230)], [l for l in range(9, 29)]],                
                'red' : [[r for r in range(48, 68)], [g for g in range(20, 41)], [b for b in range(18, 38)], [c for c in range(90, 120)], [l for l in range(11, 31)]]}

               
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

pianoTunes = {'green' : 'aplay PianoC.wav', 'blue' : 'aplay PianoD.wav', 'orange' : 'aplay PianoE.wav', 'yellow' : 'aplay PianoF.wav', 'magenta':'aplay PianoG.wav', 'pink':'aplay PianoA.wav', 'red' : 'aplay PianoB.wav'}

while True:
    averagevalues=run5times()  
    ravg, gavg, bavg, cavg, lavg = averagevalues
    for key in colorValues:
        if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]):
            os.system(pianoTunes[key])
            time.sleep(0.05)
            continue
