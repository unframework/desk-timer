import os
import tkinter as tk
from tkinter import font

class TimerFrame(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        basePath = os.path.dirname(os.path.abspath(__file__))
        self.clockMock = tk.PhotoImage(file='%s/clock-face-mockup.png' % basePath) # persistent image reference

        self.clockFace = tk.Label(self, image=self.clockMock)
        self.clockFace.grid(column=0, row=0, rowspan=2, padx=12, pady=12)

        self.detailsFrame = tk.Frame(self)
        self.detailsFrame.grid(column=1, row=0, sticky=('N', 'S', 'E', 'W'))

        self.progressFrame = tk.Frame(self, relief=tk.GROOVE, borderwidth=2)
        self.progressFrame['height'] = 16
        self.progressFrame.grid(column=1, row=1, sticky=('N', 'S', 'E', 'W'))

        self.detailsFrame.columnconfigure(0, minsize=110)
        self.detailsFrame.columnconfigure(1, weight=1)

        labelFont = font.Font(family='Fixed', size=10)
        valueFont = font.Font(family='Fixed', size=10)

        lbl = tk.Label(self.detailsFrame, text="Status", font=labelFont)
        lbl.grid(column=0, row=0, sticky='W')
        val = tk.Label(self.detailsFrame, text="ACTIVE", font=valueFont, foreground='#40ff40')
        val.grid(column=1, row=0, sticky='W')

        lbl = tk.Label(self.detailsFrame, text="Current time", font=labelFont)
        lbl.grid(column=0, row=1, sticky='W')
        val = tk.Label(self.detailsFrame, text="2020-08-25 20:23", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=1, sticky='W')

        lbl = tk.Label(self.detailsFrame, text="Start time", font=labelFont)
        lbl.grid(column=0, row=2, sticky='W')
        val = tk.Label(self.detailsFrame, text="2020-08-25 20:16", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=2, sticky='W')

        lbl = tk.Label(self.detailsFrame, text="Break time", font=labelFont)
        lbl.grid(column=0, row=3, sticky='W')
        val = tk.Label(self.detailsFrame, text="2020-08-25 20:41", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=3, sticky='W')

        lbl = tk.Label(self.detailsFrame, text="Elapsed", font=labelFont)
        lbl.grid(column=0, row=4, sticky='W')
        val = tk.Label(self.detailsFrame, text="12m", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=4, sticky='W')

        lbl = tk.Label(self.detailsFrame, text="Total elapsed", font=labelFont)
        lbl.grid(column=0, row=5, sticky='W')
        val = tk.Label(self.detailsFrame, text="2h 20m", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=5, sticky='W')


