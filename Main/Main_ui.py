import argparse
from collections import deque
from time import perf_counter
import protocol.udp_logic as UDP
import protocol.tcp_logic as TCP
import protocol.Serial_logic as SER
import numpy as np
from pyqtgraph.dockarea.Dock import Dock
from pyqtgraph.dockarea.DockArea import DockArea
import pyqtgraph as pg
import pyqtgraph.functions as fn
import pyqtgraph.parametertree as ptree
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
from pyqtgraph.parametertree import Parameter
from pyqtgraph.parametertree.Parameter import PARAM_TYPES
from pyqtgraph.parametertree.parameterTypes import GroupParameter
import threading
import sys
import PyQt5
import socket
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import time
import ctypes
import inspect
import struct
import pyqtgraph as pg
import binascii
import numpy as np

app = pg.mkQApp("Main")

class Main_ui(QtWidgets.QWidget,UDP.UdpLogic, TCP.TcpLogic, SER.PyQt_Serial):
    def __init__(self):
        super(Main_ui, self).__init__()
        pg.setConfigOption('background', 'w')

        self.Main_layout = QtWidgets.QVBoxLayout(self)
        self.Main_layout.setObjectName("Main_layout")

        self.MainDockArea = DockArea()
        # self.pw = pg.PlotWidget()
        self.pw1 = pg.plot()
        self.pw2 = pg.plot()
        self.pw3 = pg.plot()
        self.pw4 = pg.plot()
        self.pw5 = pg.plot()
        self.pw6 = pg.plot()
        self.pw7 = pg.plot()

        self.Main_d1 = Dock("Dock1", size=(1, 1))
        self.Main_d2 = Dock("Dock2", size=(1, 1))
        self.Main_d3 = Dock("Dock3", size=(1, 1))
        self.Main_d4 = Dock("Dock4", size=(1, 1))
        self.Main_d5 = Dock("Dock5", size=(1, 1))
        self.Main_d6 = Dock("Dock6", size=(1, 1))
        self.Main_d7 = Dock("Dock7", size=(1, 1))

        self.saveBtn1 = QtWidgets.QPushButton('button1')
        self.restoreBtn1 = QtWidgets.QPushButton('button2')

        self.Main_d1.addWidget(self.pw1)
        self.Main_d2.addWidget(self.pw2, row=0,colspan=2)
        self.Main_d2.addWidget(self.saveBtn1, row=1, col=0)
        self.Main_d2.addWidget(self.restoreBtn1, row=1, col=1)
        self.Main_d3.addWidget(self.pw3)
        self.Main_d4.addWidget(self.pw4)
        self.Main_d5.addWidget(self.pw5)
        self.Main_d6.addWidget(self.pw6)
        self.Main_d7.addWidget(self.pw7)

        # self.Main_d2.addWidget(self.pw)
        self.MainDockArea.addDock(self.Main_d1)
        self.MainDockArea.addDock(self.Main_d2)
        self.MainDockArea.addDock(self.Main_d3)
        self.MainDockArea.addDock(self.Main_d4,'above',self.Main_d1)
        self.MainDockArea.addDock(self.Main_d5,'above',self.Main_d4)
        self.MainDockArea.addDock(self.Main_d6,'above',self.Main_d5)
        self.MainDockArea.addDock(self.Main_d7, 'above', self.Main_d6)

        self.Main_layout.addWidget(self.MainDockArea)


    def create_Main(self):
        pw = pg.PlotWidget()
        pw.setWindowTitle('pyqtgraph example: PlotSpeedTest')
        pw.setLabel('bottom', 'Index', units='B')
        curve = MonkeyCurveItem(pen=default_pen, brush='b')
        pw.addItem(curve)
        self.create()


    def run(self):
        self.show()


if __name__ == '__main__':
    win = Main_ui()
    win.run()
    pg.exec()

