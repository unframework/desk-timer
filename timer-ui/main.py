# -*- coding: utf-8 -*-
from __future__ import absolute_import

import imgui
import imgui.extra
import math

from imgui_integration import SDL2Renderer
from icons import *

from timer_screen import init_timer_screen, timer_screen

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

def button_label(icon_texture, icon_pos, label):
    (_, area_h) = imgui.get_content_region_available()
    pos_y = imgui.get_cursor_pos_y()

    # extra spacing for now
    imgui.dummy(4, 0)
    imgui.same_line()

    imgui.set_cursor_pos_y(pos_y + (area_h - ICON_SIZE) / 2)
    icon_image(icon_texture, icon_pos)
    imgui.set_cursor_pos_y(pos_y)

    imgui.same_line()

    imgui.set_cursor_pos_y(pos_y + (area_h - imgui.get_text_line_height()) / 2)
    imgui.text(label)
    imgui.set_cursor_pos_y(pos_y)

# from PyImgui examples
def main():
    imgui.create_context()
    renderer = SDL2Renderer(SCREEN_W, SCREEN_H)

    imgui.push_style_var(imgui.STYLE_WINDOW_ROUNDING, 0.0);

    icon_texture = init_icons()
    clock_mock_texture = init_timer_screen()

    frame = 1

    while renderer.process_events():
        imgui.new_frame()

        imgui.set_next_window_position(0, MAIN_MINY)
        imgui.set_next_window_size(SCREEN_W, SCREEN_H - MAIN_MINY)
        imgui.set_next_window_focus()
        imgui.begin("Productivity Timer", False, WINDOW_FLAGS)
        timer_screen(icon_texture, clock_mock_texture)
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

            with renderer.label_font():
                button_label(icon_texture, UIICON_BRICK, 'Menu')
            imgui.next_column()

            imgui.dummy(-1, 1) # TODO fill these in with black to separate label bgs
            imgui.next_column()

            with renderer.label_font():
                button_label(icon_texture, UIICON_HAND, 'Pause')
            imgui.next_column()

            imgui.dummy(-1, 1)
            imgui.next_column()

            with renderer.label_font():
                button_label(icon_texture, UIICON_HOURGLASS, '+1min')
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
