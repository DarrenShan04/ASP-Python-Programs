import time
import os
import smbus
import Adafruit_TCS34725

tcs = Adafruit_TCS34725.TCS34725()

colorValues = {'green' : [[r for r in range(25, 51)], [g for g in range(70, 96)], [b for b in range(45, 81)], [c for c in range(150, 200)], [l for l in range(58, 90)]],
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
                
sensedcolor = tcs.get_raw_data()
re, gr, bl, cl = tcs.get_raw_data()
lux = Adafruit_TCS34725.calculate_lux(re, gr, bl)

def run5times():
    lis = []
    lislux = []
    x = 0
    while x < 5:
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

    return avgr, avgg, avgb, avgc, avgl

ravg, gavg, bavg, cavg, lavg = run5times()    

pianoTunes = {'green' : 'aplay PianoC.wav', 'brown' : 'aplay PianoC#.wav', 'blue' : 'aplay PianoD.wav', 'black' : 'PianoD#', 'orange' : 'aplay PianoE.wav', 'yellow' : 'aplay PianoF.wav', 'darkgreen' : 'aplay PianoF#.wav', 'magenta':'aplay PianoG.wav', 'dark purple' : 'aplay PianoG#.wav', 'pink':'aplay PianoA.wav', 'darkblue': 'aplay PianoA#.wav', 'red' : 'PianoB.wav'}


while True:
    print('a')
    tcs.get_raw_data()
    ravg, gavg, bavg, cavg, lavg = run5times()
    print(ravg)
    print(gavg)
    print(bavg)
    print(cavg)
    print(lavg)
    for key in colorValues:
        print('b')
        if (ravg in colorValues[key][0]) and (gavg in colorValues[key][1]) and (bavg in colorValues[key][2]) and (cavg in colorValues[key][3]) and (lavg in colorValues[key][4]):
                os.system(pianoTunes[key])
                
