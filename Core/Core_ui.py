import argparse
from collections import deque
from time import perf_counter

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
import protocol.udp_logic as UDP
import protocol.Serial_logic as SER
import protocol.tcp_logic as TCP
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import time
import ctypes
import inspect
import struct
import pyqtgraph as pg
import binascii
import numpy as np

app = pg.mkQApp("Core")

class Core_ui(QtWidgets.QWidget,UDP.UdpLogic, TCP.TcpLogic, SER.PyQt_Serial):
    def __init__(self):
        super(Core_ui, self).__init__()
        self.Core_vertical_layout = QtWidgets.QVBoxLayout(self)
        self.Core_vertical_layout.setObjectName("Core_vertical_layout")

        self.picture = pg.ImageItem()
        self.pic_view = pg.ViewBox()
        self.pic_view.addItem(self.picture)
        self.pic_view_q = pg.widgets.GraphicsView.GraphicsView()
        self.pic_view_q.setCentralItem(self.pic_view)
        self.pic_view_q.setMaximumSize(QtCore.QSize(500, 100))


        # self.splitter = QtWidgets.QSplitter(1)
        self.children = [
            dict(name='Camera', title='Camera', type='group', children=[
                dict(name='index', type='int', value=0),
                # Parameter.create(name=f'Open', type='action'),
            ]),
            dict(name='TCP', title='TCP', type='group', children=[
                dict(name='Server', type='bool', value=True),
                dict(name='Server IP', type='str', value="0.0.0.0"),
                dict(name='Server PORT', type='int', limits=[0, 65535], value=8080),
                dict(name='Client', type='list', limits=["0.0.0.0"], value="0.0.0.0"),
            ]),
            dict(name='UDP', title='UDP', type='group', children=[
                dict(name='A IP', type='str', value="0.0.0.0"),
                dict(name='A PORT', type='int', limits=[0, 65535], value=8080),
                dict(name='B IP', type='str', value="0.0.0.0"),
                dict(name='B PORT', type='int', limits=[0, 65535], value=8080),

            ]),
            dict(name='Serial', title='Serial', type='group', children=[
                dict(name='COM', type='list', limits=["COMX"], value="COMX"),
                dict(name='BAUD RATE', type='list', limits=["9600", "115200"], value="115200"),
            ]),
            dict(name='File', title='File', type='group', children=[
                Parameter.create(name=f'Choose', type='action'),
                dict(name='Path', type='str', value="temp.csv"),
            ])
        ]
        self.Core_params = ptree.Parameter.create(name='Parameters', type='group', children=self.children)
        self.Core_tree = ptree.ParameterTree(showHeader=False)
        self.Core_tree.setParameters(self.Core_params)
        self.Core_tree.setMaximumSize(QtCore.QSize(500, 550))


        self.Dock_interaction = DockArea()
        self.dock_Terminal = Dock("Terminal", size=(1, 1))
        self.dock_Receive = Dock("Recieve", size=(1, 1), closable=True)

        self.Dock_interaction.addDock(self.dock_Terminal,'left')  ## place d1 at left edge of dock area (it will fill the whole space since there are no other docks yet)
        self.Dock_interaction.addDock(self.dock_Receive, 'right')  ## place d2 at right edge of dock area


        self.dock_Terminal_w = pg.LayoutWidget()
        self.dock_Terminal_w_Text = QtWidgets.QTextEdit()
        self.dock_Terminal_w.addWidget(self.dock_Terminal_w_Text)
        self.dock_Terminal.addWidget(self.dock_Terminal_w)

        self.dock_Receive_w = pg.LayoutWidget()
        self.dock_Receive_w_Text = QtWidgets.QTextEdit()
        self.dock_Receive_w_Text_sendline = QtWidgets.QLineEdit()
        self.dock_Receive_w_Text_send = QtWidgets.QPushButton('Button')
        self.dock_Receive_w.addWidget(self.dock_Receive_w_Text, row=0, col=0)
        self.dock_Receive_w.addWidget(self.dock_Receive_w_Text_sendline, row=1, col=0)
        self.dock_Receive_w.addWidget(self.dock_Receive_w_Text_send, row=2, col=0)
        self.dock_Receive.addWidget(self.dock_Receive_w)
        self.Dock_interaction.setMaximumSize(QtCore.QSize(500, 16777215))




        self.Core_vertical_layout.addWidget(self.pic_view_q)
        self.Core_vertical_layout.addWidget(self.Core_tree)
        self.Core_vertical_layout.addWidget(self.Dock_interaction)

        self.Core_vertical_layout.setStretch(0, 0)
        self.Core_vertical_layout.setStretch(1, 0)
        self.Core_vertical_layout.setStretch(2, 2)

    def run(self):
        self.show()

# params.child('sigopts').sigTreeStateChanged.connect(makeData)
# params.child('useOpenGL').sigValueChanged.connect(onUseOpenGLChanged)
# params.child('enableExperimental').sigValueChanged.connect(onEnableExperimentalChanged)
# params.child('pen').sigValueChanged.connect(onPenChanged)
# params.child('fill').sigValueChanged.connect(onFillChanged)
# params.child('plotMethod').sigValueChanged.connect(curve.setMethod)
# params.child('segmentedLineMode').sigValueChanged.connect(onSegmentedLineModeChanged)
# params.sigTreeStateChanged.connect(resetTimings)

if __name__ == '__main__':
    win = Core_ui()
    win.run()
    pg.exec()

