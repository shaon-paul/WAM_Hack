# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:34:17 2020

@author: paul
"""

import pyautogui
import time
pyautogui.FAILSAFE = False
while True:
    time.sleep(20)
    for i in range(0,100):
        pyautogui.moveTo(0, i*5)
    for i in range(0, 3):
        pyautogui.press('shift')