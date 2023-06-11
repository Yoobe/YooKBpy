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

print(dir(board))
print("Load OLED Lib")
# OLED
import oled

# print("Init OLED")
# oled.oled_init()
# print("Load OLED Image")
oled.clear()
oled.display()

# LED
l1 = digitalio.DigitalInOut(board.GP9)  # l1
l1.switch_to_output()
l1.value = True
l1 = digitalio.DigitalInOut(board.GP10)  # l1
l1.switch_to_output()
l1.value = True
l1 = digitalio.DigitalInOut(board.GP11)  # l1
l1.switch_to_output()
l1.value = True
l1 = digitalio.DigitalInOut(board.GP12)  # l1
l1.switch_to_output()
l1.value = True
l1 = digitalio.DigitalInOut(board.GP13)  # l1
l1.switch_to_output()
l1.value = True

# Keyboard code
print("Init the Keyboard")
oled.text(1, 5, "01234567890123456789", 0x1111EE)
oled.text(1, 15, "ABCDEFGHIJKLMNOPQRST", 0x1111EE)
oled.text(1, 25, "!@#$%^&*()_+{}:;'<>?", 0x1111EE)
oled.text(1, 35, "abcderfghijklmnopqrst", 0x1111EE)
oled.text(1, 45, "-=[];'/.,?><:_+", 0x1111EE)
oled.text(1, 55, "ABCDEFGHIJKLMNOPQRST", 0x1111EE)
# oled.text(5, 5, "New long text demo with multiple lines?", 0xFFFF00)

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0,board.GP1, board.GP2,board.GP3,board.GP4)
keyboard.row_pins = (board.GP5,board.GP6,board.GP7,board.GP8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())

_____ = KC.NO

keyboard.keymap = [
    [
        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,
        KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R, 
        _____,      KC.A,       KC.S,       KC.D,       _____, 
        KC.MO(1),   KC.Z,       KC.X,       KC.C,       KC.SPACE,
    ],
    [
        KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,
        KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R, 
        _____,      KC.A,       KC.S,       KC.D,       _____,
        KC.TRNS,    KC.Z,       KC.X,       KC.C,       KC.SPACE,
    ]
]

def key_debug(key, keyboard, *args):
    print(str(key.code), " Pressed")
    oled.clear()
    oled.text(5, 5, str(key.code), 0xFFFF00)
    return False

KC.ANY.after_press_handler(key_debug)
KC.Q.after_press_handler(key_debug)
KC.W.after_press_handler(key_debug)
KC.S.after_press_handler(key_debug)
KC.D.after_press_handler(key_debug) 


if __name__ == '__main__':
    keyboard.go()
