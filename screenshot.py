import numpy as np
import cv2
import pyautogui

def Screenshot():
    # takes screenshot and saves on drive
    # image = pyautogui.screenshot()
    # image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # cv2.imwrite("image.png", image)
    image = cv2.imread("test/gw003.jpg")
    lower = [np.array([22, 93, 0], dtype="uint8")]
    upper = [np.array([120, 255, 255], dtype="uint8")]

    # yellow
    # np.array([22, 93, 0], dtype="uint8")
    # np.array([45, 255, 255], dtype="uint8")
    mask = cv2.inRange(image, lower[0], upper[0])
    cv2.imwrite("image_y.jpg", mask)

    tile = 0
    return tile