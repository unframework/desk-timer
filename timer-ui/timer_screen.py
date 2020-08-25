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

def timer_screen(icon_texture, clock_mock_texture):
    imgui.columns(2, None, False)
    imgui.set_column_width(0, 160)

    imgui.begin_child("Clock")
    (area_w, area_h) = imgui.get_content_region_available()
    (pos_x, pos_y) = imgui.get_cursor_pos()
    imgui.set_cursor_pos((pos_x + (area_w - 128) / 2, pos_y + (area_h - 128) / 2))
    imgui.image(clock_mock_texture, 128, 128)
    imgui.end_child()

    imgui.next_column()

    imgui.begin_child("Stats", 0, -20)
    stats_ui()
    imgui.end_child()
    imgui.next_column()

    imgui.columns(1)
    # icon_image(icon_texture, UIICON_HAND)
