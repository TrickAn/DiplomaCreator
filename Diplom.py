from DiplomaCreator import *
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap
import os
import sys


class My_Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.PDFopen.clicked.connect(self.openFile)
        self.ui.PDF.clicked.connect(self.chooseFile)
        self.filename = self.ui.lineEdit

    def chooseFile(self):
        fname = QFileDialog.getOpenFileName(self, 'open file')
        self.filename.setText(fname[0])
        self.way = self.filename.text()

    def openFile(self):
        image_path = self.ui.lineEdit.text()
        if os.path.isfile(image_path):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(image_path)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            self.ui.graphicsView.setScene(scene)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    class_instance = My_Application()
    class_instance.show()
    sys.exit(app.exec_())
