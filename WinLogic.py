import WinLayout
import sys
import time
from time import perf_counter
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import pyqtgraph as pg
import torch
from scipy.signal import butter, lfilter, freqz
import torch.nn.functional as F
# import CNN1DTool.Braille.models as models
app = pg.mkQApp("WinLogic")

class WinLogic(WinLayout.WinLayout):
    def __init__(self, parent=None):
        super(WinLogic, self).__init__(parent)

if __name__ == '__main__':
    win = WinLogic()
    win.show()
    pg.exec()
