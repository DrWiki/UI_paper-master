import Main.Main_ui as Main
import Core.Core_ui as Core
import pyqtgraph as pg
import PyQt5
import socket

from PyQt5 import QtCore, QtGui, QtWidgets
app = pg.mkQApp("WinLayout")

class WinLayout(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(WinLayout, self).__init__(parent)
        self.Core = Core.Core_ui()
        self.Main = Main.Main_ui()
        self.Center_layout = QtWidgets.QHBoxLayout(self)
        self.Center_layout.setObjectName("Center_layout")

        self.Center_layout.addWidget(self.Core)
        self.Center_layout.addWidget(self.Main)

        self.Center_layout.setStretch(0, 0)
        self.Center_layout.setStretch(1, 2)

if __name__ == '__main__':
    win = WinLayout()
    win.show()
    pg.exec()
