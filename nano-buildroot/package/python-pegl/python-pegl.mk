################################################################################
#
# python-pegl
#
################################################################################

PYTHON_PEGL_VERSION = 0.1a4_1.4
PYTHON_PEGL_SOURCE = Pegl-$(PYTHON_PEGL_VERSION).tar.gz
PYTHON_PEGL_SITE = https://files.pythonhosted.org/packages/29/ba/706b4ffc34f72b4884eb28290a319efa87edd6d06809d37b3d47663a19b4
PYTHON_PEGL_SETUP_TYPE = distutils
PYTHON_PEGL_LICENSE = GPL-3.0
PYTHON_PEGL_LICENSE_FILES = COPYING

$(eval $(python-package))
