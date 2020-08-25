# -*- coding: utf-8 -*-
from __future__ import absolute_import

import imgui
import imgui.extra
import math

from icons import *

def stats_ui():
    imgui.columns(2, None, False)
    imgui.set_column_width(0, 110)

    imgui.text("Status")
    imgui.next_column()
    imgui.text_colored("ACTIVE", 0.25, 1.0, 0.25)
    imgui.next_column()

    imgui.text("Current time")
    imgui.next_column()
    imgui.text_colored("2020-08-25 20:23", 0.8, 0.8, 0.8)
    imgui.next_column()

    imgui.text("Start time")
    imgui.next_column()
    imgui.text_colored("2020-08-25 20:16", 0.8, 0.8, 0.8)
    imgui.next_column()

    imgui.text("Break time")
    imgui.next_column()
    imgui.text_colored("2020-08-25 20:41", 0.8, 0.8, 0.8)
    imgui.next_column()

    imgui.text("Elapsed")
    imgui.next_column()
    imgui.text_colored("12m", 0.8, 0.8, 0.8)
    imgui.next_column()

    imgui.text("Total elapsed")
    imgui.next_column()
    imgui.text_colored("2h 20m", 0.8, 0.8, 0.8)
    imgui.next_column()

    imgui.columns(1)

def timer_screen(icon_texture):
    imgui.columns(2, None, False)
    imgui.set_column_width(0, 160)
    imgui.next_column()
    imgui.begin_child("Stats", 0, -20)
    stats_ui()
    imgui.end_child()
    imgui.next_column()
    imgui.columns(1)
    # icon_image(icon_texture, UIICON_HAND)
