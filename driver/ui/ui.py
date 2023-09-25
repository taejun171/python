# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_Launcher(object):
    def setupUi(self, Launcher):
        if not Launcher.objectName():
            Launcher.setObjectName(u"Launcher")
        Launcher.resize(1174, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Launcher.sizePolicy().hasHeightForWidth())
        Launcher.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        Launcher.setFont(font)
        self.centralwidget = QWidget(Launcher)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        Launcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Launcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1174, 21))
        self.menubar.setDefaultUp(False)
        Launcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Launcher)
        self.statusbar.setObjectName(u"statusbar")
        Launcher.setStatusBar(self.statusbar)

        self.retranslateUi(Launcher)

        QMetaObject.connectSlotsByName(Launcher)
    # setupUi

    def retranslateUi(self, Launcher):
        Launcher.setWindowTitle(QCoreApplication.translate("Launcher", u"title", None))
    # retranslateUi

