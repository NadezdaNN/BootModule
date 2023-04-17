from PyQt5 import QtWidgets
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from time import sleep
from qtwidgets import PasswordEdit
from keyboard import is_pressed 

class FormLogPass(QtWidgets.QWidget):   
    
    signalShow = QtCore.pyqtSignal()
    signalShowSettings = QtCore.pyqtSignal()
    signalShowDel = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)    
        
        cx = QApplication.desktop().width()
        cy = QApplication.desktop().height()
        self.setGeometry(0, 0, cx, cy)                

        self.labelPassword = QLabel('Пароль администратора: ')        
        self.passwordEdit = PasswordEdit(self)        
        self.labelWrongPass = QLabel('')        
        self.buttonExit = QPushButton("Выход")
        self.buttonOK = QPushButton("OK")
        
        self.buttonOK.setAutoDefault(True)
        self.buttonExit.setAutoDefault(True)
                
        self.grid = QGridLayout(self)        
        self.grid.setAlignment(Qt.AlignCenter)
        
        self.grid.addWidget(self.labelPassword, 1, 1)
        self.grid.addWidget(self.passwordEdit, 1, 2, 1, 2)           
        self.grid.addWidget(self.labelWrongPass, 2, 2, 1, 2)        
        self.grid.addWidget(self.buttonExit, 3, 2)        
        self.grid.addWidget(self.buttonOK, 3, 3)   
        
        self.setLayout(self.grid)

        self.buttonExit.clicked.connect(self.buttonExit_clicked)
        self.buttonOK.clicked.connect(self.buttonOK_clicked) 
        
    def showForm2(self):        
        self.passwordEdit.setText('') 
        self.labelWrongPass.setText('')  
        self.setStyleSheet("background-color: rgb(240, 240, 240)") 
        self.buttonOK.setStyleSheet("background-color: rgb(240, 240, 240)") 
        self.buttonExit.setStyleSheet("background-color: rgb(240, 240, 240)")  
        self.labelPassword.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.passwordEdit.setStyleSheet("background-color: white")   
        self.showFullScreen()
        

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.buttonExit_clicked()
            
        if e.key() == Qt.Key_Enter or e.key() == Qt.Key_Return:
            self.buttonOK_clicked()
        
        num=0        
        while is_pressed('F10') and num<5:            
            sleep(1)
            num+=1                     
        if num>=5:               
            self.signalShowDel.emit()
            self.setStyleSheet("background-color: lightgray") 
            self.buttonOK.setStyleSheet("background-color: lightgray") 
            self.buttonExit.setStyleSheet("background-color: lightgray")   
            self.labelPassword.setStyleSheet("background-color: lightgray")  
            self.passwordEdit.setStyleSheet("background-color: lightgray")            
    
    
    def buttonExit_clicked(self):
        self.setVisible(False)
        self.signalShow.emit()

  
    def buttonOK_clicked(self):
        password = open('password.py').read()
        password = password.rstrip('\n')
        if self.passwordEdit.text() == password:                 
            self.setVisible(False)
            self.signalShowSettings.emit()
        else:
            self.labelWrongPass.setStyleSheet("color: red")
            self.labelWrongPass.setText("Неверный пароль")           