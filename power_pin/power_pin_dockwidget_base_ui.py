# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_pin_dockwidget_base.ui'
##
## Created by: Qt User Interface Compiler version 6.x
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
## Edytuj źródłowy plik .ui, a nie ten plik.
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)

def _qt_enum(cls, *names):
    for name in names:
        val = cls
        for part in name.split('.'):
            val = getattr(val, part, None)
            if val is None:
                break
        if val is not None:
            return val
    raise AttributeError(f"Nie znaleziono enuma {names} na {cls}")

_QT_CLICK_FOCUS = _qt_enum(Qt, 'FocusPolicy.ClickFocus', 'ClickFocus')
_QT_NO_EDIT = _qt_enum(
    __import__('PySide6.QtWidgets', fromlist=['QAbstractItemView']).QAbstractItemView,
    'EditTrigger.NoEditTriggers', 'NoEditTriggers'
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QDockWidget,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QListWidget,
    QPushButton,
    QSizePolicy,
    QWidget,
)


class Ui_PowerPinDockWidgetBase:
    def setupUi(self, PowerPinDockWidgetBase):
        if not PowerPinDockWidgetBase.objectName():
            PowerPinDockWidgetBase.setObjectName("PowerPinDockWidgetBase")
        PowerPinDockWidgetBase.resize(498, 340)

        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")

        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        # --- row 0: Dynamic View checkbox ---
        self.cb_dynamic_view = QCheckBox(self.dockWidgetContents)
        self.cb_dynamic_view.setObjectName("cb_dynamic_view")
        # ClickFocus: checkbox nie przejmuje focusu automatycznie
        self.cb_dynamic_view.setFocusPolicy(_QT_CLICK_FOCUS)
        self.gridLayout.addWidget(self.cb_dynamic_view, 0, 0, 1, 1)

        # --- row 1: Compact Mode checkbox ---
        self.cb_compact_mode = QCheckBox(self.dockWidgetContents)
        self.cb_compact_mode.setObjectName("cb_compact_mode")
        self.cb_compact_mode.setFocusPolicy(_QT_CLICK_FOCUS)
        self.gridLayout.addWidget(self.cb_compact_mode, 1, 0, 1, 1)

        # --- row 2: GitHub + autor ---
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.pushButton_3 = QPushButton(self.dockWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFocusPolicy(_QT_CLICK_FOCUS)
        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.label_2 = QLabel(self.dockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        # --- row 3: etykieta listy ---
        self.label = QLabel(self.dockWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        # --- row 4: lista portali ---
        self.listWidget = QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName("listWidget")
        # ClickFocus: lista nie blokuje map tools innych wtyczek
        self.listWidget.setFocusPolicy(_QT_CLICK_FOCUS)
        # NoEditTriggers: lista służy wyłącznie do zaznaczania;
        # poprzedni SelectedClicked blokował propagację kliknięć do mapy
        self.listWidget.setEditTriggers(_QT_NO_EDIT)
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.gridLayout.addWidget(self.listWidget, 4, 0, 1, 1)

        # --- row 5: przycisk Save ---
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)

        self.pushButton = QPushButton(self.dockWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFocusPolicy(_QT_CLICK_FOCUS)
        self.horizontalLayout.addWidget(self.pushButton)

        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        PowerPinDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(PowerPinDockWidgetBase)
        QMetaObject.connectSlotsByName(PowerPinDockWidgetBase)

    def retranslateUi(self, PowerPinDockWidgetBase):
        _tr = QCoreApplication.translate
        PowerPinDockWidgetBase.setWindowTitle(
            _tr("PowerPinDockWidgetBase", "Power Pin PL", None))
        self.cb_dynamic_view.setText(
            _tr("PowerPinDockWidgetBase", "Dynamic View (Zoom/Extent)", None))
        self.cb_dynamic_view.setToolTip(
            _tr("PowerPinDockWidgetBase",
                "If checked, uses current map scale and extent. "
                "If unchecked, uses fixed zoom and point buffer.", None))
        self.cb_compact_mode.setText(
            _tr("PowerPinDockWidgetBase", "Compact Mode (Split Button)", None))
        self.cb_compact_mode.setToolTip(
            _tr("PowerPinDockWidgetBase",
                "If checked, shows only one button with the last used portal. "
                "Others are in a dropdown.", None))
        self.pushButton_3.setText(
            _tr("PowerPinDockWidgetBase", "GitHub", None))
        self.label_2.setText(
            _tr("PowerPinDockWidgetBase", "ŁŚ 2026", None))
        self.label.setText(
            _tr("PowerPinDockWidgetBase",
                "Icons on bar (Ikony widoczne na pasku)", None))
        self.pushButton.setText(
            _tr("PowerPinDockWidgetBase", "Save (Zapisz)", None))
