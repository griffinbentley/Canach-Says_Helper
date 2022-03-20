import numpy as np
import cv2
import pyautogui

def Screenshot():
    # takes screenshot and saves on drive
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("image.png", image)

    tile = 0
    return tile