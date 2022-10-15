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
import cv2
class WinLogic(WinLayout.WinLayout):
    def __init__(self, parent=None):
        super(WinLogic, self).__init__(parent)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.cam)
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

        self.timer.start(0)

    def cam(self):
        if self.cap.isOpened():
            ret,frame = self.cap.read()
            frame = cv2.flip(frame,0)
            frame = frame.transpose(1,0,2)
            frame = cv2.flip(frame,0)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            self.Main.img.setImage(frame, autoLevels=False)

if __name__ == '__main__':
    win = WinLogic()
    win.show()
    pg.exec()
