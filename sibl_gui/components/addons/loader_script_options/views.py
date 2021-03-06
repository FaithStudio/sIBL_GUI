#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**views.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Defines the :class:`sibl_gui.components.addons.loader_script_options.loader_script_options.LoaderScriptOptions`
    Component Interface class Views.

**Others:**

"""

import foundations.verbose
import umbra.ui.views

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "TemplatesAttributes_QTableWidget"]

LOGGER = foundations.verbose.install_logger()


class TemplatesAttributes_QTableWidget(umbra.ui.views.Abstract_QTableWidget):
    """
    Defines the view for Templates attributes.
    """

    pass
