# -*- coding: utf-8 -*-
from __future__ import absolute_import

from sdl2 import *

import imgui
import imgui.extra
import math
import ctypes

from imgui.integrations.opengl import FixedPipelineRenderer

import OpenGL.GL as gl

# from PyImgui SDL2Renderer
class SDL2Renderer(FixedPipelineRenderer):
    """Basic SDL2 integration implementation."""
    MOUSE_WHEEL_OFFSET_SCALE = 0.5

    def __init__(self, window):
        super(SDL2Renderer, self).__init__()
        self.window = window

        self._mouse_pressed = [False, False, False]
        self._mouse_wheel = 0.0
        self._gui_time = None

        width_ptr = ctypes.pointer(ctypes.c_int(0))
        height_ptr = ctypes.pointer(ctypes.c_int(0))
        SDL_GetWindowSize(self.window, width_ptr, height_ptr)

        self.io.display_size = width_ptr[0], height_ptr[0]
        # self.io.get_clipboard_text_fn = self._get_clipboard_text
        # self.io.set_clipboard_text_fn = self._set_clipboard_text

        self._map_keys()

    def _get_clipboard_text(self):
        return SDL_GetClipboardText()

    def _set_clipboard_text(self, text):
        SDL_SetClipboardText(ctypes.c_char_p(text.encode()))

    def _map_keys(self):
        key_map = self.io.key_map

        key_map[imgui.KEY_TAB] = SDLK_TAB
        key_map[imgui.KEY_LEFT_ARROW] = SDL_SCANCODE_LEFT
        key_map[imgui.KEY_RIGHT_ARROW] = SDL_SCANCODE_RIGHT
        key_map[imgui.KEY_UP_ARROW] = SDL_SCANCODE_UP
        key_map[imgui.KEY_DOWN_ARROW] = SDL_SCANCODE_DOWN
        key_map[imgui.KEY_PAGE_UP] = SDL_SCANCODE_PAGEUP
        key_map[imgui.KEY_PAGE_DOWN] = SDL_SCANCODE_PAGEDOWN
        key_map[imgui.KEY_HOME] = SDL_SCANCODE_HOME
        key_map[imgui.KEY_END] = SDL_SCANCODE_END
        key_map[imgui.KEY_DELETE] = SDLK_DELETE
        key_map[imgui.KEY_BACKSPACE] = SDLK_BACKSPACE
        key_map[imgui.KEY_ENTER] = SDLK_RETURN
        key_map[imgui.KEY_ESCAPE] = SDLK_ESCAPE
        key_map[imgui.KEY_A] = SDLK_a
        key_map[imgui.KEY_C] = SDLK_c
        key_map[imgui.KEY_V] = SDLK_v
        key_map[imgui.KEY_X] = SDLK_x
        key_map[imgui.KEY_Y] = SDLK_y
        key_map[imgui.KEY_Z] = SDLK_z

    def process_event(self, event):
        io = self.io

        if event.type == SDL_MOUSEWHEEL:
            self._mouse_wheel = event.wheel.y * self.MOUSE_WHEEL_OFFSET_SCALE
            return True

        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.button.button == SDL_BUTTON_LEFT:
                self._mouse_pressed[0] = True
            if event.button.button == SDL_BUTTON_RIGHT:
                self._mouse_pressed[1] = True
            if event.button.button == SDL_BUTTON_MIDDLE:
                self._mouse_pressed[2] = True
            return True

        if event.type == SDL_KEYUP or event.type == SDL_KEYDOWN:
            key = event.key.keysym.sym & ~SDLK_SCANCODE_MASK

            if key < SDL_NUM_SCANCODES:
                io.keys_down[key] = event.type == SDL_KEYDOWN

            io.key_shift = ((SDL_GetModState() & KMOD_SHIFT) != 0)
            io.key_ctrl = ((SDL_GetModState() & KMOD_CTRL) != 0)
            io.key_alt = ((SDL_GetModState() & KMOD_ALT) != 0)
            io.key_super = ((SDL_GetModState() & KMOD_GUI) != 0)

            return True

        if event.type == SDL_TEXTINPUT:
            for char in event.text.text.decode('utf-8'):
                io.add_input_character(ord(char))
            return True

    def process_inputs(self):
        io = imgui.get_io()

        s_w = ctypes.pointer(ctypes.c_int(0))
        s_h = ctypes.pointer(ctypes.c_int(0))
        SDL_GetWindowSize(self.window, s_w, s_h)
        w = s_w.contents.value
        h = s_h.contents.value

        io.display_size = w, h
        io.display_fb_scale = 1, 1

        current_time = SDL_GetTicks() / 1000.0

        if self._gui_time:
            self.io.delta_time = current_time - self._gui_time
        else:
            self.io.delta_time = 1. / 60.
        self._gui_time = current_time

        mx = ctypes.pointer(ctypes.c_int(0))
        my = ctypes.pointer(ctypes.c_int(0))
        mouse_mask = SDL_GetMouseState(mx, my)

        if SDL_GetWindowFlags(self.window) & SDL_WINDOW_MOUSE_FOCUS:
            io.mouse_pos = mx.contents.value, my.contents.value
        else:
            io.mouse_pos = -1, -1

        io.mouse_down[0] = self._mouse_pressed[0] or (mouse_mask & SDL_BUTTON(SDL_BUTTON_LEFT)) != 0
        io.mouse_down[1] = self._mouse_pressed[1] or (mouse_mask & SDL_BUTTON(SDL_BUTTON_RIGHT)) != 0
        io.mouse_down[2] = self._mouse_pressed[2] or (mouse_mask & SDL_BUTTON(SDL_BUTTON_MIDDLE)) != 0
        self._mouse_pressed = [False, False, False]

        io.mouse_wheel = self._mouse_wheel
        self._mouse_wheel = 0

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
    window, gl_context = impl_pysdl2_init()
    imgui.create_context()
    impl = SDL2Renderer(window)

    imgui.push_style_var(imgui.STYLE_WINDOW_ROUNDING, 0.0);

    frame = 1
    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
            impl.process_event(event)
        impl.process_inputs()

        imgui.new_frame()

        # imgui.set_next_window_position(8 + frame % 50, 8 + frame % 50)
        imgui.set_next_window_position(0, MAIN_MINY)
        imgui.set_next_window_size(SCREEN_W, SCREEN_H - MAIN_MINY)
        imgui.set_next_window_focus()
        imgui.begin("Custom window", False, WINDOW_FLAGS)
        imgui.text("Bar")
        imgui.text_colored("Eggs and ham? Some rhyme here", 0.0, 1.0, 0.2)
        imgui.text_colored("Eggs and ham? Some rhyme here", 0.0, 1.0, 0.2)
        imgui.text_colored("Eggs and ham? Some rhyme here", 0.0, 1.0, 0.2)
        imgui.text_colored("Eggs and ham? Some rhyme here", 0.0, 1.0, 0.2)
        imgui.text_colored("Eggs and ham? Some rhyme here", 0.0, 1.0, 0.2)
        imgui.text_colored("Eggs and ham? Some rhyme here", 0.0, 1.0, 0.2)
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
        draw_data = imgui.get_draw_data()
        impl.render(draw_data)
        SDL_GL_SwapWindow(window)

        frame += 1

    impl.shutdown()
    SDL_GL_DeleteContext(gl_context)
    SDL_DestroyWindow(window)
    SDL_Quit()


def impl_pysdl2_init():
    width, height = SCREEN_W, SCREEN_H
    window_name = "minimal ImGui/SDL2 example"

    if SDL_Init(SDL_INIT_EVERYTHING) < 0:
        print("Error: SDL could not initialize! SDL Error: " + SDL_GetError().decode())
        exit(1)

    # SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1)
    # SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24)
    # SDL_GL_SetAttribute(SDL_GL_STENCIL_SIZE, 8)
    # SDL_GL_SetAttribute(SDL_GL_ACCELERATED_VISUAL, 1)
    # SDL_GL_SetAttribute(SDL_GL_MULTISAMPLEBUFFERS, 1)
    # SDL_GL_SetAttribute(SDL_GL_MULTISAMPLESAMPLES, 16)
    # SDL_GL_SetAttribute(SDL_GL_CONTEXT_FLAGS, SDL_GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
    # SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4)
    # SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 1)
    # SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE)

    SDL_SetHint(SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK, b"1")
    SDL_SetHint(SDL_HINT_VIDEO_HIGHDPI_DISABLED, b"1")

    window = SDL_CreateWindow(window_name.encode('utf-8'),
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              width, height,
                              SDL_WINDOW_OPENGL)

    if window is None:
        print("Error: Window could not be created! SDL Error: " + SDL_GetError().decode())
        exit(1)

    gl_context = SDL_GL_CreateContext(window)
    if gl_context is None:
        print("Error: Cannot create OpenGL Context! SDL Error: " + SDL_GetError().decode())
        exit(1)

    SDL_GL_MakeCurrent(window, gl_context)
    if SDL_GL_SetSwapInterval(1) < 0:
        print("Warning: Unable to set VSync! SDL Error: " + SDL_GetError().decode())
        # exit(1)

    return window, gl_context


if __name__ == "__main__":
    main()
