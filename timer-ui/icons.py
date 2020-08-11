import OpenGL.GL as gl

def init_icons():
    width, height, pixels = (2, 2, bytes([
        0, 0, 0, 0,
        255, 255, 255, 255,
        255, 255, 255, 255,
        0, 0, 0, 0,
    ]))

    icon_texture = gl.glGenTextures(1)

    gl.glBindTexture(gl.GL_TEXTURE_2D, icon_texture)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
    gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
    gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, width, height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, pixels)

    return icon_texture
