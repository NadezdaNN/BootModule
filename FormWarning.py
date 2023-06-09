from PyQt5 import QtCore, QtWidgets

class FormWarning(QtWidgets.QWidget):
        
    signalHide = QtCore.pyqtSignal()
    signalShow = QtCore.pyqtSignal()
    signalHideRec = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)            
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        #self.setWindowTitle('Предупреждение')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)        
        cx = QtWidgets.QApplication.desktop().width()
        cy = QtWidgets.QApplication.desktop().height()
        self.resize(240,115)
        self.move(int(cx/2-self.width()/2),int(cy/2-self.height()/2))
        
        label = QtWidgets.QLabel("Настройки будут приняты после перезагрузки системы. Выйти без перезагрузки?")
        label.setAlignment(QtCore.Qt.AlignHCenter)
        label.setWordWrap(True)
        buttonYes = QtWidgets.QPushButton("Да")
        buttonNo = QtWidgets.QPushButton("Нет")

        buttonYes.setAutoDefault(True)
        buttonNo.setAutoDefault(True)         

        self.grid = QtWidgets.QGridLayout(self)        
        self.grid.setAlignment(QtCore.Qt.AlignCenter)
        self.grid.addWidget(label,0,0,1,2)
        self.grid.addWidget(buttonYes,1,0)
        self.grid.addWidget(buttonNo,1,1)
        self.setLayout(self.grid)

        buttonYes.clicked.connect(self.buttonYes_clicked)
        buttonNo.clicked.connect(self.buttonNo_clicked)   


    def showForm(self):
        self.show()


    def buttonYes_clicked(self):        
        self.setVisible(False)        
        self.signalHide.emit() 


    def buttonNo_clicked(self):              
        self.setVisible(False)        
        self.signalShow.emit()    