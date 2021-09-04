import math
import tkinter as tk

# constants
SCREEN_W = 480
SCREEN_H = 272

TOP_BUTTON_SPACE_W = 21 # this results in integer button widths
TOP_BUTTON_W = math.floor((SCREEN_W - TOP_BUTTON_SPACE_W * (3 - 1)) / 3)
TOP_BUTTON_H = 70

MAIN_GAP_H = 30

class MainLayout(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)

        self.btn1Slot = tk.Frame(self)
        self.btn1Slot.grid(column=0, row=0, sticky=('N', 'S', 'E', 'W'))
        self.btn1Slot.pack_propagate(False)
        self.btn1Slot.grid_propagate(False)

        self.btnGap1 = tk.Frame(self)
        self.btnGap1['width'] = TOP_BUTTON_SPACE_W
        self.btnGap1['height'] = TOP_BUTTON_H
        self.btnGap1.grid(column=1, row=0)

        self.btn2Slot = tk.Frame(self)
        self.btn2Slot.grid(column=2, row=0, sticky=('N', 'S', 'E', 'W'))
        self.btn2Slot.pack_propagate(False)
        self.btn2Slot.grid_propagate(False)

        self.btnGap2 = tk.Frame(self)
        self.btnGap2['width'] = TOP_BUTTON_SPACE_W
        self.btnGap2['height'] = TOP_BUTTON_H
        self.btnGap2.grid(column=3, row=0)

        self.btn3Slot = tk.Frame(self)
        self.btn3Slot.grid(column=4, row=0, sticky=('N', 'S', 'E', 'W'))
        self.btn3Slot.pack_propagate(False)
        self.btn3Slot.grid_propagate(False)

        self.gap = tk.Frame(self)
        self.gap['height'] = MAIN_GAP_H
        self.gap.grid(column=0, row=1, columnspan=5)

        self.main = tk.Frame(self)
        self.main.pack_propagate(False)
        self.main.grid_propagate(False)
        self.main.grid(column=0, row=2, columnspan=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(2, weight=1)

        self.topRowFrames = [
            self.btn1Slot,
            self.btn2Slot,
            self.btn3Slot,
        ]

    def top_row_frame(self, index):
        return self.topRowFrames[index]

    def main_frame(self):
        return self.main
