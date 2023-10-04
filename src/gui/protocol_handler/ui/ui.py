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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDockWidget,
    QFrame, QHBoxLayout, QHeaderView, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

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
        self.action_new = QAction(Launcher)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(Launcher)
        self.action_open.setObjectName(u"action_open")
        self.action_recent = QAction(Launcher)
        self.action_recent.setObjectName(u"action_recent")
        self.action_save = QAction(Launcher)
        self.action_save.setObjectName(u"action_save")
        self.action_save_as = QAction(Launcher)
        self.action_save_as.setObjectName(u"action_save_as")
        self.action_exit = QAction(Launcher)
        self.action_exit.setObjectName(u"action_exit")
        self.centralwidget = QWidget(Launcher)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_port = QComboBox(self.centralwidget)
        self.cb_port.setObjectName(u"cb_port")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_port.sizePolicy().hasHeightForWidth())
        self.cb_port.setSizePolicy(sizePolicy1)
        self.cb_port.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.cb_port)

        self.pb_scan = QPushButton(self.centralwidget)
        self.pb_scan.setObjectName(u"pb_scan")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_scan.sizePolicy().hasHeightForWidth())
        self.pb_scan.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pb_scan)

        self.cb_baud = QComboBox(self.centralwidget)
        self.cb_baud.setObjectName(u"cb_baud")
        sizePolicy1.setHeightForWidth(self.cb_baud.sizePolicy().hasHeightForWidth())
        self.cb_baud.setSizePolicy(sizePolicy1)
        self.cb_baud.setMinimumSize(QSize(100, 0))
        self.cb_baud.setEditable(True)

        self.horizontalLayout.addWidget(self.cb_baud)

        self.pb_connect = QPushButton(self.centralwidget)
        self.pb_connect.setObjectName(u"pb_connect")
        sizePolicy2.setHeightForWidth(self.pb_connect.sizePolicy().hasHeightForWidth())
        self.pb_connect.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.pb_connect)

        self.pb_clear = QPushButton(self.centralwidget)
        self.pb_clear.setObjectName(u"pb_clear")

        self.horizontalLayout.addWidget(self.pb_clear)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tw_packet_log = QTreeWidget(self.centralwidget)
        self.tw_packet_log.setObjectName(u"tw_packet_log")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tw_packet_log.sizePolicy().hasHeightForWidth())
        self.tw_packet_log.setSizePolicy(sizePolicy3)
        self.tw_packet_log.setMinimumSize(QSize(600, 450))
        self.tw_packet_log.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tw_packet_log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tw_packet_log.setRootIsDecorated(True)
        self.tw_packet_log.setItemsExpandable(True)
        self.tw_packet_log.header().setVisible(True)
        self.tw_packet_log.header().setCascadingSectionResizes(False)
        self.tw_packet_log.header().setProperty("showSortIndicator", False)
        self.tw_packet_log.header().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.tw_packet_log)

        self.pte_raw = QPlainTextEdit(self.centralwidget)
        self.pte_raw.setObjectName(u"pte_raw")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pte_raw.sizePolicy().hasHeightForWidth())
        self.pte_raw.setSizePolicy(sizePolicy4)
        self.pte_raw.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.pte_raw.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.pte_raw)

        Launcher.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Launcher)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1174, 21))
        self.menubar.setDefaultUp(False)
        self.menu_settings = QMenu(self.menubar)
        self.menu_settings.setObjectName(u"menu_settings")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_file.setTearOffEnabled(False)
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        Launcher.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Launcher)
        self.statusbar.setObjectName(u"statusbar")
        Launcher.setStatusBar(self.statusbar)
        self.dw_protocol_list = QDockWidget(Launcher)
        self.dw_protocol_list.setObjectName(u"dw_protocol_list")
        self.dw_protocol_list.setFloating(False)
        self.dw_protocol_list.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dw_protocol_list.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.le_filter_protocol_list = QLineEdit(self.dockWidgetContents_2)
        self.le_filter_protocol_list.setObjectName(u"le_filter_protocol_list")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.le_filter_protocol_list.sizePolicy().hasHeightForWidth())
        self.le_filter_protocol_list.setSizePolicy(sizePolicy5)
        self.le_filter_protocol_list.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.le_filter_protocol_list)

        self.lw_protocol_list = QListWidget(self.dockWidgetContents_2)
        self.lw_protocol_list.setObjectName(u"lw_protocol_list")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lw_protocol_list.sizePolicy().hasHeightForWidth())
        self.lw_protocol_list.setSizePolicy(sizePolicy6)

        self.verticalLayout.addWidget(self.lw_protocol_list)

        self.dw_protocol_list.setWidget(self.dockWidgetContents_2)
        Launcher.addDockWidget(Qt.LeftDockWidgetArea, self.dw_protocol_list)
        self.dw_object_explorer = QDockWidget(Launcher)
        self.dw_object_explorer.setObjectName(u"dw_object_explorer")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.dw_object_explorer.sizePolicy().hasHeightForWidth())
        self.dw_object_explorer.setSizePolicy(sizePolicy7)
        self.dw_object_explorer.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dw_object_explorer.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.le_filter_object_explorer = QLineEdit(self.dockWidgetContents_3)
        self.le_filter_object_explorer.setObjectName(u"le_filter_object_explorer")
        self.le_filter_object_explorer.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.le_filter_object_explorer)

        self.tw_object_explorer = QTreeWidget(self.dockWidgetContents_3)
        self.tw_object_explorer.setObjectName(u"tw_object_explorer")

        self.verticalLayout_2.addWidget(self.tw_object_explorer)

        self.dw_object_explorer.setWidget(self.dockWidgetContents_3)
        Launcher.addDockWidget(Qt.RightDockWidgetArea, self.dw_object_explorer)
        self.dw_attribute_editor = QDockWidget(Launcher)
        self.dw_attribute_editor.setObjectName(u"dw_attribute_editor")
        sizePolicy7.setHeightForWidth(self.dw_attribute_editor.sizePolicy().hasHeightForWidth())
        self.dw_attribute_editor.setSizePolicy(sizePolicy7)
        self.dw_attribute_editor.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dw_attribute_editor.setAllowedAreas(Qt.RightDockWidgetArea)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.le_filter_attribute_editor = QLineEdit(self.dockWidgetContents_8)
        self.le_filter_attribute_editor.setObjectName(u"le_filter_attribute_editor")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.le_filter_attribute_editor.sizePolicy().hasHeightForWidth())
        self.le_filter_attribute_editor.setSizePolicy(sizePolicy8)
        self.le_filter_attribute_editor.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.le_filter_attribute_editor)

        self.tw_attribute_editor = QTreeWidget(self.dockWidgetContents_8)
        self.tw_attribute_editor.setObjectName(u"tw_attribute_editor")
        sizePolicy6.setHeightForWidth(self.tw_attribute_editor.sizePolicy().hasHeightForWidth())
        self.tw_attribute_editor.setSizePolicy(sizePolicy6)
        self.tw_attribute_editor.setFrameShape(QFrame.StyledPanel)
        self.tw_attribute_editor.setFrameShadow(QFrame.Sunken)
        self.tw_attribute_editor.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tw_attribute_editor.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tw_attribute_editor.setProperty("showDropIndicator", True)
        self.tw_attribute_editor.setRootIsDecorated(True)
        self.tw_attribute_editor.setUniformRowHeights(False)
        self.tw_attribute_editor.setAnimated(False)
        self.tw_attribute_editor.setAllColumnsShowFocus(False)
        self.tw_attribute_editor.setWordWrap(False)
        self.tw_attribute_editor.setHeaderHidden(False)
        self.tw_attribute_editor.header().setVisible(True)
        self.tw_attribute_editor.header().setCascadingSectionResizes(False)
        self.tw_attribute_editor.header().setHighlightSections(False)
        self.tw_attribute_editor.header().setProperty("showSortIndicator", False)
        self.tw_attribute_editor.header().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tw_attribute_editor)

        self.dw_attribute_editor.setWidget(self.dockWidgetContents_8)
        Launcher.addDockWidget(Qt.RightDockWidgetArea, self.dw_attribute_editor)
        self.dockWidget_2 = QDockWidget(Launcher)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        sizePolicy7.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy7)
        self.dockWidget_2.setMinimumSize(QSize(38, 100))
        self.dockWidget_2.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.dockWidgetContents_4 = QWidget()
        self.dockWidgetContents_4.setObjectName(u"dockWidgetContents_4")
        self.dockWidget_2.setWidget(self.dockWidgetContents_4)
        Launcher.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget_2)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_recent)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_save)
        self.menu_file.addAction(self.action_save_as)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)

        self.retranslateUi(Launcher)

        QMetaObject.connectSlotsByName(Launcher)
    # setupUi

    def retranslateUi(self, Launcher):
        Launcher.setWindowTitle(QCoreApplication.translate("Launcher", u"Protocol Analyzer", None))
        self.action_new.setText(QCoreApplication.translate("Launcher", u"New", None))
        self.action_open.setText(QCoreApplication.translate("Launcher", u"Open", None))
        self.action_recent.setText(QCoreApplication.translate("Launcher", u"Recent", None))
        self.action_save.setText(QCoreApplication.translate("Launcher", u"Save", None))
        self.action_save_as.setText(QCoreApplication.translate("Launcher", u"Save As", None))
        self.action_exit.setText(QCoreApplication.translate("Launcher", u"Exit", None))
        self.pb_scan.setText(QCoreApplication.translate("Launcher", u"Scan", None))
        self.pb_connect.setText(QCoreApplication.translate("Launcher", u"Connect", None))
        self.pb_clear.setText(QCoreApplication.translate("Launcher", u"Clear", None))
        ___qtreewidgetitem = self.tw_packet_log.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Launcher", u"Data", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Launcher", u"Length", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Launcher", u"Protocol", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Launcher", u"Time", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Launcher", u"No.", None));
        self.pte_raw.setDocumentTitle("")
        self.menu_settings.setTitle(QCoreApplication.translate("Launcher", u"Settings", None))
        self.menu_view.setTitle(QCoreApplication.translate("Launcher", u"View", None))
        self.menu_file.setTitle(QCoreApplication.translate("Launcher", u"File", None))
        self.menu_edit.setTitle(QCoreApplication.translate("Launcher", u"Edit", None))
        self.menu_help.setTitle(QCoreApplication.translate("Launcher", u"Help", None))
        self.dw_protocol_list.setWindowTitle(QCoreApplication.translate("Launcher", u"Protocol List", None))
        self.le_filter_protocol_list.setInputMask("")
        self.le_filter_protocol_list.setText("")
        self.le_filter_protocol_list.setPlaceholderText(QCoreApplication.translate("Launcher", u"filter", None))
        self.dw_object_explorer.setWindowTitle(QCoreApplication.translate("Launcher", u"Object Explorer", None))
        self.le_filter_object_explorer.setPlaceholderText(QCoreApplication.translate("Launcher", u"filter", None))
        ___qtreewidgetitem1 = self.tw_object_explorer.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Launcher", u"Type", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Launcher", u"Object", None));
        self.dw_attribute_editor.setWindowTitle(QCoreApplication.translate("Launcher", u"Attribute Editor", None))
        self.le_filter_attribute_editor.setPlaceholderText(QCoreApplication.translate("Launcher", u"filter", None))
        ___qtreewidgetitem2 = self.tw_attribute_editor.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Launcher", u"Value", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Launcher", u"Attribute", None));
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("Launcher", u"Info", None))
    # retranslateUi

