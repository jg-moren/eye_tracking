import pyautogui
import numpy as np


class Screen:

    def __init__(self):
        
        img = pyautogui.screenshot()
        frame = np.array(img)
        
        self.height = frame.shape[0]
        self.wight = int(frame.shape[1]/2)
        
    

    def getScreen(self):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = frame[0:self.height,self.wight:2*self.wight]

        return frame
