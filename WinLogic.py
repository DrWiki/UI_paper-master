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
        self.Bars = [self.Main.Bar.horizontalSliderR,self.Main.Bar.horizontalSliderG,self.Main.Bar.horizontalSliderB,
                     self.Main.Bar.horizontalSliderR_2,self.Main.Bar.horizontalSliderG_2,self.Main.Bar.horizontalSliderB_2,
                     self.Main.Bar.horizontalSliderR_3,self.Main.Bar.horizontalSliderG_3,self.Main.Bar.horizontalSliderB_3]
        self.BarsLabel = [self.Main.Bar.labelR,self.Main.Bar.labelG,self.Main.Bar.labelB,
                          self.Main.Bar.labelR_2, self.Main.Bar.labelG_2, self.Main.Bar.labelB_2,
                          self.Main.Bar.labelR_3, self.Main.Bar.labelG_3, self.Main.Bar.labelB_3]
        self.timer.start(0)
        self.Core.udp_server_start()
        self.connect()


    def cam(self):
        if self.cap.isOpened():
            ret,frame = self.cap.read()
            frame = cv2.flip(frame,0)
            frame = frame.transpose(1,0,2)
            frame = cv2.flip(frame,0)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            self.Main.img.setImage(frame, autoLevels=False)

    def valueHandler(self):
        temp = self.Bars[0].value()
        tempb = temp.to_bytes(1,"big")
        self.BarsLabel[0].setText(str(temp))

        for i in range(1,self.Bars.__len__()):
            temp = self.Bars[i].value()
            self.BarsLabel[i].setText(str(temp))
            tempb = tempb + temp.to_bytes(1,"big")
        self.Core.udp_send_3(tempb)


    def connect(self):
        for i in range(self.Bars.__len__()):
            self.Bars[i].valueChanged.connect(self.valueHandler)

if __name__ == '__main__':
    win = WinLogic()
    win.show()
    pg.exec()
