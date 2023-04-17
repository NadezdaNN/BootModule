from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5 import QtCore
#from PyQt5 import QtGui
from FormLogo import *


class FormInf(QtWidgets.QWidget):  

    signalShow = QtCore.pyqtSignal()  
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)            
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.setWindowTitle('Информация об устройстве')
        self.setWindowFlags(Qt.FramelessWindowHint)
        cx = FormLogo.CX_global
        cy = FormLogo.CY_global
        #self.resize(300,150)
        self.resize(240,115)
        self.move(int(cx/2-self.width()/2),int(cy/2-self.height()/2))
        
        """qtRectangle = self.frameGeometry()
        print(qtRectangle)
        centerPoint = QDesktopWidget().availableGeometry().center()        
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.center())"""
                  
        with open('deviceInf.txt', 'r+') as file: # не создается, если нет
            lines = file.readlines()
        
        label = QtWidgets.QLabel()
        for i in lines:
            label.setText("".join(lines)) # Выйти без сохранения настроек?
        label.setAlignment(QtCore.Qt.AlignHCenter)                
        label.setWordWrap(True)

        buttonYes = QtWidgets.QPushButton("OK")        
        hSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)         # QtWidgets.QSizePolicy.Minimum    
        #self.gridLayout.addItem(hSpacer, 0, 1, 1, 1) 
        # hPolicy: QSizePolicy.Policy = QSizePolicy.Minimum, vPolicy: QSizePolicy.Policy = QSizePolicy.Minimum

        buttonYes.setAutoDefault(True)
        #buttonNo.setAutoDefault(True)         

        self.grid = QGridLayout(self)        
        self.grid.setAlignment(Qt.AlignCenter)
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