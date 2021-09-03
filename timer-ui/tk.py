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
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self['width'] = SCREEN_W
        self['height'] = SCREEN_H

        self.grid(column=0, row=0, sticky=('N', 'S', 'E', 'W'))

        btnFont = font.Font(family='Times New Roman MT Condensed', size=18)

        self.btn1 = tk.Button(self, font=btnFont)
        self.btn1["text"] = "Button 1"
        # self.btn1['height'] = TOP_BUTTON_H
        self.btn1.grid(column=0, row=0, sticky=('N', 'S', 'E', 'W'))

        self.btnGap1 = tk.Frame(self)
        self.btnGap1['width'] = TOP_BUTTON_SPACE_W
        self.btnGap1['height'] = TOP_BUTTON_H
        self.btnGap1.grid(column=1, row=0)

        self.btn2 = tk.Button(self, font=btnFont)
        self.btn2["text"] = "Button 2"
        # self.btn2['height'] = TOP_BUTTON_H
        self.btn2.grid(column=2, row=0, sticky=('N', 'S', 'E', 'W'))

        self.btnGap2 = tk.Frame(self)
        self.btnGap2['width'] = TOP_BUTTON_SPACE_W
        self.btnGap2['height'] = TOP_BUTTON_H
        self.btnGap2.grid(column=3, row=0)

        self.btn3 = tk.Button(self, font=btnFont)
        self.btn3["text"] = "Button 3"
        # self.btn3['height'] = TOP_BUTTON_H
        self.btn3.grid(column=4, row=0, sticky=('N', 'S', 'E', 'W'))

        self.gap = tk.Frame(self)
        self.gap['height'] = MAIN_GAP_H
        self.gap.grid(column=0, row=1, columnspan=5)

        self.main = tk.Frame(self)
        self.main.grid(column=0, row=2, columnspan=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(2, weight=1)

        self.pack()
    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
