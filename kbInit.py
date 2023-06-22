import board
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from macros import *


def KBInit():
    col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4)
    row_pins = (board.GP5, board.GP6, board.GP7, board.GP8)
    diode_orientation = DiodeOrientation.COL2ROW

    _____ = KC.NO

    keymap = [
        [
            KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,
            KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R, 
            _____,      KC.A,       KC.S,       KC.D,       _____, 
            KC.MO(1),   KC.Z,       KC.X,       KC.C,       KC.SPACE,
        ],
        [
            KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,
            KC.TAB,     KC.Q,       KC.W,       SAY_HI,     KC.R, 
            _____,      KC.A,       KC.S,       KC.D,       _____,
            KC.TRNS,    KC.Z,       KC.X,       KC.C,       KC.SPACE,
        ]
    ]

    return col_pins, row_pins, diode_orientation, keymap