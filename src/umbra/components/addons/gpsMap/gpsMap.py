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
#***********************************************************************************************
#
# If you are a HDRI resources vendor and are interested in making your sets SmartIBL compliant:
# Please contact us at HDRLabs:
# Christian Bloch - blochi@edenfx.com
# Thomas Mansencal - thomas.mansencal@gmail.com
#
#***********************************************************************************************

"""
**gpsMap.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	GPS Map Component Module.

**Others:**

"""

#***********************************************************************************************
#***	Python begin.
#***********************************************************************************************

#***********************************************************************************************
#***	External imports.
#***********************************************************************************************
import logging
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

#***********************************************************************************************
#***	Internal imports.
#***********************************************************************************************
import foundations.core as core
import foundations.exceptions
import foundations.strings as strings
import umbra.ui.common
from manager.uiComponent import UiComponent
from umbra.globals.constants import Constants

#***********************************************************************************************
#***	Global variables.
#***********************************************************************************************
LOGGER = logging.getLogger(Constants.logger)

#***********************************************************************************************
#***	Module classes and definitions.
#***********************************************************************************************
class Map(QWebView):
	"""
	This class is the QWebView class.
	"""

	@core.executionTrace
	def __init__(self, parent=None):
		"""
		This method initializes the class.

		@param parent: Widget parent. ( QObject )
		"""

		QWebView.__init__(self, parent)

	@core.executionTrace
	def addMarker(self, coordinates, title, icon, content):
		"""
		This method adds a marker to the map.

		@param coordinates: Marker coordinates. ( Tuple )
		@param title: Marker title. ( String )
		@param icon: Marker icon. ( String )
		@param content: Marker popup window content. ( String )
		@return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Adding '{0}' marker to gps map with '{1}' coordinates.".format(title, coordinates))

		self.page().mainFrame().evaluateJavaScript("addMarker( new Microsoft.Maps.Location({0},{1}),\"{2}\",\"{3}\",\"{4}\")".format(coordinates[0], coordinates[1], title, icon, content))
		return True

	@core.executionTrace
	def removeMarkers(self):
		"""
		This method removes the map markers.

		@return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Removing GPS map markers.")

		self.page().mainFrame().evaluateJavaScript("removeMarkers()")
		return True

	@core.executionTrace
	def setCenter(self):
		"""
		This method center the map.

		@return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Centering GPS map.")

		self.page().mainFrame().evaluateJavaScript("setCenter()")
		return True

	@core.executionTrace
	def setMapType(self, mapTypeId):
		"""
		This method sets the map type.

		@param mapTypeId: GPS map type. ( String )
		@return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Setting GPS map type to '{0}'.".format(mapTypeId))

		self.page().mainFrame().evaluateJavaScript("setMapType(\"{0}\")".format(mapTypeId))
		return True

	@core.executionTrace
	def setZoom(self, type):
		"""
		This method sets the map zoom.

		@param type: Zoom type. ( String )
		@return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Zooming '{0}' GPS map.".format(type))

		self.page().mainFrame().evaluateJavaScript("setZoom(\"{0}\")".format(type))
		return True

class GpsMap(UiComponent):
	"""
	This class is the GpsMap class.
	"""

	@core.executionTrace
	def __init__(self, name=None, uiFile=None):
		"""
		This method initializes the class.

		@param name: Component name. ( String )
		@param uiFile: Ui file. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		UiComponent.__init__(self, name=name, uiFile=uiFile)

		# --- Setting class attributes. ---
		self.deactivatable = True

		self.__uiPath = "ui/Gps_Map.ui"
		self.__uiResources = "resources"
		self.__uiZoomInImage = "Zoom_In.png"
		self.__uiZoomOutImage = "Zoom_Out.png"
		self.__gpsMapHtmlFile = "Bing_Maps.html"
		self.__gpsMapBaseSize = QSize(160, 100)
		self.__dockArea = 2

		self.__container = None

		self.__coreDatabaseBrowser = None

		self.__map = None
		self.__mapTypeIds = (("Auto", "MapTypeId.auto"), ("Aerial", "MapTypeId.aerial"), ("Road", "MapTypeId.road"))

	#***********************************************************************************************
	#***	Attributes properties.
	#***********************************************************************************************
	@property
	def uiPath(self):
		"""
		This method is the property for the _uiPath attribute.

		@return: self.__uiPath. ( String )
		"""

		return self.__uiPath

	@uiPath.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiPath(self, value):
		"""
		This method is the setter method for the _uiPath attribute.

		@param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("uiPath"))

	@uiPath.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiPath(self):
		"""
		This method is the deleter method for the _uiPath attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("uiPath"))

	@property
	def uiResources(self):
		"""
		This method is the property for the _uiResources attribute.

		@return: self.__uiResources. ( String )
		"""

		return self.__uiResources

	@uiResources.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiResources(self, value):
		"""
		This method is the setter method for the _uiResources attribute.

		@param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("uiResources"))

	@uiResources.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiResources(self):
		"""
		This method is the deleter method for the _uiResources attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("uiResources"))

	@property
	def uiZoomInImage(self):
		"""
		This method is the property for the _uiZoomInImage attribute.

		@return: self.__uiZoomInImage. ( String )
		"""

		return self.__uiZoomInImage

	@uiZoomInImage.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiZoomInImage(self, value):
		"""
		This method is the setter method for the _uiZoomInImage attribute.

		@param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("uiZoomInImage"))

	@uiZoomInImage.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiZoomInImage(self):
		"""
		This method is the deleter method for the _uiZoomInImage attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("uiZoomInImage"))

	@property
	def uiZoomOutImage(self):
		"""
		This method is the property for the _uiZoomOutImage attribute.

		@return: self.__uiZoomOutImage. ( String )
		"""

		return self.__uiZoomOutImage

	@uiZoomOutImage.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiZoomOutImage(self, value):
		"""
		This method is the setter method for the _uiZoomOutImage attribute.

		@param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("uiZoomOutImage"))

	@uiZoomOutImage.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def uiZoomOutImage(self):
		"""
		This method is the deleter method for the _uiZoomOutImage attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("uiZoomOutImage"))

	@property
	def gpsMapHtmlFile(self):
		"""
		This method is the property for the _gpsMapHtmlFile attribute.

		@return: self.__gpsMapHtmlFile. ( String )
		"""

		return self.__gpsMapHtmlFile

	@gpsMapHtmlFile.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def gpsMapHtmlFile(self, value):
		"""
		This method is the setter method for the _gpsMapHtmlFile attribute.

		@param value: Attribute value. ( String )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("gpsMapHtmlFile"))

	@gpsMapHtmlFile.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def gpsMapHtmlFile(self):
		"""
		This method is the deleter method for the _gpsMapHtmlFile attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("gpsMapHtmlFile"))

	@property
	def gpsMapBaseSize(self):
		"""
		This method is the property for the _gpsMapBaseSize attribute.

		@return: self.__gpsMapBaseSize. ( QSize() )
		"""

		return self.__gpsMapBaseSize

	@gpsMapBaseSize.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def gpsMapBaseSize(self, value):
		"""
		This method is the setter method for the _gpsMapBaseSize attribute.

		@param value: Attribute value. ( QSize() )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("gpsMapBaseSize"))

	@gpsMapBaseSize.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def gpsMapBaseSize(self):
		"""
		This method is the deleter method for the _gpsMapBaseSize attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("gpsMapBaseSize"))

	@property
	def dockArea(self):
		"""
		This method is the property for the _dockArea attribute.

		@return: self.__dockArea. ( Integer )
		"""

		return self.__dockArea

	@dockArea.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def dockArea(self, value):
		"""
		This method is the setter method for the _dockArea attribute.

		@param value: Attribute value. ( Integer )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("dockArea"))

	@dockArea.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def dockArea(self):
		"""
		This method is the deleter method for the _dockArea attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("dockArea"))

	@property
	def container(self):
		"""
		This method is the property for the _container attribute.

		@return: self.__container. ( QObject )
		"""

		return self.__container

	@container.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def container(self, value):
		"""
		This method is the setter method for the _container attribute.

		@param value: Attribute value. ( QObject )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("container"))

	@container.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def container(self):
		"""
		This method is the deleter method for the _container attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("container"))

	@property
	def coreDatabaseBrowser(self):
		"""
		This method is the property for the _coreDatabaseBrowser attribute.

		@return: self.__coreDatabaseBrowser. ( Object )
		"""

		return self.__coreDatabaseBrowser

	@coreDatabaseBrowser.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def coreDatabaseBrowser(self, value):
		"""
		This method is the setter method for the _coreDatabaseBrowser attribute.

		@param value: Attribute value. ( Object )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("coreDatabaseBrowser"))

	@coreDatabaseBrowser.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def coreDatabaseBrowser(self):
		"""
		This method is the deleter method for the _coreDatabaseBrowser attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("coreDatabaseBrowser"))

	@property
	def map(self):
		"""
		This method is the property for the _map attribute.

		@return: self.__map. ( QObject )
		"""

		return self.__map

	@map.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def map(self, value):
		"""
		This method is the setter method for the _map attribute.

		@param value: Attribute value. ( QObject )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("map"))

	@map.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def map(self):
		"""
		This method is the deleter method for the _map attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("map"))

	@property
	def mapTypeIds(self):
		"""
		This method is the property for the _mapTypeIds attribute.

		@return: self.__mapTypeIds. ( Tuple )
		"""

		return self.__mapTypeIds

	@mapTypeIds.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def mapTypeIds(self, value):
		"""
		This method is the setter method for the _mapTypeIds attribute.

		@param value: Attribute value. ( Tuple )
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is read only!".format("mapTypeIds"))

	@mapTypeIds.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def mapTypeIds(self):
		"""
		This method is the deleter method for the _mapTypeIds attribute.
		"""

		raise foundations.exceptions.ProgrammingError("'{0}' attribute is not deletable!".format("mapTypeIds"))

	#***********************************************************************************************
	#***	Class methods.
	#***********************************************************************************************
	@core.executionTrace
	def activate(self, container):
		"""
		This method activates the Component.

		@param container: Container to attach the Component to. ( QObject )
		"""

		LOGGER.debug("> Activating '{0}' Component.".format(self.__class__.__name__))

		self.uiFile = os.path.join(os.path.dirname(core.getModule(self).__file__), self.__uiPath)
		self.__uiResources = os.path.join(os.path.dirname(core.getModule(self).__file__), self.__uiResources)

		self.__container = container

		self.__coreDatabaseBrowser = self.__container.componentsManager.components["core.databaseBrowser"].interface

		self._activate()

	@core.executionTrace
	def deactivate(self):
		"""
		This method deactivates the Component.
		"""

		LOGGER.debug("> Deactivating '{0}' Component.".format(self.__class__.__name__))

		self.uiFile = None
		self.__uiResources = os.path.basename(self.__uiResources)

		self.__container = None

		self.__coreDatabaseBrowser = None

		self._deactivate()

	@core.executionTrace
	def initializeUi(self):
		"""
		This method initializes the Component ui.
		"""

		LOGGER.debug("> Initializing '{0}' Component ui.".format(self.__class__.__name__))

		self.ui.Zoom_In_pushButton.setIcon(QIcon(os.path.join(self.__uiResources, self.__uiZoomInImage)))
		self.ui.Zoom_Out_pushButton.setIcon(QIcon(os.path.join(self.__uiResources, self.__uiZoomOutImage)))

		self.ui.Map_Type_comboBox.addItems([mapType[0] for mapType in self.__mapTypeIds])

		self.__map = Map()
		self.__map.setMinimumSize(self.__gpsMapBaseSize)
		self.__map.load(QUrl.fromLocalFile(os.path.normpath(os.path.join(self.__uiResources, self.__gpsMapHtmlFile))))
		self.__map.page().mainFrame().setScrollBarPolicy(Qt.Horizontal, Qt.ScrollBarAlwaysOff)
		self.__map.page().mainFrame().setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff)
		self.ui.Map_scrollAreaWidgetContents_gridLayout.addWidget(self.__map)

		# Signals / slots.
		self.__coreDatabaseBrowser.ui.Database_Browser_listView.selectionModel().selectionChanged.connect(self.__coreDatabaseBrowser_Database_Browser_listView_selectionModel__selectionChanged)
		self.__map.loadFinished.connect(self.__map__loadFinished)
		self.ui.Map_Type_comboBox.activated.connect(self.__Map_Type_comboBox__activated)
		self.ui.Zoom_In_pushButton.clicked.connect(self.__Zoom_In_pushButton__clicked)
		self.ui.Zoom_Out_pushButton.clicked.connect(self.__Zoom_Out_pushButton__clicked)

	@core.executionTrace
	def uninitializeUi(self):
		"""
		This method uninitializes the Component ui.
		"""

		# Signals / slots.
		self.__coreDatabaseBrowser.ui.Database_Browser_listView.selectionModel().selectionChanged.disconnect(self.__coreDatabaseBrowser_Database_Browser_listView_selectionModel__selectionChanged)
		self.__map.loadFinished.disconnect(self.__map__loadFinished)
		self.ui.Map_Type_comboBox.activated.disconnect(self.__Map_Type_comboBox__activated)
		self.ui.Zoom_In_pushButton.clicked.disconnect(self.__Zoom_In_pushButton__clicked)
		self.ui.Zoom_Out_pushButton.clicked.disconnect(self.__Zoom_Out_pushButton__clicked)

		self.__map = None

	@core.executionTrace
	def addWidget(self):
		"""
		This method adds the Component Widget to the container.
		"""

		LOGGER.debug("> Adding '{0}' Component Widget.".format(self.__class__.__name__))

		self.__container.addDockWidget(Qt.DockWidgetArea(self.__dockArea), self.ui)

	@core.executionTrace
	def removeWidget(self):
		"""
		This method removes the Component Widget from the container.
		"""

		LOGGER.debug("> Removing '{0}' Component Widget.".format(self.__class__.__name__))

		self.__container.removeDockWidget(self.ui)
		self.ui.setParent(None)

	@core.executionTrace
	def __coreDatabaseBrowser_Database_Browser_listView_selectionModel__selectionChanged(self, selectedItems, deselectedItems):
		"""
		This method sets is triggered when coreDatabaseBrowser_Database_Browser_listView selection has changed.

		@param selectedItems: Selected items. ( QItemSelection )
		@param deselectedItems: Deselected items. ( QItemSelection )
		"""

		self.setMarkers__()

	@core.executionTrace
	def __Map_Type_comboBox__activated(self, index):
		"""
		This method is triggered when Map_Type_comboBox index changes.

		@param index: ComboBox activated item index. ( Integer )
		"""

		self.__map.setMapType(self.__mapTypeIds[index][1])

	@core.executionTrace
	def __Zoom_In_pushButton__clicked(self, checked):
		"""
		This method is triggered when Zoom_In_pushButton is clicked.

		@param checked: Checked state. ( Boolean )
		"""

		self.__map.setZoom("In")

	@core.executionTrace
	def __Zoom_Out_pushButton__clicked(self, checked):
		"""
		This method is triggered when Zoom_Out_pushButton is clicked.

		@param checked: Checked state. ( Boolean )
		"""

		self.__map.setZoom("Out")

	@core.executionTrace
	def __map__loadFinished(self, state):
		"""
		This method is triggered when the GPS map finishes loading.

		@param state: Loading state. ( Boolean )
		"""

		self.setMarkers__()

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(umbra.ui.common.uiBasicExceptionHandler, False, Exception)
	def setMarkers__(self):
		"""
		This method Sets selected Ibl Sets markers.

		@return: Method success. ( Boolean )
		"""

		selectedIblSets = self.__coreDatabaseBrowser.getSelectedIblSets()
		self.__map.removeMarkers()
		success = True
		for iblSet in selectedIblSets:
			success *= self.setMarker(iblSet) or False
		self.__map.setCenter()

		if success:
			return True
		else:
			raise Exception, "{0} | Exception raised while setting '{1}' GPS markers!".format(self.__class__.__name__, ", ". join((iblSet.title for iblSet in selectedIblSets)))

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def setMarker(self, iblSet):
		"""
		This method Sets Ibl Sets markers.

		@param iblSet: Ibl Set to display marker. ( DbIblSet )
		@return: Method success. ( Boolean )
		"""

		if not iblSet.latitude and not iblSet.longitude:
			return True

		LOGGER.debug("> Ibl Set '{0}' provides GEO coordinates.".format(iblSet.name))
		shotDateString = "<b>Shot Date: </b>{0}".format(self.__coreDatabaseBrowser.getFormatedShotDate(iblSet.date, iblSet.time) or Constants.nullObject)
		content = "<p><h3><b>{0}</b></h3></p><p><b>Author: </b>{1}<br><b>Location: </b>{2}<br>{3}<br><b>Comment: </b>{4}</p>".format(iblSet.title, iblSet.author, iblSet.location, shotDateString, iblSet.comment)
		return self.__map.addMarker((iblSet.latitude, iblSet.longitude), iblSet.title, strings.toForwardSlashes(iblSet.icon), content)

#***********************************************************************************************
#***	Python end.
#***********************************************************************************************
