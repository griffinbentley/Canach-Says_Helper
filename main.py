import keyboard
import time
import random
import numpy as np
from screenshot import Screenshot

key = 0

# tracks pressed keys
def callback(event):
    global key
    name = event.name
    if name == 'f':
        key = 1

def memory(base_ryb, charges=3, debug=False):
    # memory mechanism
    tiles = []
    # for each round of "Canach Says"
    for i in range(7):
        if debug: print("screenshot")
        ryb = Screenshot(debug)
        # assign symbol based on difference in color between the two images
        sub = ryb - base_ryb
        if debug: print("ryb: ", ryb, "\nbase_ryb: ", base_ryb, "\nsub: ", sub)
        if sub[0] > sub[1] and sub[0] > sub[2]:
            if debug: print(2)
            tiles.append("2")
        elif sub[1] > sub[0] and sub[1] > sub[2]:
            if debug: print(3)
            tiles.append("3")
        elif sub[2] > sub[0] and sub[2] > sub[1]:
            if debug: print(1)
            tiles.append("1")
        # if no difference can be found, print error message and terminate
        else:
            print("Could not detect difference in source and new image\nTerminating program")
            return 1
        time.sleep(.75)

        # tell player which keys to press with precise timings so that they don't try to press a key
        #  while that key is still on cooldown
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
        if i != 6:
            time.sleep(2.25 + i * .75)
        else:
            time.sleep(1)
    # assumes player starts with 4 jade bot charges, and counts down games until player must collect more
    if charges == 0:
        print("collect 4 charges")
        main()
    print("press f")
    memory(base_ryb, charges - 1)
    return 0

def main(debug=False):
    global key
    # wait for the user to press 'f' and start the first game
    while key != 1:
        keyboard.on_press(callback)
        time.sleep(.05)
    if debug: print("screenshot")
    # take the base screenshot for the others to be compared to
    base_ryb = Screenshot(debug)
    key = 0
    time.sleep(.5)

    # if memory() returns an error, end program
    if memory(base_ryb, debug): 
        return

main()
