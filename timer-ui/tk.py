import os
import math
import tkinter as tk
from tkinter import font

# constants
SCREEN_W = 480
SCREEN_H = 272

PADDING = 8

TOP_BUTTON_SPACE_W = 21 # this results in integer button widths
TOP_BUTTON_W = math.floor((SCREEN_W - TOP_BUTTON_SPACE_W * (3 - 1)) / 3)
TOP_BUTTON_H = 70

MAIN_GAP_H = 30

class Application(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)

        btnFont = font.Font(family='Times New Roman MT Condensed', size=18)

        basePath = os.path.dirname(os.path.abspath(__file__))
        self.menuIcon = tk.PhotoImage(file='%s/icons/menu.png' %  basePath).zoom(2, 2) # persistent image reference
        self.handIcon = tk.PhotoImage(file='%s/icons/hand.png' %  basePath).zoom(2, 2) # persistent image reference
        self.hourglassIcon = tk.PhotoImage(file='%s/icons/hourglass.png' %  basePath).zoom(2, 2) # persistent image reference

        self.btn1Slot = tk.Frame(self)
        self.btn1Slot.grid(column=0, row=0, sticky=('N', 'S', 'E', 'W'))
        self.btn1Slot.pack_propagate(False)
        self.btn1 = tk.Button(self.btn1Slot, font=btnFont, compound=tk.LEFT)
        self.btn1["text"] = "Menu"
        self.btn1["image"] = self.menuIcon
        self.btn1.pack(fill=tk.BOTH, expand=True)

        self.btnGap1 = tk.Frame(self)
        self.btnGap1['width'] = TOP_BUTTON_SPACE_W
        self.btnGap1['height'] = TOP_BUTTON_H
        self.btnGap1.grid(column=1, row=0)

        self.btn2Slot = tk.Frame(self)
        self.btn2Slot.grid(column=2, row=0, sticky=('N', 'S', 'E', 'W'))
        self.btn2Slot.pack_propagate(False)
        self.btn2 = tk.Button(self.btn2Slot, font=btnFont, compound=tk.LEFT)
        self.btn2["text"] = "Pause"
        self.btn2["image"] = self.handIcon
        self.btn2.pack(fill=tk.BOTH, expand=True)

        self.btnGap2 = tk.Frame(self)
        self.btnGap2['width'] = TOP_BUTTON_SPACE_W
        self.btnGap2['height'] = TOP_BUTTON_H
        self.btnGap2.grid(column=3, row=0)

        self.btn3Slot = tk.Frame(self)
        self.btn3Slot.grid(column=4, row=0, sticky=('N', 'S', 'E', 'W'))
        self.btn3Slot.pack_propagate(False)
        self.btn3 = tk.Button(self.btn3Slot, font=btnFont, compound=tk.LEFT)
        self.btn3["text"] = "+1min"
        self.btn3["image"] = self.hourglassIcon
        self.btn3.pack(fill=tk.BOTH, expand=True)

        self.gap = tk.Frame(self)
        self.gap['height'] = MAIN_GAP_H
        self.gap.grid(column=0, row=1, columnspan=5)

        self.main = tk.Frame(self)
        self.main.grid(column=0, row=2, columnspan=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(2, weight=1)

root = tk.Tk()
root.geometry('%dx%d+0+0' % (SCREEN_W, SCREEN_H))

app = Application(parent=root)
app.mainloop()
