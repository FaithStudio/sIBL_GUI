#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**get_dependencies_informations.py**

**Platform:**
    Windows, Linux, Mac Os X.

**Description:**
    Get dependencies informations.

**Others:**

"""

from __future__ import unicode_literals

import subprocess
import sys

if sys.version_info[:2] <= (2, 6):
    from ordereddict import OrderedDict
else:
    from collections import OrderedDict

import foundations.decorators
import foundations.verbose
from foundations.io import File

__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2014 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER",
           "GIT_EXECUTABLE",
           "ONCILLA_DIRECTORY",
           "FOUNDATIONS_DIRECTORY",
           "MANAGER_DIRECTORY",
           "UMBRA_DIRECTORY"
           "TEMPLATES_DIRECTORY",
           "DEPENDENCIES",
           "DEPENDENCIES_FILE",
           "get_dependencies_informations",
           "main"]

LOGGER = foundations.verbose.install_logger()

GIT_EXECUTABLE = "/usr/local/git/bin/git"
ONCILLA_DIRECTORY = "../../Oncilla"
FOUNDATIONS_DIRECTORY = "../../Foundations"
MANAGER_DIRECTORY = "../../Manager"
UMBRA_DIRECTORY = "../../Umbra"
TEMPLATES_DIRECTORY = "../../sIBL_GUI_Templates"
DEPENDENCIES = OrderedDict((("Oncilla", ONCILLA_DIRECTORY),
                            ("Foundations", FOUNDATIONS_DIRECTORY),
                            ("Manager", MANAGER_DIRECTORY),
                            ("Umbra", UMBRA_DIRECTORY),
                            ("sIBL_GUI_Templates", TEMPLATES_DIRECTORY)))
DEPENDENCIES_FILE = "../releases/sIBL_GUI_Dependencies.rc"

foundations.verbose.get_logging_console_handler()
foundations.verbose.set_verbosity_level(3)


def get_dependencies_informations():
    """
    Gets sIBL_GUI dependencies informations file.

    :return: Definition success.
    :rtype: bool
    """

    content = ["[Dependencies]\n"]
    for dependency, path in DEPENDENCIES.iteritems():
        release = subprocess.Popen("cd {0} && {1} describe".format(path, GIT_EXECUTABLE),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE).communicate()[0]
        LOGGER.info("{0} | '{1}': '{2}'.".format(get_dependencies_informations.__name__, dependency, release.strip()))
        content.append("{0}={1}".format(dependency, release))
    file = File(DEPENDENCIES_FILE)
    file.content = content
    file.write()

    return True


@foundations.decorators.system_exit
def main():
    """
    Starts the Application.

    :return: Definition success.
    :rtype: bool
    """

    return get_dependencies_informations()


if __name__ == "__main__":
    main()
