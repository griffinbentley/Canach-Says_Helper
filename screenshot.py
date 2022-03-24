import numpy as np
import cv2
import pyautogui

def Color_Sum(lower, upper, image):
    lower, upper = np.array(lower), np.array(upper)
    mask = cv2.inRange(image, lower, upper)
    return int(np.sum(mask)/255), mask

def Get_Colors(image):
    sum_r, mask= Color_Sum([0, 50, 160], [9, 255, 255], image)
    # if mode == "b":
    #     cv2.imwrite("base_mask_r.jpg", mask)
    # else:
    #     cv2.imwrite("mask_r.jpg", mask)
    sum_y, mask= Color_Sum([25, 50, 70], [35, 255, 255], image)
    # if mode == "b":
    #     cv2.imwrite("base_mask_y.jpg", mask)
    # else:
    #     cv2.imwrite("mask_y.jpg", mask)
    sum_b, mask= Color_Sum([90, 50, 70], [128, 255, 255], image)
    # if mode == "b":
    #     cv2.imwrite("base_mask_b.jpg", mask)
    # else:
    #     cv2.imwrite("mask_b.jpg", mask)
    return np.array([sum_r, sum_y, sum_b])

def Screenshot():
    image = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2HSV)
    image = image[:int(image.shape[0]/2),:,:]
    # if mode == "b":
    #     cv2.imwrite("base.jpg", cv2.cvtColor(image, cv2.COLOR_HSV2BGR))
    # else:
    #     cv2.imwrite("image_y.jpg", cv2.cvtColor(image, cv2.COLOR_HSV2BGR))
    #image = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2HSV)
    #print(Get_Colors(image))
    #image[image.shape[0]-1, image.shape[1]-1] = [255, 255, 255]
    #image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    #return image
    # if mode == "b":
    #     return Get_Colors(image, mode)
    # else:
    #     return Get_Colors(image)
    return Get_Colors(image)

