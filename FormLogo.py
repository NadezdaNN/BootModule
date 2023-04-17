import os
from PyQt5 import QtWidgets
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from MyThread import *


class FormLogo(QtWidgets.QWidget):

    CX_global = 0
    CY_global = 0
    
    startThread = QtCore.pyqtSignal(bool)
    signalShow = QtCore.pyqtSignal()
    finishedApp = QtCore.pyqtSignal(bool)
    
    def __init__(self, Sec, parent=None): 
        QtWidgets.QWidget.__init__(self, parent)
        
        self.countSec = Sec
        self.setCursor(Qt.BlankCursor)    
                
        cx = QApplication.desktop().width()
        cy = QApplication.desktop().height()        
        self.setGeometry(0, 0, cx, cy)
        self.setStyleSheet("background-color: black")   
        
        FormLogo.CX_global = cx
        FormLogo.CY_global = cy    
        
        koef=1/3
        self.label = QtWidgets.QLabel(self)        
        self.label.setGeometry(int(cx/2-cx*koef/2), int(cy/2-cy*koef/2), int(cx*koef), int(cy*koef))                          
        
        pixmap = QPixmap('Logo.png')
        pixmap = pixmap.scaled(self.label.size(),Qt.KeepAspectRatio) 
        self.label.setPixmap(pixmap)        

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setText("Нажмите F2 для доступа к настройкам... ")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setText(str(self.countSec))

        self.hbox = QtWidgets.QHBoxLayout(self)           
        self.hbox.addWidget(self.label_2, 0, Qt.AlignBottom)
        self.hbox.addWidget(self.label_3, 0, Qt.AlignBottom)
        self.hbox.addStretch(1)       
        
        self.mythread = MyThread(self.countSec)        
        self.mythread.currentValue.connect(self.on_display, QtCore.Qt.QueuedConnection)
        self.startThread.connect(self.mythread.StartOrStop, QtCore.Qt.QueuedConnection)
        self.mythread.finished.connect(self.finished, QtCore.Qt.QueuedConnection)
        self.mythread.start()    
        
    def on_display(self, s):
        self.label_3.setText(str(s))

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F2:
            self.setVisible(False)
            self.startThread.emit(False)
            self.signalShow.emit()

    def showForm1(self):
        self.label_3.setText(str(self.countSec))        
        self.showFullScreen()
        self.startThread.emit(True)        

    def finished(self):       
        nameUser=os.getlogin()
        with open('/home/' + nameUser + '/runrdp', 'r') as file:
            lines = file.readlines()
        for line in lines:                          
            if ("rdesktop" in line):                
                s = line                  
                str_tmp = s.replace("rdesktop ", "")  
                j = str_tmp.index(' ')                                         
                ip_rdp=str(str_tmp[:j])

        self.close()        
        nameUser=os.getlogin()        
        os.system(f"/home/{nameUser}/runrdp") # freeRDP or WEB
        #os.system(f"echo 'yes' | /home/{nameUser}/runrdp") # rdesktop           