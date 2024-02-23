# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(889, 600)
        self.save_toml = QAction(MainWindow)
        self.save_toml.setObjectName(u"save_toml")
        self.load_toml = QAction(MainWindow)
        self.load_toml.setObjectName(u"load_toml")
        self.save_runtime_toml = QAction(MainWindow)
        self.save_runtime_toml.setObjectName(u"save_runtime_toml")
        self.no_theme_action = QAction(MainWindow)
        self.no_theme_action.setObjectName(u"no_theme_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 0, 0)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 889, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuTheme = QMenu(self.menubar)
        self.menuTheme.setObjectName(u"menuTheme")
        self.dark_theme_menu = QMenu(self.menuTheme)
        self.dark_theme_menu.setObjectName(u"dark_theme_menu")
        self.light_theme_menu = QMenu(self.menuTheme)
        self.light_theme_menu.setObjectName(u"light_theme_menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTheme.menuAction())
        self.menuFile.addAction(self.save_toml)
        self.menuFile.addAction(self.load_toml)
        self.menuTheme.addAction(self.dark_theme_menu.menuAction())
        self.menuTheme.addAction(self.light_theme_menu.menuAction())
        self.menuTheme.addAction(self.no_theme_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save_toml.setText(QCoreApplication.translate("MainWindow", u"Save Toml", None))
#if QT_CONFIG(shortcut)
        self.save_toml.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.load_toml.setText(QCoreApplication.translate("MainWindow", u"Load Toml", None))
#if QT_CONFIG(shortcut)
        self.load_toml.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.save_runtime_toml.setText(QCoreApplication.translate("MainWindow", u"Save Runtime Toml", None))
        self.no_theme_action.setText(QCoreApplication.translate("MainWindow", u"No Theme", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTheme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.dark_theme_menu.setTitle(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.light_theme_menu.setTitle(QCoreApplication.translate("MainWindow", u"Light", None))
    # retranslateUi

