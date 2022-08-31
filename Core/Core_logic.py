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
import Control
import sys
import PyQt5
import socket
import pandas as pd
import Universaltool.TransLogic.udp_logic as UDP
import Universaltool.TransLogic.Serial_logic as SER
import Universaltool.TransLogic.tcp_logic as TCP
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import time
import ctypes
import inspect
import Metadata
import struct
import pyqtgraph as pg
import binascii
import numpy as np
import Core_ui
app = pg.mkQApp("Core")

class Core_logic(Core_ui.Core_ui):
    def __init__(self,parent=None):
        super(Core_logic, self).__init__()


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
    win = Core_logic()
    win.run()
    pg.exec()

