from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
import board

keyboard = KMKKeyboard()

# Rows: ROW0..ROW5
keyboard.row_pins = (
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
)

# Cols: COL0..COL14
keyboard.col_pins = (
    board.GP12,  # COL0
    board.GP13,  # COL1
    board.GP14,  # COL2
    board.GP15,  # COL3
    board.GP16,  # COL4
    board.GP17,  # COL5
    board.GP18,  # COL6
    board.GP19,  # COL7
    board.GP20,  # COL8
    board.GP21,  # COL9
    board.GP22,  # COL10
    board.GP26,  # COL11
    board.GP27,  # COL12
    board.GP28,  # COL13
    board.GP0,   # COL14
)

keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [[
    # Row 0 (15)
    KC.ESC, KC.TAB, KC.BSPC, KC.LSFT, KC.LCTL, KC.LALT, KC.LGUI, KC.RGUI, KC.RALT, KC.RCTL, KC.RSFT, KC.NO, KC.NO, KC.NO, KC.NO,
    # Row 1 (15)
    KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.NO, KC.NO, KC.NO,
    # Row 2 (15)
    KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    # Row 3 (15)
    KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.MINS, KC.EQL,
    # Row 4 (15)
    KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.NO, KC.NO, KC.NO,
    # Row 5 (15)
    KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.SPC, KC.NO, KC.NO, KC.NO, KC.NO,


]]

if __name__ == "__main__":
    keyboard.go()
