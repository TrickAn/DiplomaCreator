
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 618)
        MainWindow.setStyleSheet("background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, 0, 431, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("photo_2022-11-27_09-24-51.jpg"))
        self.label.setObjectName("label")

        self.CSV = QtWidgets.QPushButton(self.centralwidget)
        self.CSV.setGeometry(QtCore.QRect(230, 530, 81, 31))
        self.CSV.setObjectName("CSV")

        self.PDF = QtWidgets.QPushButton(self.centralwidget)
        self.PDF.setGeometry(QtCore.QRect(230, 480, 81, 31))
        self.PDF.setObjectName("PDF")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 480, 181, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.PDFopen = QtWidgets.QPushButton(self.centralwidget)
        self.PDFopen.setGeometry(QtCore.QRect(320, 480, 71, 31))
        self.PDFopen.setObjectName("PDFopen")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 480, 31, 31))
        self.label_2.setObjectName("label_2")

        self.CSVOpen = QtWidgets.QPushButton(self.centralwidget)
        self.CSVOpen.setGeometry(QtCore.QRect(320, 530, 71, 31))
        self.CSVOpen.setObjectName("CSVOpen")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 530, 181, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 530, 31, 31))
        self.label_3.setObjectName("label_3")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(70, 100, 256, 321))
        self.graphicsView.setObjectName("graphicsView")
        self.label.raise_()
        self.pushButton.raise_()
        self.CSV.raise_()
        self.PDF.raise_()
        self.lineEdit.raise_()
        self.PDFopen.raise_()
        self.label_2.raise_()
        self.CSVOpen.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.graphicsView.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diploma Creator"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.CSV.setText(_translate("MainWindow", "Выбрать файл"))
        self.PDF.setText(_translate("MainWindow", "Выбрать файл"))
        self.PDFopen.setText(_translate("MainWindow", "Открыть"))
        self.label_2.setText(_translate("MainWindow", "   PDF"))
        self.CSVOpen.setText(_translate("MainWindow", "Открыть"))
        self.label_3.setText(_translate("MainWindow", "   CSV"))


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())
