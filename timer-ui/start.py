import os
import tkinter as tk
from tkinter import font

from main_layout import MainLayout
from main_layout import SCREEN_W
from main_layout import SCREEN_H
from timer_frame import TimerFrame

class Application(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)

        self.layout = MainLayout(parent=self)

        btnFont = font.Font(family='Times New Roman MT Condensed', size=18)

        basePath = os.path.dirname(os.path.abspath(__file__))
        self.menuIcon = tk.PhotoImage(file='%s/icons/menu.png' %  basePath).zoom(2, 2) # persistent image reference
        self.handIcon = tk.PhotoImage(file='%s/icons/hand.png' %  basePath).zoom(2, 2) # persistent image reference
        self.hourglassIcon = tk.PhotoImage(file='%s/icons/hourglass.png' %  basePath).zoom(2, 2) # persistent image reference

        self.btn1 = tk.Button(
            self.layout.top_row_frame(0),
            font=btnFont,
            image=self.menuIcon,
            text='Menu',
            compound=tk.LEFT,
            borderwidth=0,
        )
        self.btn1.pack(fill=tk.BOTH, expand=True)

        self.btn2 = tk.Button(
            self.layout.top_row_frame(1),
            font=btnFont,
            image=self.handIcon,
            text='Pause',
            compound=tk.LEFT,
            borderwidth=0,
        )
        self.btn2.pack(fill=tk.BOTH, expand=True)

        self.btn3 = tk.Button(
            self.layout.top_row_frame(2),
            font=btnFont,
            image=self.hourglassIcon,
            text='+1min',
            compound=tk.LEFT,
            borderwidth=0,
        )
        self.btn3.pack(fill=tk.BOTH, expand=True)

        self.timerFrame = TimerFrame(parent=self.layout.main_frame())

root = tk.Tk()
root.geometry('%dx%d+0+0' % (SCREEN_W, SCREEN_H))
root.tk_setPalette(background='#101010')

app = Application(parent=root)
app.mainloop()
