from PyQt5 import QtCore, QtWidgets
from os import system

class FormInf(QtWidgets.QWidget):  

    signalShow = QtCore.pyqtSignal()  
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)            
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.setWindowTitle('Информация об устройстве')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)        
        cx = QtWidgets.QApplication.desktop().width()
        cy = QtWidgets.QApplication.desktop().height()
        
        self.resize(240,115)
        self.move(int(cx/2-self.width()/2),int(cy/2-self.height()/2))  

        try:
            file = open('deviceInf.txt', 'r+')
        except: 
            system("sudo touch deviceInf.txt")
            file = open('deviceInf.txt', 'r+')     
        lines = file.readlines()                  
                
        label = QtWidgets.QLabel()
        for i in lines:
            label.setText("".join(lines)) # Выйти без сохранения настроек?
        label.setAlignment(QtCore.Qt.AlignHCenter)                
        label.setWordWrap(True)

        buttonYes = QtWidgets.QPushButton("OK")        
        hSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)           
        
        buttonYes.setAutoDefault(True)            

        self.grid = QtWidgets.QGridLayout(self)        
        self.grid.setAlignment(QtCore.Qt.AlignCenter)
        self.grid.addWidget(label,0,0,1,2)
        self.grid.addItem(hSpacer,1,0)
        self.grid.addWidget(buttonYes,1,1)
        self.setLayout(self.grid)

        buttonYes.clicked.connect(self.buttonYes_clicked)        
        
        
    def showForm(self):
        self.show()


    def buttonYes_clicked(self):        
        self.setVisible(False)        
        self.signalShow.emit()         