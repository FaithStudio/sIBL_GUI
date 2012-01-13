#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**application_QToolBar.py.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines the :class:`Application_QToolBar` class.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import logging
from PyQt4.QtCore import QString
from PyQt4.QtCore import QUrl
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QPixmap

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.core as core
import foundations.exceptions
import umbra.guerilla
import umbra.ui.widgets.application_QToolBar
from umbra.globals.constants import Constants
from umbra.globals.uiConstants import UiConstants
from umbra.ui.widgets.active_QLabel import Active_QLabel
from umbra.ui.widgets.active_QLabelsCollection import Active_QLabelsCollection

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2012 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "Application_QToolBar"]

LOGGER = logging.getLogger(Constants.logger)

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class Application_QToolBar(umbra.ui.widgets.application_QToolBar.Application_QToolBar):
	"""
	This class is defines the Application toolbar.
	"""

	__metaclass__ = umbra.guerilla.baseWarfare

	#******************************************************************************************************************
	#***	Class methods.
	#******************************************************************************************************************
	@core.executionTrace
	def __centralWidgetButton__clicked(self):
		"""
		This method sets the **Central** Widget visibility.
		"""

		LOGGER.debug("> Central Widget button clicked!")

		if self.__container.centralwidget.isVisible():
			self.__container.centralwidget.hide()
		else:
			self.__container.centralwidget.show()

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def setToolBarChildrenWidgets(self):
		"""
		This method sets the toolBar children widgets.

		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Adding 'Application_Logo_label' widget!")
		self.addWidget(self.getApplicationLogoLabel())

		LOGGER.debug("> Adding 'Spacer_label' widget!")
		self.addWidget(self.getSpacerLabel())

		LOGGER.debug("> Adding 'Library_activeLabel', \
					'Inspect_activeLabel', \
					'Export_activeLabel', \
					'Edit_activeLabel', \
					'Preferences_activeLabel' \
					widgets!")
		for layoutActiveLabel in self.getLayoutsActiveLabels():
			self.addWidget(layoutActiveLabel)

		LOGGER.debug("> Adding 'Central_Widget_activeLabel' widget!")
		self.addWidget(self.getCentralWidgetActiveLabel())

		LOGGER.debug("> Adding 'Custom_Layouts_activeLabel' widget!")
		self.addWidget(self.getCustomLayoutsActiveLabel())

		LOGGER.debug("> Adding 'Miscellaneous_activeLabel' widget!")
		self.addWidget(self.getMiscellaneousActiveLabel())
		self.extendMiscellaneousActiveLabel()

		LOGGER.debug("> Adding 'Closure_Spacer_label' widget!")
		self.addWidget(self.getClosureSpacerLabel())

		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def getLayoutsActiveLabels(self):
		"""
		This method returns the layouts **Active_QLabel** widgets.

		:return: Layouts active labels. ( List )
		"""

		self.__layoutsActiveLabelsCollection = Active_QLabelsCollection(self)

		self.__layoutsActiveLabelsCollection.addActiveLabel(self.getLayoutActiveLabel((UiConstants.libraryIcon,
																					UiConstants.libraryHoverIcon,
																					UiConstants.libraryActiveIcon),
																					"Library_activeLabel",
																					"Library",
																					"setsCentric",
																					Qt.Key_6))

		self.__layoutsActiveLabelsCollection.addActiveLabel(self.getLayoutActiveLabel((UiConstants.inspectIcon,
																					UiConstants.inspectHoverIcon,
																					UiConstants.inspectActiveIcon),
																					"Inspect_activeLabel",
																					"Inspect",
																					"inspectCentric",
																					Qt.Key_7))

		self.__layoutsActiveLabelsCollection.addActiveLabel(self.getLayoutActiveLabel((UiConstants.exportIcon,
																					UiConstants.exportHoverIcon,
																					UiConstants.exportActiveIcon),
																					"Export_activeLabel",
																					"Export",
																					"templatesCentric",
																					Qt.Key_8))

		self.__layoutsActiveLabelsCollection.addActiveLabel(self.getLayoutActiveLabel((UiConstants.editIcon,
																					UiConstants.editHoverIcon,
																					UiConstants.editActiveIcon),
																					"Edit_activeLabel",
																					"Edit",
																					"editCentric",
																					Qt.Key_9))

		self.__layoutsActiveLabelsCollection.addActiveLabel(self.getLayoutActiveLabel((UiConstants.preferencesIcon,
																					UiConstants.preferencesHoverIcon,
																					UiConstants.preferencesActiveIcon),
																					"Preferences_activeLabel",
																					"Preferences",
																					"preferencesCentric",
																					Qt.Key_0))
		return self.__layoutsActiveLabelsCollection.activeLabels
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def getCentralWidgetActiveLabel(self):
		"""
		This method provides the default **Central_Widget_activeLabel** widget.

		:return: Central Widget active label. ( Active_QLabel )
		"""

		centralWidgetButton = Active_QLabel(self,
											QPixmap(umbra.ui.common.getResourcePath(UiConstants.centralWidgetIcon)),
											QPixmap(umbra.ui.common.getResourcePath(UiConstants.centralWidgetHoverIcon)),
											QPixmap(umbra.ui.common.getResourcePath(UiConstants.centralWidgetActiveIcon)))
		centralWidgetButton.setObjectName("Central_Widget_activeLabel")

		# Signals / Slots.
		centralWidgetButton.clicked.connect(self.__centralWidgetButton__clicked)
		return centralWidgetButton

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def extendMiscellaneousActiveLabel(self):
		"""
		This method extends the default **Miscellaneous_activeLabel** widget.

		:return: Method success. ( Boolean )
		"""

		self.miscellaneousMenu.addAction(self.__container.actionsManager.registerAction(
		"Actions|Umbra|ToolBar|Miscellaneous|Make A Donation ...",
		slot=self.__makeDonationDisplayMiscAction__triggered))
		self.miscellaneousMenu.addSeparator()
		return True

	@core.executionTrace
	def __makeDonationDisplayMiscAction__triggered(self, checked):
		"""
		This method is triggered by **'Actions|Umbra|ToolBar|Miscellaneous|Make A Donation ...'** action.

		:param checked: Checked state. ( Boolean )
		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Opening url: '{0}'.".format(UiConstants.makeDonationFile))
		QDesktopServices.openUrl(QUrl(QString(UiConstants.makeDonationFile)))
		return True