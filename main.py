import keyboard
import time
import random
import numpy as np
from screenshot import Screenshot

import cv2

key = 0

def callback(event):
    global key
    name = event.name
    if name == '1' or name == '2' or name == '3':
        key = int(name)
    elif name == 'f':
        key = 4
    elif name == 'esc':
        key = 5
    else:
        pass

def main():
    global key
    while key != 4:
        keyboard.on_press(callback)
        time.sleep(.05)
    #print("screenshot")
    base_ryb = Screenshot()
    if key == 5:
        quit()
    key = 0
    time.sleep(.5)

    # memory mechanism
    tiles = []
    for i in range(7):
        #print("screenshot")
        ryb= Screenshot()
        sub = ryb - base_ryb
        #print("ryb: ", ryb, "\nbase_ryb: ", base_ryb, "\nsub: ", sub)
        if sub[0] > sub[1] and sub[0] > sub[2]:
            #print(2)
            tiles.append("2")
        elif sub[1] > sub[0] and sub[1] > sub[2]:
            #print(3)
            tiles.append("3")
        elif sub[2] > sub[0] and sub[2] > sub[1]:
            #print(1)
            tiles.append("1")
        else:
            tiles.append("c")
        time.sleep(.75)

        # while key == 0:
        #     keyboard.on_press(callback)
        #     time.sleep(.05)
        # time.sleep(3 + i * .9)
        # if key == 5 or key == 4:
        #     quit()
        # tiles.append(key)
        # key = 0
        for j in range(i + 1):
            k = tiles[j]
            if j > 0 and tiles[j-1] == k:
                time.sleep(.6 + random.random() * .05)
            elif j > 1 and tiles[j-2] == k:
                time.sleep(.55 + random.random() * .05)
            elif j > 2 and tiles[j-3] == k:
                time.sleep(.5 + random.random() * .05)
            else:
                time.sleep(.2 * random.random() * .05)   
            print("press: ", k)
        time.sleep(2.25 + i * .75)

while True:
    main()


#cv2.imwrite("image_y.jpg", Screenshot(cv2.imread("test/gw001.jpg")))
