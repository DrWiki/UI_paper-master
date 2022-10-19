import RGBBar as UI
import sys
import PyQt5
import socket
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets

class RGBBarClass(UI.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(RGBBarClass, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = RGBBarClass()
    mainWindow.show()
    sys.exit(app.exec_())
