#from screenshot import Screenshot
import keyboard
import time
import random

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
    time.sleep(1)
    if key == 5:
        quit()
    key = 0

    # memory mechanism
    tiles = []
    for i in range(6):
        # get tile from screenshot
        #tiles.append(Screenshot())
        print("go")
        while key == 0:
            keyboard.on_press(callback)
            time.sleep(.05)
        time.sleep(3 + i * .9)
        if key == 5 or key == 4:
            quit()
        tiles.append(key)
        key = 0
        for j in range(i + 1):
            k = tiles[j]
            if j > 0 and tiles[j-1] == k:
                time.sleep(.6 + random.random() * .05)
            elif j > 1 and tiles[j-2] == k:
                time.sleep(.5 + random.random() * .05)
            elif j > 2 and tiles[j-3] == k:
                time.sleep(.4 + random.random() * .05)
            else:
                time.sleep(.2 * random.random() * .05)   
            print("press: ", k)
    print("go")

while True:
    main()
