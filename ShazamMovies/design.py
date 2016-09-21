# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(350, 652)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.radioButton = QtGui.QRadioButton(self.centralWidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 50, 100, 20))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralWidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 90, 100, 20))
        self.radioButton_2.setText(_fromUtf8(""))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(190, 90, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 50, 113, 21))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 130, 113, 32))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.listWidget = QtGui.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 160, 241, 81))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 80, 121, 31))
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.picLabel = QtGui.QLabel(self.centralWidget)
        self.picLabel.setGeometry(QtCore.QRect(100, 270, 131, 91))
        self.picLabel.setMinimumSize(QtCore.QSize(131, 91))
        self.picLabel.setText(_fromUtf8(""))
        self.picLabel.setObjectName(_fromUtf8("picLabel"))
        self.movieTitle = QtGui.QLabel(self.centralWidget)
        self.movieTitle.setGeometry(QtCore.QRect(110, 250, 131, 31))
        self.movieTitle.setText(_fromUtf8(""))
        self.movieTitle.setObjectName(_fromUtf8("movieTitle"))
        self.subtitle = QtGui.QTextEdit(self.centralWidget)
        self.subtitle.setGeometry(QtCore.QRect(50, 390, 241, 211))
        self.subtitle.setReadOnly(False)
        self.subtitle.setObjectName(_fromUtf8("subtitle"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Subtile Search", None))
        self.radioButton.setText(_translate("MainWindow", "Enter Text", None))
        self.pushButton.setText(_translate("MainWindow", "Search", None))
        self.pushButton_2.setText(_translate("MainWindow", "Start Recording", None))

