#/usr/bin/bash

echo ----------------------------------------------------------------
echo sIBL_GUI - Mac Os X - Build
echo ----------------------------------------------------------------

alias python=/Library/Frameworks/Python.framework/Versions/2.6/bin/python
#! sIBL_GUI Build.
rm -rf build dist
python ../../utilities/sIBL_GUI_darwinSetup.py py2app --includes "foundations.strings,foundations.pkzip,ui.widgets.variable_QPushButton,sip,PyQt4.QtNetwork,PyQt4.QtWebKit,sqlalchemy,sqlalchemy.orm,sqlalchemy.ext,sqlalchemy.ext.declarative,sqlalchemy.databases" --no-strip
rm -rf `find ./dist/sIBL_GUI.app/ -name *debug*`
mkdir ./dist/sIBL_GUI.app/Contents/Resources/ui
cp  ../../src/ui/sIBL_GUI.ui ./dist/sIBL_GUI.app/Contents/Resources/ui
cp  ../../src/ui/sIBL_GUI_Layouts.rc ./dist/sIBL_GUI.app/Contents/Resources/ui
cp  ../../src/ui/Windows_styleSheet.qss ./dist/sIBL_GUI.app/Contents/Resources/ui
cp  ../../src/ui/Darwin_styleSheet.qss ./dist/sIBL_GUI.app/Contents/Resources/ui
cp  ../../src/ui/Linux_styleSheet.qss ./dist/sIBL_GUI.app/Contents/Resources/ui
mkdir ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Icon_Light_512.icns ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/sIBL_GUI_SpashScreen.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/sIBL_GUI_Logo.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Central_Widget.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Central_Widget_Hover.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Central_Widget_Active.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Layout.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Layout_Hover.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Layout_Active.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Miscellaneous.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Miscellaneous_Hover.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Miscellaneous_Active.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Library.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Library_Hover.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Library_Active.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Export.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Export_Hover.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Export_Active.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Preferences.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Preferences_Hover.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Preferences_Active.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp  ../../src/resources/Toolbar.png ./dist/sIBL_GUI.app/Contents/Resources/resources
cp -rf ../../src/templates ./dist/sIBL_GUI.app/Contents/Resources/
cp -rf ../../src/components ./dist/sIBL_GUI.app/Contents/Resources/
cp -f ./support/__boot__.py ./dist/sIBL_GUI.app/Contents/Resources/
cp -f ./support/qt.conf ./dist/sIBL_GUI.app/Contents/Resources/
cp -rf ./support/imageformats ./dist/sIBL_GUI.app/Contents/MacOs
rm -rf ./dist/sIBL_GUI.app/Contents/Resources/Templates/3dsMax
rm -rf ./dist/sIBL_GUI.app/Contents/Resources/Templates/XSI

#! sIBL_GUI Cleanup.
python ../../utilities/sIBL_GUI_recursiveRemove.py ./dist/sIBL_GUI.app/ .pyc
python ../../utilities/sIBL_GUI_recursiveRemove.py ./dist/sIBL_GUI.app/ .pyo
python ../../utilities/sIBL_GUI_recursiveRemove.py ./dist/sIBL_GUI.app/ .DS_Store
python ../../utilities/sIBL_GUI_recursiveRemove.py ./dist/sIBL_GUI.app/ Thumbs.db

#! sIBL_GUI DMG.
rm -f ./sIBL_GUI.dmg
hdiutil create ./sIBL_GUI.dmg -volname "sIBL_GUI" -fs HFS+ -srcfolder "./dist/sIBL_GUI.app"