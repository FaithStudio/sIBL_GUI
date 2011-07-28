#!/usr/bin/env python
# -*- coding: utf-8 -*-

#***********************************************************************************************
#
# Copyright (C) 2008 - 2011 - Thomas Mansencal - thomas.mansencal@gmail.com
#
#***********************************************************************************************
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#***********************************************************************************************
#
# The following code is protected by GNU GPL V3 Licence.
#

"""
**sIBL_GUI_getHDRLabsDocumentation.py

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	Extracts sIBL_GUI Documentation Body For HDRLabs.com.

**Others:**

"""

#***********************************************************************************************
#***	Python Begin.
#***********************************************************************************************
#***********************************************************************************************
#***	External Imports.
#***********************************************************************************************
import logging
import os
import sys
import re
from xml.etree import ElementTree

#***********************************************************************************************
#***	Internal Imports.
#***********************************************************************************************
import foundations.core as core
from foundations.io import File
from foundations.globals.constants import Constants

#***********************************************************************************************
#***	Global Variables.
#***********************************************************************************************
LOGGER = logging.getLogger(Constants.logger)

LOGGING_CONSOLE_HANDLER = logging.StreamHandler(sys.stdout)
LOGGING_CONSOLE_HANDLER.setFormatter(core.LOGGING_DEFAULT_FORMATTER)
LOGGER.addHandler(LOGGING_CONSOLE_HANDLER)

core.setVerbosityLevel(3)

#***********************************************************************************************
#***	Main Python Code.
#***********************************************************************************************
def getHDRLabsDocumentation(fileIn, fileOut):
	"""
	This Definition Extracts sIBL_GUI Documentation Body For HDRLabs.com.

	@param fileIn: File To Convert. ( String )
	@param fileOut: Output File. ( String )
	"""

	LOGGER.info("{0} | Extracting 'body' Tag Content From {1}' file!".format(getHDRLabsDocumentation.__name__, fileIn))
	file = File(fileIn)
	file.read()

	LOGGER.info("{0} | Building 'ElementTree' Parsing Tree!".format(getHDRLabsDocumentation.__name__))
	element = ElementTree.fromstringlist(file.content)
	tree = ElementTree.ElementTree(element)

	LOGGER.info("{0} | Processing 'body' Datas!".format(getHDRLabsDocumentation.__name__))
	content = ["{0}\n".format(line.replace("html:", "").replace("\t", "", 2)) for line in ElementTree.tostring(tree.find("{http://www.w3.org/1999/xhtml}body")).split("\n") if not re.search("<html:body.*", line) and not re.search("</html:body.*", line)]

	file = File(fileOut)
	file.content = content
	file.write()

if __name__ == "__main__":
	getHDRLabsDocumentation(sys.argv[1], sys.argv[2])

#***********************************************************************************************
#***	Python End.
#***********************************************************************************************
