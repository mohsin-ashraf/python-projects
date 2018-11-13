#trex-game.skipser.com
from PIL import ImageGrab, ImageOps
import numpy as np
import pyautogui
import time
class Cordinates:
    restartBtn = (697, 377)
    dinoCord = (455, 387)
    boxStarting = (464, 376)
    boxEnding = (553, 414)
def replay():
    pyautogui.click(Cordinates.restartBtn)
def pressSpace():
    pyautogui.keyDown('space')
def imageGrab():
    box = (Cordinates.boxStarting[0],Cordinates.boxStarting[1],Cordinates.boxEnding[0],Cordinates.boxEnding[1])
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    print a.sum()
    return a.sum()
replay()
while True:
    if imageGrab()!= 3629:
        pressSpace()
