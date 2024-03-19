# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_pin_dockwidget_base.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDockWidget, QGridLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QWidget)

class Ui_PowerPinDockWidgetBase(object):
    def setupUi(self, PowerPinDockWidgetBase):
        if not PowerPinDockWidgetBase.objectName():
            PowerPinDockWidgetBase.setObjectName(u"PowerPinDockWidgetBase")
        PowerPinDockWidgetBase.resize(498, 207)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.listWidget = QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)

        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        PowerPinDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(PowerPinDockWidgetBase)

        QMetaObject.connectSlotsByName(PowerPinDockWidgetBase)
    # setupUi

    def retranslateUi(self, PowerPinDockWidgetBase):
        PowerPinDockWidgetBase.setWindowTitle(QCoreApplication.translate("PowerPinDockWidgetBase", u"Power Pin PL", None))
        self.pushButton.setText(QCoreApplication.translate("PowerPinDockWidgetBase", u"Zapisz", None))
    # retranslateUi

