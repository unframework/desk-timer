import os
import tkinter as tk
from tkinter import font

class TimerDetailsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)

        self.columnconfigure(0, minsize=110)
        self.columnconfigure(1, weight=1)

        labelFont = font.Font(family='Fixed', size=10)
        valueFont = font.Font(family='Fixed', size=10)

        lbl = tk.Label(self, text="Status", font=labelFont)
        lbl.grid(column=0, row=0, sticky='W')
        val = tk.Label(self, text="ACTIVE", font=valueFont, foreground='#40ff40')
        val.grid(column=1, row=0, sticky='W')

        lbl = tk.Label(self, text="Current time", font=labelFont)
        lbl.grid(column=0, row=1, sticky='W')
        val = tk.Label(self, text="2020-08-25 20:23", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=1, sticky='W')

        lbl = tk.Label(self, text="Start time", font=labelFont)
        lbl.grid(column=0, row=2, sticky='W')
        val = tk.Label(self, text="2020-08-25 20:16", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=2, sticky='W')

        lbl = tk.Label(self, text="Break time", font=labelFont)
        lbl.grid(column=0, row=3, sticky='W')
        val = tk.Label(self, text="2020-08-25 20:41", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=3, sticky='W')

        lbl = tk.Label(self, text="Elapsed", font=labelFont)
        lbl.grid(column=0, row=4, sticky='W')
        val = tk.Label(self, text="12m", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=4, sticky='W')

        lbl = tk.Label(self, text="Total elapsed", font=labelFont)
        lbl.grid(column=0, row=5, sticky='W')
        val = tk.Label(self, text="2h 20m", font=valueFont, foreground='#cccccc')
        val.grid(column=1, row=5, sticky='W')

class TimerProgressFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.pack(fill=tk.BOTH, expand=True)

        self.rowconfigure(0, weight=1) # center vertically (not horizontally)

        margin = 12 # space on the sides so that text labels can fit in

        base_rgba = '#404040'
        filled_rgba = '#40c040'
        active_rgba = '#fff'

        timeline_height = 8
        timeline_start_x = margin + 1 # need an extra 1 for some reason?
        timeline_start_y = 13
        notch_width = 6

        total_width = notch_width * 48 + 1 + margin * 2

        self.chart = tk.Canvas(self, width=total_width, height=24)
        self.chart.grid(column=0, row=0, pady=12)

        timeFont = font.Font(family='Fixed', size=8)

        for i in range(48):
            offset_x = i * notch_width
            rgba = (
                filled_rgba if (i > 18 and i < 28) or (i > 33) else (
                    base_rgba
                )
            )

            self.chart.create_rectangle(
                timeline_start_x + offset_x,
                timeline_start_y,
                timeline_start_x + offset_x + notch_width - 1,
                timeline_start_y + timeline_height,
                fill=rgba,
                width=0,
            )

        self.chart.create_rectangle(
            timeline_start_x + 48 * notch_width,
            timeline_start_y,
            timeline_start_x + 48 * notch_width + 1,
            timeline_start_y + timeline_height,
            fill=active_rgba,
            width=0,
        )

        time_start_hour = 20.25
        time_label_index = 0
        for time_label in ['12am', '3am', '6am', '9am', '12pm', '3pm', '6pm', '9pm']:
            # calculate offset in hours and then convert to notch sizing
            time_label_hour_offset = (24 + time_label_index * 3 - time_start_hour + 12) % 24
            time_label_index += 1

            if time_label_hour_offset > 12:
                continue

            time_label_offset = time_label_hour_offset * 4 * notch_width

            self.chart.create_text(
                timeline_start_x + time_label_offset,
                timeline_start_y,
                anchor='s',
                fill=active_rgba,
                font=timeFont,
                text=time_label,
            )

            self.chart.create_rectangle(
                timeline_start_x + time_label_offset,
                timeline_start_y + timeline_height + 1,
                timeline_start_x + time_label_offset + 1,
                timeline_start_y + timeline_height + 4,
                fill=base_rgba,
                width=0,
            )

class TimerFrame(tk.Frame):
    def __init__(self, parent):
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
        self.detailsFrame.grid(column=1, row=0, sticky=('N', 'S', 'E', 'W'), padx=12, pady=(12, 0))

        self.progressFrame = tk.Frame(self)
        self.progressFrame.grid(column=1, row=1, sticky=('N', 'S', 'E', 'W'))

        self.detailsContent = TimerDetailsFrame(self.detailsFrame)
        self.progressContent = TimerProgressFrame(self.progressFrame)
