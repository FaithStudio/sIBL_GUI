#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**listImports.py

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Lists Application imports.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import logging
import re
import sys

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.core as core
import foundations.walkers
from foundations.io import File
from foundations.globals.constants import Constants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2012 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "LOGGING_CONSOLE_HANDLER", "IMPORTS", "FILTERS_IN", "FILTERS_OUT", "listImports"]

LOGGER = logging.getLogger(Constants.logger)

LOGGING_CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
LOGGING_CONSOLE_HANDLER.setFormatter(core.LOGGING_DEFAULT_FORMATTER)
LOGGER.addHandler(LOGGING_CONSOLE_HANDLER)

core.setVerbosityLevel(3)

IMPORTS = ["PyQt.uic"]

FILTERS_IN = ("\.py$",)
FILTERS_OUT = ("defaultScript\.py", "tests")

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
def listImports(sourceDirectory, filtersIn, filtersOut):
	"""
	This definition lists Application imports.

	:param sourceDirectory: Source directory. ( String )
	:param filtersIn: Filters in. ( Tuple / List )
	:param filtersOut: Filters out. ( Tuple / List )
	:return: Imports. ( List )
	"""

	imports = IMPORTS
	for file in sorted(list(foundations.walkers.filesWalker(sourceDirectory, filtersIn, filtersOut))):
		source = File(file)
		source.read()
		for line in source.content:
			if not re.search("foundations|manager|umbra|sibl_gui", line):
				search = re.search("^\s*import\s*(?P<moduleA>[\w+\.]+)|^\s*from\s*(?P<moduleB>[\w+\.]+)\s+import", line)
				if search:
					statement = search.group("moduleA") or search.group("moduleB")
					statement not in imports and statement != "_" and imports.append(statement)
	return imports

if __name__ == "__main__":
	imports = listImports(sys.argv[1], filtersIn=FILTERS_IN, filtersOut=FILTERS_OUT)
	LOGGER.info("{0} | Imports: \"{1}\"".format(listImports.__name__, ",".join(sorted(imports))))