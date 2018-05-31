import time
import os
import smbus
import Adafruit_TCS34725

tcs = Adafruit_TCS34725.TCS34725()
a = tcs.get_raw_data()
re, gr, bl, cl = tcs.get_raw_data()
l = Adafruit_TCS34725.calculate_lux(re, gr, bl)

def run5times():
    lis = []
    lislux = []
    x = 0
   

    while x < 5:
        lis.append(a)
        lislux.append(l)
        x += 1
    print(lis)
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
    ravg = sum(red) / 5
    gavg = sum(green) / 5
    bavg = sum(blue) / 5
    cavg = sum(clear) / 5
    lavg = sum(luxvalues) / 5

    print(ravg)
    print(gavg)
    print(bavg)
    print(cavg)
    print(lavg)
    
    #for x in lis:
        #print(x)
        #print(x[0])
        #print(x[1])
        #if x[0] in range(89, 100) and x[1] in range(1, 6):
            #print('Yes')
run5times()


