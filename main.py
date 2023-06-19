#!/usr/bin/python3

from sys import argv, exit
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import FormLogo
import FormLogPass
import FormSettings
import FormWarning
import FormInf
import FormDelSettings

if __name__ == "__main__":
    app = QApplication(argv)
        
    formLogo = FormLogo.FormLogo(5)    
    formLogPass = FormLogPass.FormLogPass()
    formSettings = FormSettings.FormSettings()      
    formWarning = FormWarning.FormWarning()    
    formInf = FormInf.FormInf() 
    formDelSettings = FormDelSettings.FormDelSettings()
           
    formLogo.signalShow.connect(formLogPass.showForm, Qt.QueuedConnection)
    formLogPass.signalShow.connect(formLogo.showForm, Qt.QueuedConnection)
    formLogPass.signalShowSettings.connect(formSettings.showForm, Qt.QueuedConnection)
    formLogPass.signalShowDel.connect(formDelSettings.showForm, Qt.DirectConnection)
    formSettings.signalShow.connect(formLogo.showForm, Qt.QueuedConnection)    
    formSettings.signalShowWarning.connect(formWarning.showForm, Qt.QueuedConnection)
    formWarning.signalHide.connect(formSettings.Exit_2_clicked, Qt.QueuedConnection)
    formWarning.signalShow.connect(formSettings.showForm, Qt.QueuedConnection)
    formSettings.signalShowInf.connect(formInf.showForm, Qt.QueuedConnection)
    formInf.signalShow.connect(formSettings.showForm, Qt.QueuedConnection)
    formDelSettings.signalHide.connect(formLogPass.showForm, Qt.QueuedConnection)
    formDelSettings.signalDelSettings.connect(formSettings.slotDelSett, Qt.QueuedConnection)
    
    formLogo.showFullScreen()      
    exit(app.exec_())    