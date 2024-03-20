from os import system, getlogin
from PyQt5 import QtWidgets, QtCore, QtGui
import MyThread
import MyThread_wsgi
from PyQt5.QtCore import QSettings

class FormLogo(QtWidgets.QWidget):
        
    startThread = QtCore.pyqtSignal(bool)
    signalShow = QtCore.pyqtSignal()
    finishedApp = QtCore.pyqtSignal(bool)
        
    mysettings2 = QSettings()    
    
    def __init__(self, Sec, parent=None): 
        QtWidgets.QWidget.__init__(self, parent)        
              
        self.countSec = Sec
        self.setCursor(QtCore.Qt.BlankCursor)    
                
        cx = QtWidgets.QApplication.desktop().width()
        cy = QtWidgets.QApplication.desktop().height()     
        
        self.setGeometry(0, 0, cx, cy)
        self.setStyleSheet("background-color: black")   
                
        koef=1/3
        self.label = QtWidgets.QLabel(self)        
        self.label.setGeometry(int(cx/2-cx*koef/2), int(cy/2-cy*koef/2), int(cx*koef), int(cy*koef))
        #self.label.setAlignment(Qt.AlignHCenter)                       
        
        pixmap = QtGui.QPixmap('Logo.png')
        pixmap = pixmap.scaled(self.label.size(),QtCore.Qt.KeepAspectRatio) 
        self.label.setPixmap(pixmap)        

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_2.setText("Нажмите F2 для доступа к настройкам... ")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setText(str(self.countSec))

        self.hbox = QtWidgets.QHBoxLayout(self)           
        self.hbox.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.hbox.addWidget(self.label_3, 0, QtCore.Qt.AlignBottom)
        self.hbox.addStretch(1)       
                
        self.mythread_wsgi = MyThread_wsgi.MyThread_wsgi()        
        self.mythread_wsgi.start()
        
        self.mythread = MyThread.MyThread(self.countSec)        
        self.mythread.currentValue.connect(self.on_display, QtCore.Qt.QueuedConnection)
        self.startThread.connect(self.mythread.StartOrStop, QtCore.Qt.QueuedConnection)
        self.mythread.finished.connect(self.finished, QtCore.Qt.QueuedConnection)
        self.mythread.start()    
                        
    def on_display(self, s):
        self.label_3.setText(str(s))
        

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_F2:
            self.setVisible(False)            
            self.startThread.emit(False)
            self.signalShow.emit()


    def showForm(self):
        self.label_3.setText(str(self.countSec))        
        self.showFullScreen()
        self.startThread.emit(True)   
             

    def finished(self):       
        self.close()        
        nameUser=getlogin()        
        system(f"/home/{nameUser}/runrdp") # freeRDP or WEB