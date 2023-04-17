from PyQt5 import QtCore
import os

class MyThread(QtCore.QThread):
    currentValue = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal()
    
    def __init__(self, Sec, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.count_sec = Sec
        self.count_SEC = Sec
        self.flag = True
        
    def run(self):
        while self.count_sec>=1 & self.flag==True:
            self.sleep(1)
            self.count_sec -= 1 
            self.currentValue.emit(self.count_sec)
        if self.count_sec==0:            
            self.finished.emit()
            
    def StartOrStop(self, flag):
        if flag==True:
            self.flag = flag
            self.count_sec = self.count_SEC
            self.start()
        else:
            self.flag = flag
            
