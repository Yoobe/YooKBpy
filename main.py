#!/usr/bin/python
# -*- coding:utf-8 -*-

print("Starting YooKBpi 1.0")

# HID Init
import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kbInit import KBInit
from ascii import *

# DEBUG
import os
import gc
import microcontroller
import time
# import board
gc.enable()
print("Running", os.uname().machine, " on python", os.uname().version)
print("CPU1", 
      microcontroller.cpus[0].frequency/1000000," MHz", 
      " - Temp :", 
      microcontroller.cpus[0].temperature) # Get the Frequency of the CPU
print("CPU2", 
      microcontroller.cpus[1].frequency/1000000," MHz", 
      " - Temp :", 
      microcontroller.cpus[1].temperature) # Get the Frequency of the CPU
print( "F. Mem", gc.mem_free()/1000, "KB" )
# print( "Board Pins")
# for pin in dir(microcontroller.pin):
#     if isinstance(getattr(microcontroller.pin, pin), microcontroller.Pin):
#         print(" - ".join(("microcontroller.pin.", pin, "\t")), end=" ")
#         for alias in dir(board):
#             if getattr(board, alias) is getattr(microcontroller.pin, pin):
#                 print("".join(("", "board.", alias)), end=" ")
#     print()

# OLED
import oled
import asciiart 

# Load first image "Welcome"
asciiart.printAscii(55, 5, asciiart.cat1)
asciiart.Mario(85, 45)

# print("Init OLED")
# oled.oled_init()
# print("Load OLED Image")
# oled.clear()
# oled.display()

import leds
leds.all_off() # Turn off all leds

# Keyboard code
print("Init the Keyboard")
# oled.text(1, 5, "01234567890123456789", 0x1111EE)
# oled.text(1, 15, "ABCDEFGHIJKLMNOPQRST", 0x1111EE)
# oled.text(1, 25, "!@#$%^&*()_+{}:;'<>?", 0x1111EE)
# oled.text(1, 35, "abcderfghijklmnopqrst", 0x1111EE)
# oled.text(1, 45, "-=[];'/.,?><:_+", 0x1111EE)
# oled.text(1, 55, "ABCDEFGHIJKLMNOPQRST", 0x1111EE)
# oled.text(5, 5, "New long text demo with multiple lines?", 0xFFFF00)

# Create Keyboard object
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# Load Keyboard Pins and Keymap
kbConfig = KBInit()
keyboard.col_pins = kbConfig[0]
keyboard.row_pins = kbConfig[1]
keyboard.diode_orientation = kbConfig[2]
keyboard.keymap = kbConfig[3]

# Function Called for each key press
keyCount = 0
def key_debug(key, keyboard, *args):
    global keyCount
    keyCount += 1
    # check if key exists in the Codes table
    val = KEY_CODES[key.code] if key.code in KEY_CODES else "NA"
    oled.text(0, 55, f"{val}   {keyCount}", 0x9900F9)
    # print( "M", gc.mem_free()/1000, "KB" )
    return False

# Function keyPressHandler
for kbLayers in kbConfig[3]:
    for key in kbLayers:
        # if key != KC.MO(1):
        if hasattr(key, '_post_press_handlers') == False:
            key.after_press_handler(key_debug)

# Debug Timer
def debugText():
    CPUFreq = str(int(microcontroller.cpus[0].frequency/1000000))
    CPUTemp = str(int(microcontroller.cpus[0].temperature))
    Mem = str(int(gc.mem_free()/1000))

    # print("T", CPUTemp, "- M", Mem, "kB" )
    oled.text(1, 45, f"{CPUTemp}° - {Mem} kB", 0x00FFFF)

# tim4 = pyb.Timer(4, freq=10)
# tim4.callback(lambda t: debugText())

# init KB
print("Init Keyboard class")
keyboard.YooKBInit()
lasttime = time.monotonic()

if __name__ == '__main__':
    while keyboard.YooKBmain() != False:
        gc.collect()
        now = time.monotonic()
        # print(now)
        if now - lasttime > 10:
            # print("tic")
            lasttime = now
            debugText()
        
