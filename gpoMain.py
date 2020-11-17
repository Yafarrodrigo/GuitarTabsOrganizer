# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gpoMainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(380, 150))
        MainWindow.setMaximumSize(QtCore.QSize(380, 150))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(380, 150))
        self.centralwidget.setMaximumSize(QtCore.QSize(380, 150))
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 120, 360, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(240, 40, 125, 55))
        self.startButton.setObjectName("startButton")
        self.currentFileLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentFileLabel.setGeometry(QtCore.QRect(10, 98, 375, 21))
        self.currentFileLabel.setText("")
        self.currentFileLabel.setObjectName("currentFileLabel")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(80, 50, 101, 16))
        self.infoLabel.setObjectName("infoLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 60, 191, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.directionTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.directionTextBox.setGeometry(QtCore.QRect(20, 10, 285, 25))
        self.directionTextBox.setFrame(True)
        self.directionTextBox.setObjectName("directionTextBox")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(310, 10, 55, 25))
        self.browseButton.setObjectName("browseButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 70, 191, 21))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.analyseFile = QtWidgets.QRadioButton(self.widget)
        self.analyseFile.setChecked(True)
        self.analyseFile.setObjectName("analyseFile")
        self.horizontalLayout.addWidget(self.analyseFile)
        self.copyFile = QtWidgets.QRadioButton(self.widget)
        self.copyFile.setObjectName("copyFile")
        self.horizontalLayout.addWidget(self.copyFile)
        self.moveFile = QtWidgets.QRadioButton(self.widget)
        self.moveFile.setObjectName("moveFile")
        self.horizontalLayout.addWidget(self.moveFile)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guitar Pro Organizer"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.infoLabel.setText(_translate("MainWindow", "Choose an action"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.analyseFile.setText(_translate("MainWindow", "Analyze"))
        self.copyFile.setText(_translate("MainWindow", "Copy"))
        self.moveFile.setText(_translate("MainWindow", "Move"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
