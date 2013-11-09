# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nvidia_expo_gui.ui'
#
# Created: Wed May 29 00:06:19 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(447, 167)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.nvidia_image_label = QtGui.QLabel(Dialog)
        self.nvidia_image_label.setObjectName(_fromUtf8("nvidia_image_label"))
        self.horizontalLayout_4.addWidget(self.nvidia_image_label)
        self.amber_image_label = QtGui.QLabel(Dialog)
        self.amber_image_label.setObjectName(_fromUtf8("amber_image_label"))
        self.horizontalLayout_4.addWidget(self.amber_image_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.gtx_titan_lcdNumber = QtGui.QLCDNumber(Dialog)
        self.gtx_titan_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(0, 255, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}"))
        self.gtx_titan_lcdNumber.setObjectName(_fromUtf8("gtx_titan_lcdNumber"))
        self.horizontalLayout_2.addWidget(self.gtx_titan_lcdNumber)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gtx_640_lcdNumber = QtGui.QLCDNumber(Dialog)
        self.gtx_640_lcdNumber.setStyleSheet(_fromUtf8("QLCDNumber{\n"
"    color: rgb(0, 255, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}"))
        self.gtx_640_lcdNumber.setObjectName(_fromUtf8("gtx_640_lcdNumber"))
        self.horizontalLayout_2.addWidget(self.gtx_640_lcdNumber)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gtx_titan_run_button = QtGui.QPushButton(Dialog)
        self.gtx_titan_run_button.setObjectName(_fromUtf8("gtx_titan_run_button"))
        self.horizontalLayout.addWidget(self.gtx_titan_run_button)
        self.gtx_640_run_button = QtGui.QPushButton(Dialog)
        self.gtx_640_run_button.setObjectName(_fromUtf8("gtx_640_run_button"))
        self.horizontalLayout.addWidget(self.gtx_640_run_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout.setLayout(1, QtGui.QFormLayout.LabelRole, self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Nvidia Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Science on your desktop powered by", None, QtGui.QApplication.UnicodeUTF8))
        self.nvidia_image_label.setText(QtGui.QApplication.translate("Dialog", "nvidia image", None, QtGui.QApplication.UnicodeUTF8))
        self.amber_image_label.setText(QtGui.QApplication.translate("Dialog", "amber image", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Speed :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "ns/day", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Speed :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "ns/day", None, QtGui.QApplication.UnicodeUTF8))
        self.gtx_titan_run_button.setText(QtGui.QApplication.translate("Dialog", "Run on GTX Titan", None, QtGui.QApplication.UnicodeUTF8))
        self.gtx_640_run_button.setText(QtGui.QApplication.translate("Dialog", "Run on GTX640", None, QtGui.QApplication.UnicodeUTF8))

