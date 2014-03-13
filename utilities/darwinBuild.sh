#!/usr/bin/env bash
echo -------------------------------------------------------------------------------
echo sIBL_GUI - Mac Os X - Overall Build
echo -------------------------------------------------------------------------------

export PYINSTALLER=/Users/kelsolaar/Setup/pyinstaller-2.0/

export PROJECT=$( dirname "${BASH_SOURCE[0]}" )/..
export MAJOR_VERSION=4

export UTILITIES=$PROJECT/utilities

export SOURCE=$PROJECT/
export RELEASES=$PROJECT/releases/Darwin
export DISTRIBUTION=$RELEASES/dist
export BUILD=$RELEASES/build
export BUNDLE=$DISTRIBUTION/sIBL_GUI\ $MAJOR_VERSION.app
export DEPENDENCIES=$BUNDLE/Contents/MacOS
export RESOURCES=$BUNDLE/Contents/Resources

IFS=","

#! sIBL_GUI cleanup.
echo -------------------------------------------------------------------------------
echo Cleanup - Begin
echo -------------------------------------------------------------------------------
rm -rf $BUILD $DISTRIBUTION $DEPENDENCIES $BUNDLE
packages="foundations,manager,umbra,sibl_gui"
for package in $packages
do
	for type in ".pyc,.pyo,.DS_Store,Thumbs.db"
	do
		python $UTILITIES/recursiveRemove.py $( $UTILITIES/getPackagePath.py $package ) $type
	done
done
echo -------------------------------------------------------------------------------
echo Cleanup - End
echo -------------------------------------------------------------------------------

#! Darwin build.
echo -------------------------------------------------------------------------------
echo Build - Begin
echo -------------------------------------------------------------------------------
mv sibl_gui/launcher.py sibl_gui/sIBL_GUI\ $MAJOR_VERSION.py 
python $PYINSTALLER/pyinstaller.py --noconfirm --noconsole -o releases/Darwin --hidden-import=ConfigParser --hidden-import=PyQt4 --hidden-import=PyQt4.QtCore --hidden-import=PyQt4.QtGui --hidden-import=PyQt4.QtNetwork --hidden-import=PyQt4.QtWebKit --hidden-import=PyQt4.uic --hidden-import=PyQt4.uic.Compiler --hidden-import=PyQt4.uic.Compiler.PyQt4 --hidden-import=PyQt4.uic.Compiler.compiler --hidden-import=PyQt4.uic.Compiler.indenter --hidden-import=PyQt4.uic.Compiler.logging --hidden-import=PyQt4.uic.Compiler.misc --hidden-import=PyQt4.uic.Compiler.proxy_metaclass --hidden-import=PyQt4.uic.Compiler.qobjectcreator --hidden-import=PyQt4.uic.Compiler.qtproxies --hidden-import=PyQt4.uic.Compiler.re --hidden-import=PyQt4.uic.Compiler.sys --hidden-import=PyQt4.uic.PyQt4 --hidden-import=PyQt4.uic.exceptions --hidden-import=PyQt4.uic.icon_cache --hidden-import=PyQt4.uic.logging --hidden-import=PyQt4.uic.objcreator --hidden-import=PyQt4.uic.os --hidden-import=PyQt4.uic.port_v2 --hidden-import=PyQt4.uic.port_v2.PyQt4 --hidden-import=PyQt4.uic.port_v2.as_string --hidden-import=PyQt4.uic.port_v2.ascii_upper --hidden-import=PyQt4.uic.port_v2.cStringIO --hidden-import=PyQt4.uic.port_v2.load_plugin --hidden-import=PyQt4.uic.port_v2.proxy_base --hidden-import=PyQt4.uic.port_v2.re --hidden-import=PyQt4.uic.port_v2.string --hidden-import=PyQt4.uic.port_v2.string_io --hidden-import=PyQt4.uic.properties --hidden-import=PyQt4.uic.re --hidden-import=PyQt4.uic.sys --hidden-import=PyQt4.uic.uiparser --hidden-import=PyQt4.uic.xml --hidden-import=Queue --hidden-import=SocketServer --hidden-import=StringIO --hidden-import=UserDict --hidden-import=__builtin__ --hidden-import=__future__ --hidden-import=__main__ --hidden-import=_abcoll --hidden-import=_ast --hidden-import=_bisect --hidden-import=_codecs --hidden-import=_collections --hidden-import=_ctypes --hidden-import=_functools --hidden-import=_hashlib --hidden-import=_heapq --hidden-import=_io --hidden-import=_locale --hidden-import=_random --hidden-import=_scproxy --hidden-import=_socket --hidden-import=_sqlite3 --hidden-import=_sre --hidden-import=_ssl --hidden-import=_struct --hidden-import=_virtualenv_distutils --hidden-import=_warnings --hidden-import=_weakref --hidden-import=_weakrefset --hidden-import=abc --hidden-import=array --hidden-import=ast --hidden-import=atexit --hidden-import=base64 --hidden-import=binascii --hidden-import=bisect --hidden-import=cPickle --hidden-import=cStringIO --hidden-import=cgi --hidden-import=code --hidden-import=codecs --hidden-import=codeop --hidden-import=collections --hidden-import=contextlib --hidden-import=copy --hidden-import=copy_reg --hidden-import=ctypes --hidden-import=ctypes._ctypes --hidden-import=ctypes._endian --hidden-import=ctypes.ctypes --hidden-import=ctypes.macholib --hidden-import=ctypes.macholib.dyld --hidden-import=ctypes.macholib.dylib --hidden-import=ctypes.macholib.framework --hidden-import=ctypes.macholib.itertools --hidden-import=ctypes.macholib.os --hidden-import=ctypes.macholib.re --hidden-import=ctypes.os --hidden-import=ctypes.struct --hidden-import=ctypes.sys --hidden-import=ctypes.util --hidden-import=datetime --hidden-import=decimal --hidden-import=decorator --hidden-import=dis --hidden-import=distutils --hidden-import=distutils.debug --hidden-import=distutils.dep_util --hidden-import=distutils.dist --hidden-import=distutils.distutils --hidden-import=distutils.email --hidden-import=distutils.errors --hidden-import=distutils.fancy_getopt --hidden-import=distutils.getopt --hidden-import=distutils.imp --hidden-import=distutils.log --hidden-import=distutils.opcode --hidden-import=distutils.os --hidden-import=distutils.re --hidden-import=distutils.spawn --hidden-import=distutils.stat --hidden-import=distutils.string --hidden-import=distutils.sys --hidden-import=distutils.sysconfig --hidden-import=distutils.text_file --hidden-import=distutils.util --hidden-import=distutils.warnings --hidden-import=email --hidden-import=email.Charset --hidden-import=email.Encoders --hidden-import=email.Errors --hidden-import=email.FeedParser --hidden-import=email.Generator --hidden-import=email.Header --hidden-import=email.Iterators --hidden-import=email.MIMEAudio --hidden-import=email.MIMEBase --hidden-import=email.MIMEImage --hidden-import=email.MIMEMessage --hidden-import=email.MIMEMultipart --hidden-import=email.MIMENonMultipart --hidden-import=email.MIMEText --hidden-import=email.Message --hidden-import=email.Parser --hidden-import=email.Utils --hidden-import=email._parseaddr --hidden-import=email.base64 --hidden-import=email.base64MIME --hidden-import=email.base64mime --hidden-import=email.binascii --hidden-import=email.cStringIO --hidden-import=email.charset --hidden-import=email.codecs --hidden-import=email.email --hidden-import=email.encoders --hidden-import=email.errors --hidden-import=email.feedparser --hidden-import=email.generator --hidden-import=email.header --hidden-import=email.iterators --hidden-import=email.message --hidden-import=email.mime --hidden-import=email.mime.audio --hidden-import=email.mime.base --hidden-import=email.mime.cStringIO --hidden-import=email.mime.email --hidden-import=email.mime.image --hidden-import=email.mime.imghdr --hidden-import=email.mime.message --hidden-import=email.mime.multipart --hidden-import=email.mime.nonmultipart --hidden-import=email.mime.sndhdr --hidden-import=email.mime.text --hidden-import=email.os --hidden-import=email.parser --hidden-import=email.quopri --hidden-import=email.quopriMIME --hidden-import=email.quoprimime --hidden-import=email.random --hidden-import=email.re --hidden-import=email.socket --hidden-import=email.string --hidden-import=email.sys --hidden-import=email.time --hidden-import=email.urllib --hidden-import=email.utils --hidden-import=email.uu --hidden-import=email.warnings --hidden-import=encodings --hidden-import=encodings.__builtin__ --hidden-import=encodings.aliases --hidden-import=encodings.ascii --hidden-import=encodings.codecs --hidden-import=encodings.encodings --hidden-import=encodings.utf_8 --hidden-import=errno --hidden-import=exceptions --hidden-import=fcntl --hidden-import=fnmatch --hidden-import=functools --hidden-import=gc --hidden-import=genericpath --hidden-import=getopt --hidden-import=getpass --hidden-import=gettext --hidden-import=grp --hidden-import=hashlib --hidden-import=heapq --hidden-import=httplib --hidden-import=imghdr --hidden-import=imp --hidden-import=inspect --hidden-import=io --hidden-import=itertools --hidden-import=keyword --hidden-import=linecache --hidden-import=locale --hidden-import=logging --hidden-import=logging.atexit --hidden-import=logging.cStringIO --hidden-import=logging.codecs --hidden-import=logging.os --hidden-import=logging.sys --hidden-import=logging.thread --hidden-import=logging.threading --hidden-import=logging.time --hidden-import=logging.traceback --hidden-import=logging.warnings --hidden-import=logging.weakref --hidden-import=logilab --hidden-import=marshal --hidden-import=math --hidden-import=migrate --hidden-import=migrate.changeset --hidden-import=migrate.changeset.StringIO --hidden-import=migrate.changeset.UserDict --hidden-import=migrate.changeset.ansisql --hidden-import=migrate.changeset.constraint --hidden-import=migrate.changeset.databases --hidden-import=migrate.changeset.databases.UserDict --hidden-import=migrate.changeset.databases.copy --hidden-import=migrate.changeset.databases.firebird --hidden-import=migrate.changeset.databases.migrate --hidden-import=migrate.changeset.databases.mysql --hidden-import=migrate.changeset.databases.oracle --hidden-import=migrate.changeset.databases.postgres --hidden-import=migrate.changeset.databases.sqlalchemy --hidden-import=migrate.changeset.databases.sqlite --hidden-import=migrate.changeset.databases.visitor --hidden-import=migrate.changeset.migrate --hidden-import=migrate.changeset.re --hidden-import=migrate.changeset.schema --hidden-import=migrate.changeset.sqlalchemy --hidden-import=migrate.changeset.warnings --hidden-import=migrate.exceptions --hidden-import=migrate.migrate --hidden-import=migrate.versioning --hidden-import=migrate.versioning.ConfigParser --hidden-import=migrate.versioning.api --hidden-import=migrate.versioning.cfgparse --hidden-import=migrate.versioning.config --hidden-import=migrate.versioning.datetime --hidden-import=migrate.versioning.genmodel --hidden-import=migrate.versioning.inspect --hidden-import=migrate.versioning.logging --hidden-import=migrate.versioning.migrate --hidden-import=migrate.versioning.os --hidden-import=migrate.versioning.pathed --hidden-import=migrate.versioning.pkg_resources --hidden-import=migrate.versioning.re --hidden-import=migrate.versioning.repository --hidden-import=migrate.versioning.schema --hidden-import=migrate.versioning.schemadiff --hidden-import=migrate.versioning.script --hidden-import=migrate.versioning.script.StringIO --hidden-import=migrate.versioning.script.base --hidden-import=migrate.versioning.script.inspect --hidden-import=migrate.versioning.script.logging --hidden-import=migrate.versioning.script.migrate --hidden-import=migrate.versioning.script.py --hidden-import=migrate.versioning.script.shutil --hidden-import=migrate.versioning.script.sql --hidden-import=migrate.versioning.script.warnings --hidden-import=migrate.versioning.shutil --hidden-import=migrate.versioning.sqlalchemy --hidden-import=migrate.versioning.string --hidden-import=migrate.versioning.sys --hidden-import=migrate.versioning.tempita --hidden-import=migrate.versioning.template --hidden-import=migrate.versioning.util --hidden-import=migrate.versioning.util.decorator --hidden-import=migrate.versioning.util.importpath --hidden-import=migrate.versioning.util.keyedinstance --hidden-import=migrate.versioning.util.logging --hidden-import=migrate.versioning.util.migrate --hidden-import=migrate.versioning.util.os --hidden-import=migrate.versioning.util.pkg_resources --hidden-import=migrate.versioning.util.sqlalchemy --hidden-import=migrate.versioning.util.sys --hidden-import=migrate.versioning.util.warnings --hidden-import=migrate.versioning.version --hidden-import=mimetools --hidden-import=new --hidden-import=numbers --hidden-import=opcode --hidden-import=operator --hidden-import=optparse --hidden-import=os --hidden-import=os.path --hidden-import=pickle --hidden-import=pkg_resources --hidden-import=pkgutil --hidden-import=platform --hidden-import=plistlib --hidden-import=posix --hidden-import=posixpath --hidden-import=pwd --hidden-import=pyexpat --hidden-import=pyexpat.errors --hidden-import=pyexpat.model --hidden-import=quopri --hidden-import=random --hidden-import=re --hidden-import=rfc822 --hidden-import=select --hidden-import=sets --hidden-import=shutil --hidden-import=signal --hidden-import=sip --hidden-import=site --hidden-import=sitecustomize --hidden-import=sndhdr --hidden-import=socket --hidden-import=sqlalchemy --hidden-import=sqlalchemy.codecs --hidden-import=sqlalchemy.collections --hidden-import=sqlalchemy.connectors --hidden-import=sqlalchemy.connectors.mxodbc --hidden-import=sqlalchemy.connectors.mysqldb --hidden-import=sqlalchemy.connectors.pyodbc --hidden-import=sqlalchemy.connectors.re --hidden-import=sqlalchemy.connectors.sqlalchemy --hidden-import=sqlalchemy.connectors.sys --hidden-import=sqlalchemy.connectors.urllib --hidden-import=sqlalchemy.connectors.warnings --hidden-import=sqlalchemy.connectors.zxJDBC --hidden-import=sqlalchemy.cprocessors --hidden-import=sqlalchemy.cresultproxy --hidden-import=sqlalchemy.databases --hidden-import=sqlalchemy.databases.sqlalchemy --hidden-import=sqlalchemy.datetime --hidden-import=sqlalchemy.dialects --hidden-import=sqlalchemy.dialects.access --hidden-import=sqlalchemy.dialects.access.base --hidden-import=sqlalchemy.dialects.access.sqlalchemy --hidden-import=sqlalchemy.dialects.drizzle --hidden-import=sqlalchemy.dialects.drizzle.base --hidden-import=sqlalchemy.dialects.drizzle.mysqldb --hidden-import=sqlalchemy.dialects.drizzle.sqlalchemy --hidden-import=sqlalchemy.dialects.firebird --hidden-import=sqlalchemy.dialects.firebird.base --hidden-import=sqlalchemy.dialects.firebird.datetime --hidden-import=sqlalchemy.dialects.firebird.kinterbasdb --hidden-import=sqlalchemy.dialects.firebird.re --hidden-import=sqlalchemy.dialects.firebird.sqlalchemy --hidden-import=sqlalchemy.dialects.informix --hidden-import=sqlalchemy.dialects.informix.base --hidden-import=sqlalchemy.dialects.informix.datetime --hidden-import=sqlalchemy.dialects.informix.informixdb --hidden-import=sqlalchemy.dialects.informix.re --hidden-import=sqlalchemy.dialects.informix.sqlalchemy --hidden-import=sqlalchemy.dialects.maxdb --hidden-import=sqlalchemy.dialects.maxdb.base --hidden-import=sqlalchemy.dialects.maxdb.datetime --hidden-import=sqlalchemy.dialects.maxdb.itertools --hidden-import=sqlalchemy.dialects.maxdb.re --hidden-import=sqlalchemy.dialects.maxdb.sapdb --hidden-import=sqlalchemy.dialects.maxdb.sqlalchemy --hidden-import=sqlalchemy.dialects.mssql --hidden-import=sqlalchemy.dialects.mssql.adodbapi --hidden-import=sqlalchemy.dialects.mssql.base --hidden-import=sqlalchemy.dialects.mssql.datetime --hidden-import=sqlalchemy.dialects.mssql.decimal --hidden-import=sqlalchemy.dialects.mssql.information_schema --hidden-import=sqlalchemy.dialects.mssql.mxodbc --hidden-import=sqlalchemy.dialects.mssql.operator --hidden-import=sqlalchemy.dialects.mssql.pymssql --hidden-import=sqlalchemy.dialects.mssql.pyodbc --hidden-import=sqlalchemy.dialects.mssql.re --hidden-import=sqlalchemy.dialects.mssql.sqlalchemy --hidden-import=sqlalchemy.dialects.mssql.sys --hidden-import=sqlalchemy.dialects.mssql.zxjdbc --hidden-import=sqlalchemy.dialects.mysql --hidden-import=sqlalchemy.dialects.mysql.array --hidden-import=sqlalchemy.dialects.mysql.base --hidden-import=sqlalchemy.dialects.mysql.datetime --hidden-import=sqlalchemy.dialects.mysql.inspect --hidden-import=sqlalchemy.dialects.mysql.mysqlconnector --hidden-import=sqlalchemy.dialects.mysql.mysqldb --hidden-import=sqlalchemy.dialects.mysql.oursql --hidden-import=sqlalchemy.dialects.mysql.pymysql --hidden-import=sqlalchemy.dialects.mysql.pyodbc --hidden-import=sqlalchemy.dialects.mysql.re --hidden-import=sqlalchemy.dialects.mysql.sqlalchemy --hidden-import=sqlalchemy.dialects.mysql.sys --hidden-import=sqlalchemy.dialects.mysql.zxjdbc --hidden-import=sqlalchemy.dialects.oracle --hidden-import=sqlalchemy.dialects.oracle.base --hidden-import=sqlalchemy.dialects.oracle.collections --hidden-import=sqlalchemy.dialects.oracle.cx_oracle --hidden-import=sqlalchemy.dialects.oracle.datetime --hidden-import=sqlalchemy.dialects.oracle.decimal --hidden-import=sqlalchemy.dialects.oracle.random --hidden-import=sqlalchemy.dialects.oracle.re --hidden-import=sqlalchemy.dialects.oracle.sqlalchemy --hidden-import=sqlalchemy.dialects.oracle.zxjdbc --hidden-import=sqlalchemy.dialects.postgresql --hidden-import=sqlalchemy.dialects.postgresql.base --hidden-import=sqlalchemy.dialects.postgresql.logging --hidden-import=sqlalchemy.dialects.postgresql.pg8000 --hidden-import=sqlalchemy.dialects.postgresql.psycopg2 --hidden-import=sqlalchemy.dialects.postgresql.pypostgresql --hidden-import=sqlalchemy.dialects.postgresql.re --hidden-import=sqlalchemy.dialects.postgresql.sqlalchemy --hidden-import=sqlalchemy.dialects.postgresql.uuid --hidden-import=sqlalchemy.dialects.postgresql.zxjdbc --hidden-import=sqlalchemy.dialects.sqlite --hidden-import=sqlalchemy.dialects.sqlite.base --hidden-import=sqlalchemy.dialects.sqlite.datetime --hidden-import=sqlalchemy.dialects.sqlite.os --hidden-import=sqlalchemy.dialects.sqlite.pysqlite --hidden-import=sqlalchemy.dialects.sqlite.re --hidden-import=sqlalchemy.dialects.sqlite.sqlalchemy --hidden-import=sqlalchemy.dialects.sqlite.sqlite3 --hidden-import=sqlalchemy.dialects.sybase --hidden-import=sqlalchemy.dialects.sybase.base --hidden-import=sqlalchemy.dialects.sybase.operator --hidden-import=sqlalchemy.dialects.sybase.pyodbc --hidden-import=sqlalchemy.dialects.sybase.pysybase --hidden-import=sqlalchemy.dialects.sybase.sqlalchemy --hidden-import=sqlalchemy.engine --hidden-import=sqlalchemy.engine.StringIO --hidden-import=sqlalchemy.engine.base --hidden-import=sqlalchemy.engine.codecs --hidden-import=sqlalchemy.engine.collections --hidden-import=sqlalchemy.engine.ddl --hidden-import=sqlalchemy.engine.default --hidden-import=sqlalchemy.engine.inspect --hidden-import=sqlalchemy.engine.itertools --hidden-import=sqlalchemy.engine.operator --hidden-import=sqlalchemy.engine.random --hidden-import=sqlalchemy.engine.re --hidden-import=sqlalchemy.engine.reflection --hidden-import=sqlalchemy.engine.sqlalchemy --hidden-import=sqlalchemy.engine.strategies --hidden-import=sqlalchemy.engine.sys --hidden-import=sqlalchemy.engine.threadlocal --hidden-import=sqlalchemy.engine.url --hidden-import=sqlalchemy.engine.urllib --hidden-import=sqlalchemy.engine.weakref --hidden-import=sqlalchemy.event --hidden-import=sqlalchemy.events --hidden-import=sqlalchemy.exc --hidden-import=sqlalchemy.ext --hidden-import=sqlalchemy.ext.declarative --hidden-import=sqlalchemy.ext.sqlalchemy --hidden-import=sqlalchemy.inspect --hidden-import=sqlalchemy.interfaces --hidden-import=sqlalchemy.log --hidden-import=sqlalchemy.logging --hidden-import=sqlalchemy.orm --hidden-import=sqlalchemy.orm.attributes --hidden-import=sqlalchemy.orm.collections --hidden-import=sqlalchemy.orm.copy --hidden-import=sqlalchemy.orm.dependency --hidden-import=sqlalchemy.orm.deprecated_interfaces --hidden-import=sqlalchemy.orm.descriptor_props --hidden-import=sqlalchemy.orm.evaluator --hidden-import=sqlalchemy.orm.events --hidden-import=sqlalchemy.orm.exc --hidden-import=sqlalchemy.orm.identity --hidden-import=sqlalchemy.orm.inspect --hidden-import=sqlalchemy.orm.instrumentation --hidden-import=sqlalchemy.orm.interfaces --hidden-import=sqlalchemy.orm.itertools --hidden-import=sqlalchemy.orm.mapper --hidden-import=sqlalchemy.orm.operator --hidden-import=sqlalchemy.orm.persistence --hidden-import=sqlalchemy.orm.properties --hidden-import=sqlalchemy.orm.query --hidden-import=sqlalchemy.orm.re --hidden-import=sqlalchemy.orm.scoping --hidden-import=sqlalchemy.orm.session --hidden-import=sqlalchemy.orm.sets --hidden-import=sqlalchemy.orm.sqlalchemy --hidden-import=sqlalchemy.orm.state --hidden-import=sqlalchemy.orm.strategies --hidden-import=sqlalchemy.orm.sync --hidden-import=sqlalchemy.orm.sys --hidden-import=sqlalchemy.orm.types --hidden-import=sqlalchemy.orm.unitofwork --hidden-import=sqlalchemy.orm.util --hidden-import=sqlalchemy.orm.weakref --hidden-import=sqlalchemy.pool --hidden-import=sqlalchemy.processors --hidden-import=sqlalchemy.re --hidden-import=sqlalchemy.schema --hidden-import=sqlalchemy.sql --hidden-import=sqlalchemy.sql.collections --hidden-import=sqlalchemy.sql.compiler --hidden-import=sqlalchemy.sql.decimal --hidden-import=sqlalchemy.sql.expression --hidden-import=sqlalchemy.sql.functions --hidden-import=sqlalchemy.sql.itertools --hidden-import=sqlalchemy.sql.operator --hidden-import=sqlalchemy.sql.operators --hidden-import=sqlalchemy.sql.re --hidden-import=sqlalchemy.sql.sqlalchemy --hidden-import=sqlalchemy.sql.sys --hidden-import=sqlalchemy.sql.util --hidden-import=sqlalchemy.sql.visitors --hidden-import=sqlalchemy.sqlalchemy --hidden-import=sqlalchemy.sys --hidden-import=sqlalchemy.time --hidden-import=sqlalchemy.traceback --hidden-import=sqlalchemy.types --hidden-import=sqlalchemy.util --hidden-import=sqlalchemy.util._collections --hidden-import=sqlalchemy.util.cPickle --hidden-import=sqlalchemy.util.collections --hidden-import=sqlalchemy.util.compat --hidden-import=sqlalchemy.util.contextlib --hidden-import=sqlalchemy.util.decimal --hidden-import=sqlalchemy.util.deprecations --hidden-import=sqlalchemy.util.functools --hidden-import=sqlalchemy.util.hashlib --hidden-import=sqlalchemy.util.inspect --hidden-import=sqlalchemy.util.itertools --hidden-import=sqlalchemy.util.langhelpers --hidden-import=sqlalchemy.util.operator --hidden-import=sqlalchemy.util.queue --hidden-import=sqlalchemy.util.re --hidden-import=sqlalchemy.util.sets --hidden-import=sqlalchemy.util.sqlalchemy --hidden-import=sqlalchemy.util.sys --hidden-import=sqlalchemy.util.threading --hidden-import=sqlalchemy.util.time --hidden-import=sqlalchemy.util.topological --hidden-import=sqlalchemy.util.types --hidden-import=sqlalchemy.util.urlparse --hidden-import=sqlalchemy.util.warnings --hidden-import=sqlalchemy.util.weakref --hidden-import=sqlalchemy.weakref --hidden-import=sqlite3 --hidden-import=sqlite3._sqlite3 --hidden-import=sqlite3.datetime --hidden-import=sqlite3.dbapi2 --hidden-import=sqlite3.time --hidden-import=sre_compile --hidden-import=sre_constants --hidden-import=sre_parse --hidden-import=ssl --hidden-import=stat --hidden-import=string --hidden-import=strop --hidden-import=struct --hidden-import=sys --hidden-import=tempfile --hidden-import=tempita --hidden-import=tempita._looper --hidden-import=tempita.cStringIO --hidden-import=tempita.cgi --hidden-import=tempita.compat3 --hidden-import=tempita.os --hidden-import=tempita.re --hidden-import=tempita.sys --hidden-import=tempita.tempita --hidden-import=tempita.tokenize --hidden-import=tempita.urllib --hidden-import=termios --hidden-import=textwrap --hidden-import=thread --hidden-import=threading --hidden-import=time --hidden-import=token --hidden-import=tokenize --hidden-import=traceback --hidden-import=types --hidden-import=urllib --hidden-import=urllib2 --hidden-import=urlparse --hidden-import=uu --hidden-import=uuid --hidden-import=warnings --hidden-import=weakref --hidden-import=xml --hidden-import=xml.etree --hidden-import=xml.etree.ElementPath --hidden-import=xml.etree.ElementTree --hidden-import=xml.etree.re --hidden-import=xml.etree.sys --hidden-import=xml.etree.warnings --hidden-import=xml.etree.xml --hidden-import=xml.parsers --hidden-import=xml.parsers.expat --hidden-import=xml.parsers.pyexpat --hidden-import=zipfile --hidden-import=zipimport --hidden-import=zlib sibl_gui/sIBL_GUI\ $MAJOR_VERSION.py
mv sibl_gui/sIBL_GUI\ $MAJOR_VERSION.py sibl_gui/launcher.py 
echo -------------------------------------------------------------------------------
echo Build - End
echo -------------------------------------------------------------------------------

#! Darwin release.
echo -------------------------------------------------------------------------------
echo Release - Begin
echo -------------------------------------------------------------------------------
packages="foundations,manager,umbra,sibl_gui"
for package in $packages
do
	cp -r $( $UTILITIES/getPackagePath.py $package ) $DEPENDENCIES/
done
packages="umbra,sibl_gui"
extensions="bmp,icns,ico"
for package in $packages
do
	rm -rf $DEPENDENCIES/$package/resources/images/builders

	for extension in $extensions
	do
		rm -f $DEPENDENCIES/$package/resources/images/*.$extension
	done
done
cp $SOURCE/sibl_gui/resources/images/Icon_Light_256.icns $RESOURCES/icon-windowed.icns
python $UTILITIES/recursiveRemove.py $BUNDLE .pyc
rm -f $DEPENDENCIES/sibl_gui/libraries/freeImage/resources/*.dll
rm -f $DEPENDENCIES/sibl_gui/libraries/freeImage/resources/*.so
rm -rf $DEPENDENCIES/sibl_gui/resources/templates/3dsMax*
rm -rf $DEPENDENCIES/sibl_gui/resources/templates/Softimage*
rm -rf $DEPENDENCIES/sibl_gui/resources/templates/XSI*
rm -rf $DEPENDENCIES/*/tests
echo -------------------------------------------------------------------------------
echo Release - End
echo -------------------------------------------------------------------------------

echo -------------------------------------------------------------------------------
echo Templates ReStructuredText Files Cleanup - Begin
echo -------------------------------------------------------------------------------
python $UTILITIES/recursiveRemove.py $BUNDLE/ .rst
echo -------------------------------------------------------------------------------
echo Templates ReStructuredText Files Cleanup - End
echo -------------------------------------------------------------------------------

#! sIBL_GUI DMG.
echo -------------------------------------------------------------------------------
echo Dmg Compilation - Begin
echo -------------------------------------------------------------------------------
rm -f ./*.dmg
dropdmg -g sIBL_GUI -y sIBL_GUI $BUNDLE
mv $RELEASES/sIBL_GUI\ $MAJOR_VERSION.dmg $RELEASES/sIBL_GUI.dmg
echo -------------------------------------------------------------------------------
echo Dmg Compilation - End
echo -------------------------------------------------------------------------------
