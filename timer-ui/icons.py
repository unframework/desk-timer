import os

import ctypes
from sdl2 import *
from sdl2.sdlimage import *
import OpenGL.GL as gl

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
