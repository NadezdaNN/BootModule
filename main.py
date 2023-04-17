#!/usr/bin/python3

import sys
from PyQt5 import QtWidgets
from FormLogo import *
from FormLogPass import *
from FormSettings import *
from FormWarning import *
from FormInf import *
from FormDelSettings import*

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
        
    formLogo = FormLogo(5)    
    formLogPass = FormLogPass()
    formSettings = FormSettings()      
    formWarning = FormWarning()    
    formInf = FormInf() 
    formDelSettings = FormDelSettings()
           
    formLogo.signalShow.connect(formLogPass.showForm2, QtCore.Qt.QueuedConnection)
    formLogPass.signalShow.connect(formLogo.showForm1, QtCore.Qt.QueuedConnection)
    formLogPass.signalShowSettings.connect(formSettings.showForm3, QtCore.Qt.QueuedConnection)
    formLogPass.signalShowDel.connect(formDelSettings.showForm4, QtCore.Qt.DirectConnection)
    formSettings.signalShow.connect(formLogo.showForm1, QtCore.Qt.QueuedConnection)    
    formSettings.signalShowWarning.connect(formWarning.showForm, QtCore.Qt.QueuedConnection)
    formWarning.signalHide.connect(formSettings.Exit_2_clicked, QtCore.Qt.QueuedConnection)
    formWarning.signalShow.connect(formSettings.showForm3, QtCore.Qt.QueuedConnection)
    formSettings.signalShowInf.connect(formInf.showForm, QtCore.Qt.QueuedConnection)
    formInf.signalShow.connect(formSettings.showForm3, QtCore.Qt.QueuedConnection)
    formDelSettings.signalHide.connect(formLogPass.showForm2, QtCore.Qt.QueuedConnection)
    formDelSettings.signalDelSettings.connect(formSettings.slotDelSett, QtCore.Qt.QueuedConnection)
    
    formLogo.showFullScreen()      
    sys.exit(app.exec_())    