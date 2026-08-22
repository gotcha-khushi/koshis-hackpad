import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.row_pins = (board.D2, board.D3, board.D6)

keyboard.col_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientaton = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [  KC.A, KC.B, KC.C,
       KC.D, KC.E, KC.F,
       KC.G, KC.H, KC.I,
    ]
]

keyboard.got()