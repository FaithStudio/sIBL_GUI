#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**imagesCachesOperations.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines the :class:`ImagesCachesOperations` Component Interface class.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import logging
import os
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QMessageBox

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.core as core
import foundations.exceptions
import sibl_gui.exceptions
import umbra.ui.common
import umbra.ui.widgets.messageBox as messageBox
from manager.qwidgetComponent import QWidgetComponentFactory
from umbra.globals.constants import Constants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "COMPONENT_UI_FILE", "ImagesCachesOperations"]

LOGGER = logging.getLogger(Constants.logger)

COMPONENT_UI_FILE = os.path.join(os.path.dirname(__file__), "ui", "Images_Caches_Operations.ui")

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class ImagesCachesOperations(QWidgetComponentFactory(uiFile=COMPONENT_UI_FILE)):
	"""
	| This class is the :mod:`umbra.components.addons.imagesCachesOperations.imagesCachesOperations` Component Interface class.
	| It provides various methods to operate on the images caches.
	"""

	@core.executionTrace
	def __init__(self, parent=None, name=None, *args, **kwargs):
		"""
		This method initializes the class.

		:param parent: Object parent. ( QObject )
		:param name: Component name. ( String )
		:param \*args: Arguments. ( \* )
		:param \*\*kwargs: Keywords arguments. ( \*\* )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		super(ImagesCachesOperations, self).__init__(parent, name, *args, **kwargs)

		# --- Setting class attributes. ---
		self.deactivatable = True

		self.__engine = None

		self.__factoryPreferencesManager = None

		self.__editLayout = "editCentric"

	#******************************************************************************************************************
	#***	Attributes properties.
	#******************************************************************************************************************
	@property
	def engine(self):
		"""
		This method is the property for **self.__engine** attribute.

		:return: self.__engine. ( QObject )
		"""

		return self.__engine

	@engine.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def engine(self, value):
		"""
		This method is the setter method for **self.__engine** attribute.

		:param value: Attribute value. ( QObject )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "engine"))

	@engine.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def engine(self):
		"""
		This method is the deleter method for **self.__engine** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "engine"))

	@property
	def factoryPreferencesManager(self):
		"""
		This method is the property for **self.__factoryPreferencesManager** attribute.

		:return: self.__factoryPreferencesManager. ( Object )
		"""

		return self.__factoryPreferencesManager

	@factoryPreferencesManager.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def factoryPreferencesManager(self, value):
		"""
		This method is the setter method for **self.__factoryPreferencesManager** attribute.

		:param value: Attribute value. ( Object )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "factoryPreferencesManager"))

	@factoryPreferencesManager.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def factoryPreferencesManager(self):
		"""
		This method is the deleter method for **self.__factoryPreferencesManager** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "factoryPreferencesManager"))

	@property
	def editLayout(self):
		"""
		This method is the property for **self.__editLayout** attribute.

		:return: self.__editLayout. ( String )
		"""

		return self.__editLayout

	@editLayout.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def editLayout(self, value):
		"""
		This method is the setter method for **self.__editLayout** attribute.

		:param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "editLayout"))

	@editLayout.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def editLayout(self):
		"""
		This method is the deleter method for **self.__editLayout** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "editLayout"))

	#******************************************************************************************************************
	#***	Class methods.
	#******************************************************************************************************************
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def activate(self, engine):
		"""
		This method activates the Component.

		:param engine: Engine to attach the Component to. ( QObject )
		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Activating '{0}' Component.".format(self.__class__.__name__))

		self.__engine = engine
		self.__settings = self.__engine.settings
		self.__settingsSection = self.name

		self.__factoryPreferencesManager = self.__engine.componentsManager.components[
											"factory.preferencesManager"].interface
		self.activated = True
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def deactivate(self):
		"""
		This method deactivates the Component.

		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Deactivating '{0}' Component.".format(self.__class__.__name__))

		self.__engine = None
		self.__settings = None
		self.__settingsSection = None

		self.__factoryPreferencesManager = None

		self.activated = False
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def initializeUi(self):
		"""
		This method initializes the Component ui.
		
		:return: Method success. ( Boolean )		
		"""

		LOGGER.debug("> Initializing '{0}' Component ui.".format(self.__class__.__name__))

		# Signals / Slots.
		self.Output_Images_Caches_Metrics_pushButton.clicked.connect(self.__Output_Images_Caches_Metrics_pushButton__clicked)
		self.Clear_Images_Caches_pushButton.clicked.connect(self.__Clear_Images_Caches_pushButton__clicked)

		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def uninitializeUi(self):
		"""
		This method uninitializes the Component ui.
		
		:return: Method success. ( Boolean )		
		"""

		LOGGER.debug("> Uninitializing '{0}' Component ui.".format(self.__class__.__name__))

		# Signals / Slots.
		self.Output_Images_Caches_Metrics_pushButton.clicked.disconnect(self.__Output_Images_Caches_Metrics_pushButton__clicked)
		self.Clear_Images_Caches_pushButton.clicked.disconnect(self.__Clear_Images_Caches_pushButton__clicked)

		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def addWidget(self):
		"""
		This method adds the Component Widget to the engine.

		:return: Method success. ( Boolean )		
		"""

		LOGGER.debug("> Adding '{0}' Component Widget.".format(self.__class__.__name__))

		self.__factoryPreferencesManager.Others_Preferences_gridLayout.addWidget(self.Images_Caches_Operations_groupBox)

		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def removeWidget(self):
		"""
		This method removes the Component Widget from the engine.

		:return: Method success. ( Boolean )		
		"""

		LOGGER.debug("> Removing '{0}' Component Widget.".format(self.__class__.__name__))

		self.__factoryPreferencesManager.findChild(QGridLayout, "Others_Preferences_gridLayout").removeWidget(self)
		self.Images_Caches_Operations_groupBox.setParent(None)

		return True

	@core.executionTrace
	def __Clear_Images_Caches_pushButton__clicked(self, checked):
		"""
		This method is triggered when **Clear_Images_Caches_pushButton** Widget is clicked.

		:param checked: Checked state. ( Boolean )
		"""

		self.clearImagesCaches()

	@core.executionTrace
	def __Output_Images_Caches_Metrics_pushButton__clicked(self, checked):
		"""
		This method is triggered when **Output_Images_Caches_Metrics_pushButton** Widget is clicked.

		:param checked: Checked state. ( Boolean )
		"""

		self.outputImagesCachesMetrics()
		self.__engine.currentLayout != self.__editLayout and self.__engine.restoreLayout(self.__editLayout)

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def outputImagesCachesMetrics(self):
		"""
		This method logs images caches metrics.

		:return: Method success. ( Boolean )
		"""

		separator = "{0}".format(Constants.loggingSeparators.replace("*", "-"))
		for type, cache in self.__engine.imagesCaches.iteritems():
			LOGGER.info(separator)
			LOGGER.info("{0} | Metrics for '{1}' '{2}' images cache:".format(self.__class__.__name__,
																			Constants.applicationName, type))
			cacheMetrics = cache.getMetrics().content
			LOGGER.info("{0} | \tCached graphics items count: '{1}'".format(self.__class__.__name__, len(cacheMetrics)))
			for path, data in sorted(cache.getMetrics().content.iteritems()):
				LOGGER.info("{0} | \t\t'{1}':".format(self.__class__.__name__, path))
				LOGGER.info("{0} | \t\t\tSize: {1}x{2} px".format(self.__class__.__name__, data.width, data.height))
				LOGGER.info("{0} | \t\t\tBpp: {1} bit".format(self.__class__.__name__, data.bpp / 4))
			LOGGER.info(separator)
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(umbra.ui.common.uiBasicExceptionHandler,
											False,
											sibl_gui.exceptions.CacheOperationError)
	def clearImagesCaches(self):
		"""

		:return: Method success. ( Boolean )
		"""

		success = True
		for cache in self.__engine.imagesCaches.itervalues():
			success *= cache.flushContent()

		if success:
			messageBox.messageBox("Information", "Information",
			"{0} | Images caches have been successfully cleared!".format(self.__class__.__name__),
			QMessageBox.Information, QMessageBox.Ok)
			return True
		else:
			raise sibl_gui.exceptions.CacheOperationError(
				"{0} | Exception raised while attempting to clear images caches!".format(
				self.__class__.__name__))
