# -*- coding: utf-8 -*-
from __future__ import absolute_import

import imgui
import imgui.extra
import math

from imgui_integration import SDL2Renderer
from icons import *

# constants
SCREEN_W = 480
SCREEN_H = 272

PADDING = 8

BUTTON_SPACE_W = 21 # this results in integer button widths
BUTTON_AREA_W = math.floor((SCREEN_W - BUTTON_SPACE_W * (3 - 1)) / 3)
BUTTON_ROW_H = 70
BUTTONS_IMGUI_ERROR_W = 5 # ImGui 1.65 seems to add extra padding on right side of columns?

MAIN_SPACE_H = 30
MAIN_MINY = BUTTON_ROW_H + MAIN_SPACE_H

WINDOW_FLAGS = imgui.WINDOW_NO_RESIZE | imgui.WINDOW_NO_MOVE | imgui.WINDOW_NO_COLLAPSE | imgui.WINDOW_NO_SAVED_SETTINGS

# from PyImgui examples
def main():
    imgui.create_context()
    renderer = SDL2Renderer(SCREEN_W, SCREEN_H)

    imgui.push_style_var(imgui.STYLE_WINDOW_ROUNDING, 0.0);

    icon_texture = init_icons()

    frame = 1

    while renderer.process_events():
        imgui.new_frame()

        # imgui.set_next_window_position(8 + frame % 50, 8 + frame % 50)
        imgui.set_next_window_position(0, MAIN_MINY)
        imgui.set_next_window_size(SCREEN_W, SCREEN_H - MAIN_MINY)
        imgui.set_next_window_focus()
        imgui.begin("Custom window", False, WINDOW_FLAGS)
        imgui.text("Bar")
        imgui.text_colored("Eggs and ham? Some rhyme here", 0.0, 1.0, 0.2)
        icon_image(icon_texture, UIICON_HAND)
        imgui.end()

        with imgui.extra.istyled(
            imgui.STYLE_WINDOW_BORDERSIZE, 0.0,
        ):
            imgui.set_next_window_position(0, 0)
            imgui.set_next_window_size(SCREEN_W + BUTTONS_IMGUI_ERROR_W, BUTTON_ROW_H)
            imgui.begin("Buttons", False, WINDOW_FLAGS | imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_SCROLLBAR)

            imgui.columns(3 + (3 - 1), None, False)
            imgui.set_column_width(0, BUTTON_AREA_W)
            imgui.set_column_width(1, BUTTON_SPACE_W)
            imgui.set_column_width(2, BUTTON_AREA_W)
            imgui.set_column_width(3, BUTTON_SPACE_W)
            imgui.set_column_width(4, BUTTON_AREA_W)

            imgui.button('Button A', -1, BUTTON_ROW_H - PADDING * 2)
            imgui.next_column()

            imgui.dummy(-1, 1)
            imgui.next_column()

            imgui.button('Button B', -1, BUTTON_ROW_H - PADDING * 2)
            imgui.next_column()

            imgui.dummy(-1, 1)
            imgui.next_column()

            with imgui.extra.colored(imgui.COLOR_BUTTON, 0.8, 0.4, 0.2):
                with imgui.extra.colored(imgui.COLOR_BUTTON_HOVERED, 1.0, 0.6, 0.2):
                    imgui.button('Button C', -1, BUTTON_ROW_H - PADDING * 2)
            imgui.next_column()

            imgui.columns(1)

            imgui.end()

        # gl.glClearColor(1., 1., 1., 1)
        # gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        imgui.render()
        renderer.render()

        frame += 1

    renderer.shutdown()

if __name__ == "__main__":
    main()
