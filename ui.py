# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 985)
        MainWindow.setMinimumSize(QtCore.QSize(1700, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_id = QtWidgets.QLabel(self.centralwidget)
        self.label_id.setGeometry(QtCore.QRect(1740, 490, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(28)
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.button_sampling = QtWidgets.QPushButton(self.centralwidget)
        self.button_sampling.setGeometry(QtCore.QRect(1750, 655, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(22)
        self.button_sampling.setFont(font)
        self.button_sampling.setObjectName("button_sampling")
        self.label_photo = QtWidgets.QLabel(self.centralwidget)
        self.label_photo.setGeometry(QtCore.QRect(1670, 230, 250, 250))
        self.label_photo.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_photo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_photo.setLineWidth(1)
        self.label_photo.setText("")
        self.label_photo.setObjectName("label_photo")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(1720, 614, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(18)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.label_camera = QtWidgets.QLabel(self.centralwidget)
        self.label_camera.setGeometry(QtCore.QRect(0, 0, 1700, 930))
        self.label_camera.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_camera.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_camera.setLineWidth(1)
        self.label_camera.setText("")
        self.label_camera.setObjectName("label_camera")
        self.label_enterID = QtWidgets.QLabel(self.centralwidget)
        self.label_enterID.setGeometry(QtCore.QRect(1720, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(24)
        self.label_enterID.setFont(font)
        self.label_enterID.setObjectName("label_enterID")
        self.textBrowser_status = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_status.setGeometry(QtCore.QRect(1720, 770, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.textBrowser_status.setFont(font)
        self.textBrowser_status.setDocumentTitle("")
        self.textBrowser_status.setObjectName("textBrowser_status")
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(1750, 890, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(22)
        self.button_exit.setFont(font)
        self.button_exit.setObjectName("button_exit")
        self.button_clear = QtWidgets.QPushButton(self.centralwidget)
        self.button_clear.setGeometry(QtCore.QRect(1750, 710, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(22)
        self.button_clear.setFont(font)
        self.button_clear.setObjectName("button_clear")
        self.label_photo_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_photo_2.setGeometry(QtCore.QRect(1710, 20, 200, 200))
        self.label_photo_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_photo_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_photo_2.setLineWidth(1)
        self.label_photo_2.setText("")
        self.label_photo_2.setObjectName("label_photo_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "翹課終結者3000"))
        self.label_id.setText(_translate("MainWindow", "ID"))
        self.button_sampling.setText(_translate("MainWindow", "Sampling"))
        self.label_enterID.setText(_translate("MainWindow", "Enter ID"))
        self.textBrowser_status.setPlaceholderText(_translate("MainWindow", "Sampling button to start sample  /  Clear button to clear name and ID   /  Exit button to exit"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))
        self.button_clear.setText(_translate("MainWindow", "Clear"))
