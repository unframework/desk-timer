################################################################################
#
# python-pysdl2
#
################################################################################

PYTHON_PYSDL2_VERSION = 0.9.7
PYTHON_PYSDL2_SOURCE = PySDL2-$(PYTHON_PYSDL2_VERSION).tar.gz
PYTHON_PYSDL2_SITE = https://files.pythonhosted.org/packages/39/58/21d31ceba68b7d8c06be5ee620264bc91a5a7c69b796a7c32aae9e8b10bc
PYTHON_PYSDL2_SETUP_TYPE = setuptools
PYTHON_PYSDL2_LICENSE = FIXME: license id couldn't be detected
PYTHON_PYSDL2_LICENSE_FILES = COPYING.txt

$(eval $(python-package))
