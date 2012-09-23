#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**views.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines the :class:`sibl_gui.components.core.collectionsOutliner.collectionsOutliner.CollectionsOutliner`
	Component Interface class Views.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import pickle
import logging
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QAbstractItemView

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.core as core
import foundations.exceptions
import sibl_gui.ui.views
import umbra.ui.common
from umbra.globals.constants import Constants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2012 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "IblSetsCollections_QTreeView"]

LOGGER = logging.getLogger(Constants.logger)

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class IblSetsCollections_QTreeView(sibl_gui.ui.views.Abstract_QTreeView):
	"""
	This class is used to display Database Collections.
	"""

	@core.executionTrace
	def __init__(self, parent, model=None, readOnly=False):
		"""
		This method initializes the class.

		:param parent: Object parent. ( QObject )
		:param model: Model. ( QObject )
		:param readOnly: View is read only. ( Boolean )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		sibl_gui.ui.views.Abstract_QTreeView.__init__(self, parent, model, readOnly)

		# --- Setting class attributes. ---
		self.__container = parent

		self.__treeViewIndentation = 15

		IblSetsCollections_QTreeView.__initializeUi(self)

	#******************************************************************************************************************
	#***	Attributes properties.
	#******************************************************************************************************************
	@property
	def container(self):
		"""
		This method is the property for **self.__container** attribute.

		:return: self.__container. ( QObject )
		"""

		return self.__container

	@container.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def container(self, value):
		"""
		This method is the setter method for **self.__container** attribute.

		:param value: Attribute value. ( QObject )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "container"))

	@container.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def container(self):
		"""
		This method is the deleter method for **self.__container** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "container"))

	@property
	def treeViewIndentation(self):
		"""
		This method is the property for **self.__treeViewIndentation** attribute.

		:return: self.__treeViewIndentation. ( Integer )
		"""

		return self.__treeViewIndentation

	@treeViewIndentation.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def treeViewIndentation(self, value):
		"""
		This method is the setter method for **self.__treeViewIndentation** attribute.

		:param value: Attribute value. ( Integer )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "treeViewIndentation"))

	@treeViewIndentation.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def treeViewIndentation(self):
		"""
		This method is the deleter method for **self.__treeViewIndentation** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "treeViewIndentation"))

	#******************************************************************************************************************
	#***	Class methods.
	#******************************************************************************************************************
	@core.executionTrace
	def dragEnterEvent(self, event):
		"""
		This method reimplements the :meth:`sibl_gui.ui.views.Abstract_QTreeView.dragEnterEvent` method.

		:param event: QEvent. ( QEvent )
		"""

		if event.mimeData().hasFormat("application/x-umbragraphmodeldatalist"):
			LOGGER.debug("> '{0}' drag event type accepted!".format("application/x-umbragraphmodeldatalist"))
			event.accept()
		else:
			event.ignore()

	@core.executionTrace
	def dragMoveEvent(self, event):
		"""
		This method reimplements the :meth:`sibl_gui.ui.views.Abstract_QTreeView.dragMoveEvent` method.

		:param event: QEvent. ( QEvent )
		"""

		pass

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(umbra.ui.common.notifyExceptionHandler,
											False,
											foundations.exceptions.DirectoryExistsError,
											foundations.exceptions.UserError)
	def dropEvent(self, event):
		"""
		This method reimplements the :meth:`sibl_gui.ui.views.Abstract_QTreeView.dropEvent` method.

		:param event: QEvent. ( QEvent )
		"""

		if not self.readOnly:
			indexAt = self.indexAt(event.pos())
			collectionNode = self.model().getNode(indexAt)

			if not collectionNode:
				return

			if collectionNode.name in (self.__container.overallCollection, "InvisibleRootNode"):
				return

			LOGGER.debug("> Item at drop position: '{0}'.".format(collectionNode))

			nodes = pickle.loads(event.mimeData().data("application/x-umbragraphmodeldatalist"))
			for node in nodes:
				if node.family != "IblSet":
					continue

				node._AbstractDatabaseNode__dbItem = self.__container.db.dbSession.merge(node.dbItem)
				if collectionNode.dbItem.id != node.dbItem.collection:
					LOGGER.info("> Moving '{0}' Ibl Set to '{1}' Collection.".format(node.dbItem.title,
																					collectionNode.dbItem.name))
					node.dbItem.collection = collectionNode.dbItem.id
			if self.__container.db.commit():
				self.__container.modelRefresh.emit()
		else:
			raise foundations.exceptions.UserError("{0} | Cannot perform action, View has been set read only!".format(
			self.__class__.__name__))

	@core.executionTrace
	def __initializeUi(self):
		"""
		This method initializes the Widget ui.
		"""

		self.setAutoScroll(True)
		self.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.setIndentation(self.__treeViewIndentation)
		self.setDragDropMode(QAbstractItemView.DropOnly)

		self.setSortingEnabled(True)
		self.sortByColumn(0, Qt.AscendingOrder)

		self.__setDefaultUiState()

		# Signals / Slots.
		self.model().modelReset.connect(self.__setDefaultUiState)

	@core.executionTrace
	def __setDefaultUiState(self):
		"""
		This method sets the Widget default ui state.
		"""

		LOGGER.debug("> Setting default View state!")

		if not self.model():
			return

		self.expandAll()

		for column in range(len(self.model().horizontalHeaders)):
			self.resizeColumnToContents(column)

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def storeModelSelection(self):
		"""
		This method stores the Model selection.

		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Storing Model selection!")

		self.modelSelection = {"Overall" : [], "Collections" : []}
		for node in self.getSelectedNodes():
			if node.name == self.__container.overallCollection:
				self.modelSelection["Overall"].append(node.name)
			elif node.family == "Collection":
				self.modelSelection["Collections"].append(node.id.value)
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def restoreModelSelection(self):
		"""
		This method restores the Model selection.

		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Restoring Model selection!")

		if not self.modelSelection:
			return False

		selection = self.modelSelection.get("Overall", None) or self.modelSelection.get("Collections", None)
		if not selection:
			return False

		indexes = []
		for node in foundations.walkers.nodesWalker(self.model().rootNode):
			if node.family == "Collection":
				self.modelSelection.get("Collections", None) and \
				node.id.value in self.modelSelection["Collections"] and indexes.append(self.model().getNodeIndex(node))
			else:
				self.modelSelection.get("Overall", None) and \
				node.name in self.modelSelection["Overall"] and indexes.append(self.model().getNodeIndex(node))

		return self.selectIndexes(indexes)