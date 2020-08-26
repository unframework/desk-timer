# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import imgui
import imgui.extra
import math

from icons import *

def init_timer_screen():
    rgba_format = SDL_AllocFormat(SDL_PIXELFORMAT_RGBA32)
    raw_image_path = '%s/clock-face-mockup.png' % os.path.dirname(os.path.abspath(__file__))
    raw_image = IMG_Load(raw_image_path.encode('utf-8'))

    try:
        rgba_image = SDL_ConvertSurface(raw_image, rgba_format, 0)

        try:
            if rgba_image.contents.format.contents.BytesPerPixel != 4:
                raise Exception('expecting RGBA')

            surface = rgba_image.contents
            pixel_count = surface.w * surface.h * 4
            pixel_data = ctypes.create_string_buffer(b'', pixel_count)
            ctypes.memmove(pixel_data, surface.pixels, pixel_count)

            clock_mock_texture = gl.glGenTextures(1)

            gl.glBindTexture(gl.GL_TEXTURE_2D, clock_mock_texture)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
            gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, surface.w, surface.h, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, pixel_data.raw)

        finally:
            SDL_FreeSurface(rgba_image)

    finally:
        SDL_FreeSurface(raw_image)
        SDL_FreeFormat(rgba_format)

    return clock_mock_texture

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

def chart_ui():
    (pos_x, pos_y) = imgui.get_cursor_screen_pos()
    base_rgba = imgui.get_color_u32_rgba(.25, .25, .25, 1)
    filled_rgba = imgui.get_color_u32_rgba(.25, .75, .25, 1)
    active_rgba = imgui.get_color_u32_rgba(1, 1, 1, 1)

    draw_list = imgui.get_window_draw_list()

    timeline_offset_y = 12
    timeline_height = 8

    for i in range(96):
        offset_x = i * 3
        rgba = active_rgba if i == 35 else (
            filled_rgba if (i > 18 and i < 22) or (i > 28 and i < 35) else (
                base_rgba
            )
        )

        draw_list.add_rect_filled(
            pos_x + offset_x,
            pos_y + timeline_offset_y,
            pos_x + offset_x + 2,
            pos_y + timeline_offset_y + timeline_height,
            rgba
        )

def timer_screen(icon_texture, clock_mock_texture):
    imgui.columns(2, None, False)
    imgui.set_column_width(0, 150)

    imgui.begin_child("Clock")
    (area_w, area_h) = imgui.get_content_region_available()
    (pos_x, pos_y) = imgui.get_cursor_pos()
    imgui.set_cursor_pos((pos_x + (area_w - 128) / 2, pos_y + (area_h - 128) / 2))
    imgui.image(clock_mock_texture, 128, 128)
    imgui.end_child()

    imgui.next_column()

    imgui.begin_child("Stats", 0, -32)
    stats_ui()
    imgui.end_child()

    imgui.begin_child("Chart", 0, 28)
    # (chart_w, chart_h) = imgui.get_content_region_available()
    chart_ui()
    imgui.end_child()

    imgui.next_column()

    imgui.columns(1)
    # icon_image(icon_texture, UIICON_HAND)
