################################################################################
#
# python-imgui
#
################################################################################

PYTHON_IMGUI_VERSION = 1.1.0
PYTHON_IMGUI_SOURCE = imgui-$(PYTHON_IMGUI_VERSION).tar.gz
PYTHON_IMGUI_SITE = https://files.pythonhosted.org/packages/91/70/fd945b94342732d11af0cf555c34fdb56adbd2a452b38cdc8782ee658257
PYTHON_IMGUI_SETUP_TYPE = setuptools
PYTHON_IMGUI_LICENSE = BSD-3-Clause
PYTHON_IMGUI_LICENSE_FILES = LICENSE

$(eval $(python-package))
