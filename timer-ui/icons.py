import os

import ctypes
from sdl2 import *
from sdl2.sdlimage import *
import OpenGL.GL as gl
import imgui

UIICON_BRICK = (0, 0)
UIICON_HAND = (1, 0)
UIICON_HOURGLASS = (2, 0)

ICON_SIZE = 32

_icon_uv_size = 0.25

def init_icons():
    rgbaFormat = SDL_AllocFormat(SDL_PIXELFORMAT_RGBA32)
    raw_image_path = '%s/icons.png' % os.path.dirname(os.path.abspath(__file__))
    rawImage = IMG_Load(raw_image_path.encode('utf-8'))

    try:
        rgbaImage = SDL_ConvertSurface(rawImage, rgbaFormat, 0)

        try:
            if rgbaImage.contents.format.contents.BytesPerPixel != 4:
                raise Exception('expecting RGBA')

            surface = rgbaImage.contents
            pixel_count = surface.w * surface.h * 4
            pixel_data = ctypes.create_string_buffer(b'', pixel_count)
            ctypes.memmove(pixel_data, surface.pixels, pixel_count)

            icon_texture = gl.glGenTextures(1)

            gl.glBindTexture(gl.GL_TEXTURE_2D, icon_texture)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_NEAREST)
            gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
            gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, surface.w, surface.h, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, pixel_data.raw)

        finally:
            SDL_FreeSurface(rgbaImage)

    finally:
        SDL_FreeSurface(rawImage)
        SDL_FreeFormat(rgbaFormat)

    return icon_texture

def icon_image(icon_texture, icon_pos):
    icon_x, icon_y = icon_pos
    uv0 = (icon_x * _icon_uv_size, icon_y * _icon_uv_size)
    uv1 = (uv0[0] + _icon_uv_size, uv0[1] + _icon_uv_size)
    imgui.image(icon_texture, ICON_SIZE, ICON_SIZE, uv0, uv1)
