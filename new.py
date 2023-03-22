# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 19:04:51 2022

@author: igork
"""

from pynput.keyboard import Key, Controller
import time
import keyboard
keyboard.wait('-')
keyboarder = Controller()                              
timer = 1.1          
for i in range(15):
 keyboarder.press(' ')
 keyboarder.release(' ')
 time.sleep(timer)
 timer   = timer -  0.0151  
                                  
print(timer)                             
timer = 0.91        
keyboard.wait('-')
for i in range(15):
 keyboarder.press(' ')
 keyboarder.release(' ')
 time.sleep(timer)
 timer   = timer -  0.015             
