import numpy as np
import cv2
import pyautogui

# sums up number of pixel within given HSV range
def Color_Sum(lower, upper, image, debug=False):
    lower, upper = np.array(lower), np.array(upper)
    mask = cv2.inRange(image, lower, upper)
    if debug: print(mask)
    return int(np.sum(mask)/255), mask

# gathers sums of the three colors of given image
def Get_Colors(image, debug=False):
    sum_r, mask= Color_Sum([0, 50, 160], [9, 255, 255], image, debug)
    if debug: cv2.imwrite("mask_r.jpg", mask)
    sum_y, mask= Color_Sum([25, 50, 70], [35, 255, 255], image, debug)
    if debug: cv2.imwrite("mask_y.jpg", mask)
    sum_b, mask= Color_Sum([90, 50, 70], [128, 255, 255], image, debug)
    if debug: cv2.imwrite("mask_b.jpg", mask)
    return np.array([sum_r, sum_y, sum_b])

# takes screenshot and returns color sums for red, yellow and blue
def Screenshot(debug=False):
    image = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2HSV)
    image = image[:int(image.shape[0]/2),:,:]
    return Get_Colors(image, debug)
