################################################################################
#
# python-pyopengl
#
################################################################################

PYTHON_PYOPENGL_VERSION = 3.1.5
PYTHON_PYOPENGL_SOURCE = PyOpenGL-$(PYTHON_PYOPENGL_VERSION).tar.gz
PYTHON_PYOPENGL_SITE = https://files.pythonhosted.org/packages/b8/73/31c8177f3d236e9a5424f7267659c70ccea604dab0585bfcd55828397746
PYTHON_PYOPENGL_SETUP_TYPE = setuptools
PYTHON_PYOPENGL_LICENSE = FIXME: license id couldn't be detected
PYTHON_PYOPENGL_LICENSE_FILES = license.txt

$(eval $(python-package))
