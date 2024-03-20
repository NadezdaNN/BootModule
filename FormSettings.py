import os
from PyQt5 import QtWidgets, QtCore
from qtwidgets import PasswordEdit
from keyboard import press_and_release
import FormSettingsD
import MyThreadNet
import MySettings
import FormLogo


class FormSettings(QtWidgets.QWidget, FormSettingsD.Ui_Form):    #QtWidgets.QWidget, ,QtWidgets.QWidget QtWidgets.QWidget, 

    signalShow = QtCore.pyqtSignal()  
    signalShowWarning = QtCore.pyqtSignal()  
    signalListWiFi = QtCore.pyqtSignal() 
    signalUpWiFi = QtCore.pyqtSignal()  
    signalUpEth = QtCore.pyqtSignal()  
    signaDialog = QtCore.pyqtSignal()
    signalShowRec = QtCore.pyqtSignal()
    signalSpace = QtCore.pyqtSignal()
    signalShowInf = QtCore.pyqtSignal()    
    signalUpVPN = QtCore.pyqtSignal() 
    signalUpVPN2 = QtCore.pyqtSignal()
    signalDownVPN = QtCore.pyqtSignal()  
    
    def __init__(self, parent=None):         
        QtWidgets.QWidget.__init__(self, parent)        
        self.ui = FormSettingsD.Ui_Form()    
        self.ui.setupUi(self)           
                
        # Переопределяем компоненты родительского класса        
        self.cx = QtWidgets.QApplication.desktop().width()
        self.cy = QtWidgets.QApplication.desktop().height()  
        self.resize(self.cx, self.cy) 
        self.widget = QtWidgets.QWidget(self)              
        self.ui.widget.move(int(self.cx/2-self.ui.widget.width()/2),int(self.cy/2-self.ui.widget.height()/2))
        self.ui.editPass = PasswordEdit()  
        self.ui.editPass.setObjectName("editPass")
        self.ui.gridLayout.addWidget(self.ui.editPass, 2, 0, 1, 3)
        self.ui.editNewPass = PasswordEdit() 
        self.ui.editNewPass.setObjectName("editNewPass")
        self.ui.gridLayout_5.addWidget(self.ui.editNewPass, 2, 0, 1, 3)
        self.ui.editPass2 = PasswordEdit()
        self.ui.editPass2.setObjectName("editPass2")
        self.ui.gridLayout_2.addWidget(self.ui.editPass2, 6, 0, 1, 2)
        self.ui.editPass_2 = PasswordEdit() 
        self.ui.editPass_2.setObjectName("editPass_2")
        self.ui.gridLayout_4.addWidget(self.ui.editPass_2, 4, 0, 1, 3)

        self.lineEdit_5 = QtWidgets.QLineEdit(self) # Новый компонент             
        self.lineEdit_5.setMaximumWidth(50)          
        self.ui.gridLayout_3.addWidget(self.lineEdit_5, 0, 4, 1, 1)        
        
        self.ui.editIP.setCursorPosition(0)
        self.ui.editIP.installEventFilter(self)             
        self.ui.editNetmask.setCursorPosition(0)
        self.ui.editNetmask.installEventFilter(self)             
        self.ui.editDHCP.setCursorPosition(0)
        self.ui.editDHCP.installEventFilter(self)                       
        self.ui.editDNS.setCursorPosition(0)
        self.ui.editDNS.installEventFilter(self)         
        self.ui.lineEdit_3.setCursorPosition(0)     
        self.ui.editAdrRDP.setCursorPosition(0) 
        self.ui.editLog2.setCursorPosition(0)
        self.ui.editPass2.setCursorPosition(0)          

        self.ui.labelNewPass.setDisabled(True)
        self.ui.editNewPass.setDisabled(True)
        self.ui.buttonTake.setDisabled(True)        
        self.ui.buttonReset.setAutoDefault(True)
        self.ui.buttonTake.setAutoDefault(True)
        self.ui.buttonTakeSett.setAutoDefault(True)
        self.ui.buttonReboot.setAutoDefault(True)
        self.ui.buttonTurnOff.setAutoDefault(True)       
        self.ui.pushButton.setIcon(QtWidgets.qApp.style().standardIcon(QtWidgets.QStyle.SP_BrowserReload)) 
        self.ui.pushButton_2.setIcon(QtWidgets.qApp.style().standardIcon(QtWidgets.QStyle.SP_FileIcon))
        
        self.ui.checkBox.clicked.connect(self.checkBox_clicked)
        self.ui.checkBox_2.clicked.connect(self.checkBox_2_clicked)
        self.ui.buttonReset.clicked.connect(self.buttonReset_clicked)
        self.ui.buttonTake.clicked.connect(self.buttonTake_clicked)
        self.ui.buttonTakeSett.clicked.connect(self.buttonTakeSett_clicked)
        self.ui.buttonReboot.clicked.connect(self.buttonReboot_clicked) 
        self.ui.buttonTurnOff.clicked.connect(self.buttonTurnOff_clicked) 
        self.ui.pushButton.clicked.connect(self.pushButton_clicked)   
        self.ui.checkBox_4.clicked.connect(self.checkBox_4_clicked)    
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_clicked)     
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_clicked)  
        self.ui.comboBox.activated.connect(self.comboBox_activated) 
        self.ui.comboBox_2.activated.connect(self.comboBox_2_activated)
        self.ui.checkBox_3.clicked.connect(self.checkBox_3_clicked)        

        self.mysettings = QtCore.QSettings() # Save settings
        self.certificate = None     
        self.countSpase = False       

        self.showSettings()              
        self.showSettingsVPN()      
        self.showSettingsRDP()    
        self.signalSpace.connect(self.whitespace, QtCore.Qt.QueuedConnection)     

        QtWidgets.QWidget.setTabOrder(self.ui.checkBox, self.ui.editIP)  
        QtWidgets.QWidget.setTabOrder(self.ui.editIP, self.ui.editNetmask)
        QtWidgets.QWidget.setTabOrder(self.ui.editNetmask, self.ui.editDHCP)
        QtWidgets.QWidget.setTabOrder(self.ui.editDHCP, self.ui.editDNS)  
        QtWidgets.QWidget.setTabOrder(self.ui.editDNS, self.ui.checkBox_2)
        QtWidgets.QWidget.setTabOrder(self.ui.checkBox_2, self.ui.pushButton)
        QtWidgets.QWidget.setTabOrder(self.ui.pushButton, self.ui.editNetSel)
        QtWidgets.QWidget.setTabOrder(self.ui.editNetSel, self.ui.editPass)
        QtWidgets.QWidget.setTabOrder(self.ui.editPass, self.ui.checkBox_4)
        QtWidgets.QWidget.setTabOrder(self.ui.checkBox_4, self.ui.comboBox)
        QtWidgets.QWidget.setTabOrder(self.ui.comboBox, self.ui.lineEdit)
        QtWidgets.QWidget.setTabOrder(self.ui.lineEdit, self.ui.lineEdit_2)
        QtWidgets.QWidget.setTabOrder(self.ui.lineEdit_2, self.ui.editLog3)
        QtWidgets.QWidget.setTabOrder(self.ui.editLog3, self.ui.editPass_2)
        QtWidgets.QWidget.setTabOrder(self.ui.editPass_2, self.ui.pushButton_2)
        QtWidgets.QWidget.setTabOrder(self.ui.pushButton_2, self.ui.editNewPass)
        QtWidgets.QWidget.setTabOrder(self.ui.editNewPass, self.ui.buttonReset)         
        QtWidgets.QWidget.setTabOrder(self.ui.buttonReset, self.ui.buttonTake)       
        QtWidgets.QWidget.setTabOrder(self.ui.buttonTake, self.ui.comboBox_2)
        QtWidgets.QWidget.setTabOrder(self.ui.comboBox_2, self.ui.lineEdit_3)
        QtWidgets.QWidget.setTabOrder(self.ui.lineEdit_3, self.ui.editAdrRDP)
        QtWidgets.QWidget.setTabOrder(self.ui.editAdrRDP, self.ui.editLog2)
        QtWidgets.QWidget.setTabOrder(self.ui.editLog2, self.ui.editPass2)
        QtWidgets.QWidget.setTabOrder(self.ui.editPass2, self.ui.checkBox_5)
        QtWidgets.QWidget.setTabOrder(self.ui.checkBox_5, self.ui.buttonTakeSett)
        QtWidgets.QWidget.setTabOrder(self.ui.buttonTakeSett, self.ui.buttonReboot)
        QtWidgets.QWidget.setTabOrder(self.ui.buttonReboot, self.ui.buttonTurnOff)
        QtWidgets.QWidget.setTabOrder(self.ui.buttonTurnOff, self.ui.pushButton_3)
        QtWidgets.QWidget.setTabOrder(self.ui.pushButton_3, self.ui.buttonTurnOff)
        QtWidgets.QWidget.setTabOrder(self.ui.buttonTurnOff, self.ui.checkBox)        
        
        self.thread = QtCore.QThread()
        self.myThreadNet = MyThreadNet.MyThreadNet()     
        self.myThreadNet.moveToThread(self.thread)
        self.thread.started.connect(self.myThreadNet.run)    
        self.signalListWiFi.connect(self.myThreadNet.listWiFi)    
        self.signalUpWiFi.connect(self.myThreadNet.upWiFi)
        self.signalUpEth.connect(self.myThreadNet.upEth)
        self.signalUpVPN.connect(self.myThreadNet.upVPN)
        self.signalUpVPN2.connect(self.myThreadNet.upVPN2)
        self.signalDownVPN.connect(self.myThreadNet.downVPN)
        self.myThreadNet.signalSetCursor.connect(self.slotSetCursor, QtCore.Qt.QueuedConnection)
        self.myThreadNet.signalSetTextEth0.connect(self.slotSetTextEth0, QtCore.Qt.QueuedConnection)
        self.myThreadNet.signalSetTextWiFi.connect(self.slotSetTextWiFi, QtCore.Qt.QueuedConnection)
        self.myThreadNet.signalPushButton.connect(self.slotPushButton, QtCore.Qt.QueuedConnection)
        self.myThreadNet.signalSetTextVPN.connect(self.slotSetTextVPN, QtCore.Qt.QueuedConnection)
        self.thread.start()

        print('123456789_init=', FormLogo.FormLogo.mysettings2.value("123"))
        if MySettings.mysettings.value("checkBox_4.isChecked")==True: # Старт VPN при загрузке ТК
            self.signalUpVPN2.emit()          
                  
        
    def slotDelSett(self):
        MySettings.mysettings.clear()  
        MySettings.mysettings.setValue("checkBox.isChecked", True)     
        MySettings.mysettings.setValue("checkBox_3.isChecked", False)        
        self.showSettings()   
        MySettings.mysettings.setValue("comboBox.text", 'IPsec/L2TP')      
        MySettings.mysettings.setValue("checkBox_4.isChecked", False)             
        self.showSettingsVPN()   
        MySettings.mysettings.setValue("comboBox_2.text", 'RDP')
        self.showSettingsRDP() 
        MySettings.mysettings.setValue("default_password", '123') # default password
                       

    def pushButton_3_clicked(self): # Кнопка Информация об устройстве
        self.ui.widget.setDisabled(True)     
        self.ui.widget.setStyleSheet("background-color: lightgray")   
        self.ui.editIP.setStyleSheet("background-color: lightgray")   
        self.ui.labelIP.setStyleSheet("background-color: lightgray")     
        self.ui.editNetmask.setStyleSheet("background-color: lightgray")
        self.ui.labelNetmask.setStyleSheet("background-color: lightgray")
        self.ui.editDHCP.setStyleSheet("background-color: lightgray")
        self.ui.labelDHCP.setStyleSheet("background-color: lightgray")
        self.ui.editDNS.setStyleSheet("background-color: lightgray")
        self.ui.labelDNS.setStyleSheet("background-color: lightgray")
        self.ui.labelSettEth.setStyleSheet("background-color: lightgray")
        self.ui.checkBox_2.setStyleSheet("background-color: lightgray")
        self.ui.pushButton.setStyleSheet("background-color: lightgray")
        self.ui.labelNetSel.setStyleSheet("background-color: lightgray")
        self.ui.labelPass.setStyleSheet("background-color: lightgray")
        self.ui.labelSettWiFi.setStyleSheet("background-color: lightgray")        
        self.ui.editNetSel.setStyleSheet("background-color: lightgray")
        self.ui.editPass.setStyleSheet("background-color: lightgray")
        self.ui.editLog3.setStyleSheet("background-color: lightgray")
        self.ui.editPass_2.setStyleSheet("background-color: lightgray")
        self.ui.editNewPass.setStyleSheet("background-color: lightgray")
        self.ui.editAdrRDP.setStyleSheet("background-color: lightgray")
        self.ui.editLog2.setStyleSheet("background-color: lightgray")
        self.ui.editPass2.setStyleSheet("background-color: lightgray")
        self.ui.comboBox.setStyleSheet("background-color: lightgray") 
        self.ui.comboBox_2.setStyleSheet("background-color: lightgray")    #    
        self.ui.checkBox_4.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit.setStyleSheet("background-color: lightgray")
        self.ui.label_4.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit_2.setStyleSheet("background-color: lightgray")  
        self.ui.label_5.setStyleSheet("background-color: lightgray")        
        self.ui.labelSettings.setStyleSheet("background-color: lightgray")
        self.ui.labelNetSel_2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass_2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass_2.setStyleSheet("background-color: lightgray")
        self.ui.pushButton_3.setStyleSheet("background-color: lightgray")
        self.ui.buttonTurnOff.setStyleSheet("background-color: lightgray")
        self.ui.buttonTakeSett.setStyleSheet("background-color: lightgray")
        self.ui.buttonReboot.setStyleSheet("background-color: lightgray")
        self.ui.label_3.setStyleSheet("background-color: lightgray")
        self.ui.pushButton_2.setStyleSheet("background-color: lightgray")
        self.ui.label.setStyleSheet("background-color: lightgray")
        self.ui.label_2.setStyleSheet("background-color: lightgray")
        self.ui.labelAdm.setStyleSheet("background-color: lightgray")
        self.ui.labelNewPass.setStyleSheet("background-color: lightgray")
        self.ui.buttonReset.setStyleSheet("background-color: lightgray")
        self.ui.buttonTake.setStyleSheet("background-color: lightgray")
        self.ui.labelConnection.setStyleSheet("background-color: lightgray")
        self.ui.label_6.setStyleSheet("background-color: lightgray")
        self.ui.labelAdrRDP.setStyleSheet("background-color: lightgray")
        self.ui.labelLog2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass2.setStyleSheet("background-color: lightgray")
        self.ui.checkBox_5.setStyleSheet("background-color: lightgray")
        self.ui.labelSettRDP.setStyleSheet("background-color: lightgray")
        self.ui.labelNotify.setStyleSheet("background-color: lightgray")                       
        self.ui.labelEth.setStyleSheet("background-color: lightgray")
        self.ui.checkBox.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit_3.setStyleSheet("background-color: lightgray")    
        self.lineEdit_5.setStyleSheet("background-color: lightgray")   
        self.ui.checkBox_3.setStyleSheet("background-color: lightgray") 
        self.setStyleSheet("background-color: lightgray")                
        
        self.signalShowInf.emit() 

    def pushButton_clicked(self): # Обновление списка WiFi-подключений
        self.setCursor(QtCore.Qt.BusyCursor) 
        self.ui.pushButton.setDisabled(True)
        self.signalListWiFi.emit()        
        #self.readListWiFi() # Wi-Fi отключен  
    
    def slotSetCursor(self):
        self.setCursor(QtCore.Qt.ArrowCursor)        

    def slotSetTextEth0(self):
        self.ui.labelSettEth.setStyleSheet("color: black")                
        self.ui.labelSettEth.setText("Настройки сохранены")  

    def slotSetTextVPN(self):        
        self.ui.label_2.setStyleSheet("color: black")
        self.ui.label_2.setText("Настройки сохранены")

    def slotSetTextWiFi(self):
        self.ui.labelSettWiFi.setStyleSheet("color: black")
        self.ui.labelSettWiFi.setText("Настройки сохранены") 

    def slotPushButton(self):
        #self.readListWiFi() # Wi-Fi отключен
        if self.ui.checkBox_2.isChecked():
            self.ui.pushButton.setDisabled(False)    
        else:
            self.ui.pushButton.setDisabled(True)

    def pushButton_2_clicked(self): # Кнопка Сертификат
        self.ui.widget.setDisabled(True)     
        self.ui.widget.setStyleSheet("background-color: lightgray")   
        self.ui.editIP.setStyleSheet("background-color: lightgray")   
        self.ui.labelIP.setStyleSheet("background-color: lightgray")     
        self.ui.editNetmask.setStyleSheet("background-color: lightgray")
        self.ui.labelNetmask.setStyleSheet("background-color: lightgray")
        self.ui.editDHCP.setStyleSheet("background-color: lightgray")
        self.ui.labelDHCP.setStyleSheet("background-color: lightgray")
        self.ui.editDNS.setStyleSheet("background-color: lightgray")
        self.ui.labelDNS.setStyleSheet("background-color: lightgray")
        self.ui.labelSettEth.setStyleSheet("background-color: lightgray")
        self.ui.checkBox_2.setStyleSheet("background-color: lightgray")
        self.ui.pushButton.setStyleSheet("background-color: lightgray")
        self.ui.labelNetSel.setStyleSheet("background-color: lightgray")
        self.ui.labelPass.setStyleSheet("background-color: lightgray")
        self.ui.labelSettWiFi.setStyleSheet("background-color: lightgray")        
        self.ui.editNetSel.setStyleSheet("background-color: lightgray")
        self.ui.editPass.setStyleSheet("background-color: lightgray")
        self.ui.editLog3.setStyleSheet("background-color: lightgray")
        self.ui.editPass_2.setStyleSheet("background-color: lightgray")
        self.ui.editNewPass.setStyleSheet("background-color: lightgray")
        self.ui.editAdrRDP.setStyleSheet("background-color: lightgray")
        self.ui.editLog2.setStyleSheet("background-color: lightgray")
        self.ui.editPass2.setStyleSheet("background-color: lightgray")
        self.ui.comboBox.setStyleSheet("background-color: lightgray")   
        self.ui.comboBox_2.setStyleSheet("background-color: lightgray")     
        self.ui.checkBox_4.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit.setStyleSheet("background-color: lightgray")
        self.ui.label_4.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit_2.setStyleSheet("background-color: lightgray")  
        self.ui.label_5.setStyleSheet("background-color: lightgray")        
        self.ui.labelSettings.setStyleSheet("background-color: lightgray")
        self.ui.labelNetSel_2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass_2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass_2.setStyleSheet("background-color: lightgray")
        self.ui.pushButton_3.setStyleSheet("background-color: lightgray")
        self.ui.buttonTurnOff.setStyleSheet("background-color: lightgray")
        self.ui.buttonTakeSett.setStyleSheet("background-color: lightgray")
        self.ui.buttonReboot.setStyleSheet("background-color: lightgray")
        self.ui.label_3.setStyleSheet("background-color: lightgray")
        self.ui.pushButton_2.setStyleSheet("background-color: lightgray")
        self.ui.label.setStyleSheet("background-color: lightgray")
        self.ui.label_2.setStyleSheet("background-color: lightgray")
        self.ui.labelAdm.setStyleSheet("background-color: lightgray")
        self.ui.labelNewPass.setStyleSheet("background-color: lightgray")
        self.ui.buttonReset.setStyleSheet("background-color: lightgray")
        self.ui.buttonTake.setStyleSheet("background-color: lightgray")
        self.ui.labelConnection.setStyleSheet("background-color: lightgray")
        self.ui.labelAdrRDP.setStyleSheet("background-color: lightgray")
        self.ui.labelLog2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass2.setStyleSheet("background-color: lightgray")
        self.ui.checkBox_5.setStyleSheet("background-color: lightgray")
        self.ui.labelSettRDP.setStyleSheet("background-color: lightgray")
        self.ui.labelNotify.setStyleSheet("background-color: lightgray")                       
        self.ui.labelEth.setStyleSheet("background-color: lightgray")
        self.ui.checkBox.setStyleSheet("background-color: lightgray")
        self.setStyleSheet("background-color: lightgray")
        
        self.dialog = QtWidgets.QFileDialog(self)
        self.dialog.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.dialog.move(int(self.cx/2-self.dialog.width()/2),int(self.cy/2-self.dialog.height()/2))           
        file = self.dialog.getOpenFileName(self.dialog, "Open File", "/media/sda1/", "All Files (*.*)") 
        self.certificate = (str(file).split(","))[0].strip("(")        
        self.signaDialog.connect(self.showDialog)     
        self.signaDialog.emit() 
        

    def showDialog(self):  
        self.ui.editIP.setStyleSheet("background-color: white")
        self.ui.editNetmask.setStyleSheet("background-color: white")
        self.ui.editDHCP.setStyleSheet("background-color: white")
        self.ui.editDNS.setStyleSheet("background-color: white")        
        self.ui.editPass.setStyleSheet("background-color: white")
        self.ui.editLog3.setStyleSheet("background-color: white")
        self.ui.editPass_2.setStyleSheet("background-color: white")
        self.ui.editNewPass.setStyleSheet("background-color: white")
        self.ui.editAdrRDP.setStyleSheet("background-color: white")
        self.ui.editLog2.setStyleSheet("background-color: white")
        self.ui.editPass2.setStyleSheet("background-color: white")
        self.ui.widget.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.showForm()
        

    def whitespace(self):         
        press_and_release("space")
              
            
    def eventFilter(self, source, event):    
        line=source.text()         
        posCurs = source.cursorPosition()      
                        
        if (event.type() == QtCore.QEvent.KeyPress and  
                ((event.key()<QtCore.Qt.Key_0 or event.key()>QtCore.Qt.Key_9) and event.key()!=QtCore.Qt.Key_Period and
                event.key()!=QtCore.Qt.Key_Left and event.key()!=QtCore.Qt.Key_Right and event.key()!=QtCore.Qt.Key_Tab and # and event.key()!=Qt.Key_Enter and event.key()!=Qt.Key_Return
                event.key()!=QtCore.Qt.Key_Escape and event.key()!=QtCore.Qt.Key_Backspace and event.key()!=QtCore.Qt.Key_Delete and event.key()!=QtCore.Qt.Key_Space)):      # and source is self.ui.editDNS     and event.key() != Qt.Key_Backspase    
            return True 
                
        if (event.type() == QtCore.QEvent.KeyPress and event.key()==QtCore.Qt.Key_Backspace):            
            if (source.hasSelectedText()):
                start = source.selectionStart()
                end = source.selectionEnd()
                source.deselect()
                line=list(line)                
                for i in range(start,end):
                    if line[i].isdigit():
                        line[i]=" "
                    i=i+1                
                line = ''.join(line).replace(" ", '')              
                source.setText(line)
                source.setCursorPosition(start)                     
                return True
            if (line[posCurs-1]=="."):
                source.setCursorPosition(posCurs-1)                           
                return True              
        
        if (event.type() == QtCore.QEvent.KeyPress and event.key()==QtCore.Qt.Key_Space):          
            if (source.hasSelectedText()):                
                source.deselect()                
            source.setCursorPosition(posCurs+1) 
            posCurs = source.cursorPosition()                
            return True

        if (event.type() == QtCore.QEvent.KeyPress and event.key()==QtCore.Qt.Key_Period):             
            if (source.hasSelectedText()):                
                source.deselect()                
            source.setCursorPosition(posCurs+1) 
            posCurs = source.cursorPosition()                
            return True
                
        if (event.type() == QtCore.QEvent.KeyPress and event.key()==QtCore.Qt.Key_Delete):            
            if (source.hasSelectedText()):
                start = source.selectionStart()
                end = source.selectionEnd()
                source.deselect()
                line=list(line)                
                for i in range(start,end):
                    if line[i].isdigit():
                        line[i]=" "
                    i=i+1                
                line = ''.join(line).replace(" ", '')              
                source.setText(line)
                source.setCursorPosition(start)                  
                return True
            if (line[posCurs]=="."):
                source.setCursorPosition(posCurs+1)                                             
                return True                      
                
        if (event.type() == QtCore.QEvent.KeyPress and (event.key() >= QtCore.Qt.Key_0 and event.key() <= QtCore.Qt.Key_9)): 
            if (source.hasSelectedText()):
                start = source.selectionStart()
                end = source.selectionEnd()
                source.deselect()
                line=list(line)                
                for i in range(start,end):
                    if line[i].isdigit():
                        line[i]=" "
                    i=i+1                
                line = ''.join(line).replace(" ", '')              
                source.setText(line)
                source.setCursorPosition(start)                          
                                
            if (posCurs>=3 and len(line)>=posCurs+1 and line[posCurs-1].isdigit() and line[posCurs-2].isdigit() and line[posCurs-3].isdigit()):
                source.setCursorPosition(posCurs+1)
                posCurs = source.cursorPosition()
                
            if ((posCurs>=0 and posCurs<=2) and line[0].isdigit() and line[1].isdigit() and line[2].isdigit() and line[3]=='.'):               
                return True    
            if (posCurs>=6 and len(line)==posCurs and line[posCurs-1].isdigit() and line[posCurs-2].isdigit() and line[posCurs-3].isdigit() and line[posCurs-4]=='.'):       
                return True
            if ((posCurs>=1 and len(line)>=(posCurs+3) and  line[posCurs-1]=="." and line[posCurs].isdigit() and line[posCurs+1].isdigit() and 
                    line[posCurs+2].isdigit()) or
                    (posCurs>=1 and len(line)>=(posCurs+2) and line[posCurs-1].isdigit() and line[posCurs].isdigit() and line[posCurs+1].isdigit()) or
                    (posCurs>=2 and len(line)>=(posCurs+1) and line[posCurs-2].isdigit() and line[posCurs-1].isdigit() and line[posCurs].isdigit()) or
                    (posCurs>=3 and len(line)>=(posCurs+4) and line[posCurs]=="." and line[posCurs+1].isdigit() and line[posCurs+2].isdigit() and 
                    line[posCurs+3].isdigit() and line[posCurs-1].isdigit() and line[posCurs-2].isdigit() and line[posCurs-3].isdigit()) or
                    (posCurs>=4 and len(line)>=(posCurs+1) and line[posCurs].isdigit() and line[posCurs-1].isdigit() and 
                    line[posCurs-2].isdigit() and line[posCurs-3]==".") or
                    (posCurs>=4 and len(line)>=(posCurs+1) and line[posCurs-1].isdigit() and line[posCurs-2].isdigit() and 
                    line[posCurs-3].isdigit() and line[posCurs-4]==".")):
                return True           
        
        return super(QtWidgets.QWidget, self).eventFilter(source, event)
        
    def showForm(self):         
        self.ui.labelNotify.setText("")
        self.ui.labelSettEth.setText("")
        self.ui.labelSettWiFi.setText("")
        self.ui.labelSettRDP.setText("")              
        
        self.ui.widget.setDisabled(False)     
        self.ui.widget.setStyleSheet("background-color: rgb(240, 240, 240)")   
        self.ui.editIP.setStyleSheet("background-color: rgb(240, 240, 240)")   
        self.ui.labelIP.setStyleSheet("background-color: rgb(240, 240, 240)")     
        self.ui.editNetmask.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelNetmask.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editDHCP.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelDHCP.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editDNS.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelDNS.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelSettEth.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.checkBox_2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.pushButton.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelNetSel.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelPass.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelSettWiFi.setStyleSheet("background-color: rgb(240, 240, 240)")        
        self.ui.editNetSel.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editPass.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editLog3.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editPass_2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editNewPass.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editAdrRDP.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editLog2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.editPass2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.comboBox.setStyleSheet("background-color: rgb(240, 240, 240)")   
        self.ui.comboBox_2.setStyleSheet("background-color: rgb(240, 240, 240)")   #     
        self.ui.checkBox_4.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.label_4.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240)")  
        self.ui.label_5.setStyleSheet("background-color: rgb(240, 240, 240)")        
        self.ui.labelSettings.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelNetSel_2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelPass_2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelPass_2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.pushButton_3.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.buttonTurnOff.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.buttonTakeSett.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.buttonReboot.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.label_3.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.pushButton_2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.label.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.label_2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelAdm.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelNewPass.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.buttonReset.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.buttonTake.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelConnection.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.label_6.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelAdrRDP.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelLog2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelPass2.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.checkBox_5.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelSettRDP.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.labelNotify.setStyleSheet("background-color: rgb(240, 240, 240)")                       
        self.ui.labelEth.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.checkBox.setStyleSheet("background-color: rgb(240, 240, 240)")       
        self.lineEdit_5.setStyleSheet("background-color: rgb(240, 240, 240)")     
        self.ui.checkBox_3.setStyleSheet("background-color: rgb(240, 240, 240)")   
        self.setStyleSheet("background-color: rgb(240, 240, 240)")
        
        self.ui.checkBox_2.setDisabled(True) # Отключение Wi-Fi

        self.ui.editAdrRDP.setStyleSheet("background-color: white")
        self.ui.editLog2.setStyleSheet("background-color: white")
        self.ui.editPass2.setStyleSheet("background-color: white")    
        self.ui.widget.setStyleSheet("background-color: rgb(240, 240, 240)")     
        self.setStyleSheet("background-color: rgb(240, 240, 240)")  
        self.ui.labelSettings.setStyleSheet("background-color: rgb(240, 240, 240)")  
        self.ui.labelEth.setStyleSheet("background-color: rgb(240, 240, 240)") 
        self.ui.checkBox.setStyleSheet("background-color: rgb(240, 240, 240)") 
        
        self.checkBox_clicked() # Button 'Получение IP автоматически'
        self.checkBox_2_clicked() # Button Wi-Fi
        self.checkBox_4_clicked() # Button VPN  
        self.comboBox_2_activated() # Button RDP
        self.checkBox_3_clicked() #VLAN
        
        self.showAdministration()                
        self.showFullScreen() 
        
    def showAdministration(self):
        self.ui.labelNewPass.setDisabled(True)
        self.ui.editNewPass.setDisabled(True)
        self.ui.editNewPass.setStyleSheet("background-color: rgb(240, 240, 240)")
        self.ui.buttonTake.setDisabled(True)


    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:            
            self.Exit_clicked()

              
    def Exit_clicked(self): # Button ESCAPE        
        self.ui.widget.setDisabled(True)     
        self.ui.widget.setStyleSheet("background-color: lightgray")   
        self.ui.editIP.setStyleSheet("background-color: lightgray")   
        self.ui.labelIP.setStyleSheet("background-color: lightgray")     
        self.ui.editNetmask.setStyleSheet("background-color: lightgray")
        self.ui.labelNetmask.setStyleSheet("background-color: lightgray")
        self.ui.editDHCP.setStyleSheet("background-color: lightgray")
        self.ui.labelDHCP.setStyleSheet("background-color: lightgray")
        self.ui.editDNS.setStyleSheet("background-color: lightgray")
        self.ui.labelDNS.setStyleSheet("background-color: lightgray")
        self.ui.labelSettEth.setStyleSheet("background-color: lightgray")
        self.ui.checkBox_2.setStyleSheet("background-color: lightgray")
        self.ui.pushButton.setStyleSheet("background-color: lightgray")
        self.ui.labelNetSel.setStyleSheet("background-color: lightgray")
        self.ui.labelPass.setStyleSheet("background-color: lightgray")
        self.ui.labelSettWiFi.setStyleSheet("background-color: lightgray")        
        self.ui.editNetSel.setStyleSheet("background-color: lightgray")
        self.ui.editPass.setStyleSheet("background-color: lightgray")
        self.ui.editLog3.setStyleSheet("background-color: lightgray")
        self.ui.editPass_2.setStyleSheet("background-color: lightgray")
        self.ui.editNewPass.setStyleSheet("background-color: lightgray")
        self.ui.editAdrRDP.setStyleSheet("background-color: lightgray")
        self.ui.editLog2.setStyleSheet("background-color: lightgray")
        self.ui.editPass2.setStyleSheet("background-color: lightgray")
        self.ui.comboBox.setStyleSheet("background-color: lightgray")   
        self.ui.comboBox_2.setStyleSheet("background-color: lightgray")    #  
        self.ui.checkBox_4.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit.setStyleSheet("background-color: lightgray")
        self.ui.label_4.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit_2.setStyleSheet("background-color: lightgray")  
        self.ui.label_5.setStyleSheet("background-color: lightgray")        
        self.ui.labelSettings.setStyleSheet("background-color: lightgray")
        self.ui.labelNetSel_2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass_2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass_2.setStyleSheet("background-color: lightgray")
        self.ui.pushButton_3.setStyleSheet("background-color: lightgray")
        self.ui.buttonTurnOff.setStyleSheet("background-color: lightgray")
        self.ui.buttonTakeSett.setStyleSheet("background-color: lightgray")
        self.ui.buttonReboot.setStyleSheet("background-color: lightgray")
        self.ui.label_3.setStyleSheet("background-color: lightgray")
        self.ui.pushButton_2.setStyleSheet("background-color: lightgray")
        self.ui.label.setStyleSheet("background-color: lightgray")
        self.ui.label_2.setStyleSheet("background-color: lightgray")
        self.ui.labelAdm.setStyleSheet("background-color: lightgray")
        self.ui.labelNewPass.setStyleSheet("background-color: lightgray")
        self.ui.buttonReset.setStyleSheet("background-color: lightgray")
        self.ui.buttonTake.setStyleSheet("background-color: lightgray")
        self.ui.labelConnection.setStyleSheet("background-color: lightgray")
        self.ui.label_6.setStyleSheet("background-color: lightgray")
        self.ui.labelAdrRDP.setStyleSheet("background-color: lightgray")
        self.ui.labelLog2.setStyleSheet("background-color: lightgray")
        self.ui.labelPass2.setStyleSheet("background-color: lightgray")
        self.ui.checkBox_5.setStyleSheet("background-color: lightgray")
        self.ui.labelSettRDP.setStyleSheet("background-color: lightgray")
        self.ui.labelNotify.setStyleSheet("background-color: lightgray")                       
        self.ui.labelEth.setStyleSheet("background-color: lightgray")
        self.ui.checkBox.setStyleSheet("background-color: lightgray")
        self.ui.lineEdit_3.setStyleSheet("background-color: lightgray")        
        self.lineEdit_5.setStyleSheet("background-color: lightgray")
        self.ui.checkBox_3.setStyleSheet("background-color: lightgray")
        self.setStyleSheet("background-color: lightgray")

        self.signalShowWarning.emit()


    def Exit_2_clicked(self):
        self.setVisible(False)
        self.signalShow.emit()        


    def checkBox_clicked(self): # Получение IP автоматически        
        if self.ui.checkBox.isChecked():            
            self.ui.editIP.setDisabled(True)      
            self.ui.editIP.setStyleSheet("background-color: rgb(240, 240, 240)")      
            self.ui.editNetmask.setDisabled(True)    
            self.ui.editNetmask.setStyleSheet("background-color: rgb(240, 240, 240)")        
            self.ui.editDHCP.setDisabled(True)  
            self.ui.editDHCP.setStyleSheet("background-color: rgb(240, 240, 240)")            
            self.ui.editDNS.setDisabled(True)  
            self.ui.editDNS.setStyleSheet("background-color: rgb(240, 240, 240)") 
                   
            self.ui.labelIP.setDisabled(True)            
            self.ui.labelNetmask.setDisabled(True)            
            self.ui.labelDHCP.setDisabled(True)            
            self.ui.labelDNS.setDisabled(True)            
            self.ui.editIP.setText('...')
            self.ui.editNetmask.setText('...') 
            self.ui.editDHCP.setText('...')
            self.ui.editDNS.setText('...')                     
            self.ui.labelSettEth.setText("")            
        else:            
            self.ui.editIP.setDisabled(False) 
            self.ui.editIP.setStyleSheet("background-color: white")             
            self.ui.editNetmask.setDisabled(False)  
            self.ui.editNetmask.setStyleSheet("background-color: white")           
            self.ui.editDHCP.setDisabled(False) 
            self.ui.editDHCP.setStyleSheet("background-color: white")            
            self.ui.editDNS.setDisabled(False)    
            self.ui.editDNS.setStyleSheet("background-color: white")                    
            self.ui.labelIP.setDisabled(False)            
            self.ui.labelNetmask.setDisabled(False)            
            self.ui.labelDHCP.setDisabled(False)            
            self.ui.labelDNS.setDisabled(False)            
            self.ui.labelSettEth.setText("")                          
                        
            if (MySettings.mysettings.value("editIP.text.static") is None):
                self.ui.editIP.setText('...')
            else:
                self.ui.editIP.setText(MySettings.mysettings.value("editIP.text.static")) 
            if MySettings.mysettings.value("editNetmask.text.static") is None:
                self.ui.editNetmask.setText('...')
            else:
                self.ui.editNetmask.setText(MySettings.mysettings.value("editNetmask.text.static")) 
            if MySettings.mysettings.value("editDHCP.text.static") is None:
                self.ui.editDHCP.setText('...')
            else:
                self.ui.editDHCP.setText(MySettings.mysettings.value("editDHCP.text.static"))
            if MySettings.mysettings.value("editDNS.text.static") is None:
                self.ui.editDNS.setText('...')
            else:
                self.ui.editDNS.setText(MySettings.mysettings.value("editDNS.text.static"))            
        

    def checkBox_2_clicked(self):   # Button Wi-Fi    
        if self.ui.checkBox_2.isChecked():
            self.ui.pushButton.setDisabled(False)              
            self.ui.label_3.setDisabled(False)            
            self.ui.editNetSel.setDisabled(False)
            self.ui.editNetSel.setStyleSheet("QComboBox"
                                        "{"
                                            "color:black;"
                                            "background-color: white;"                                            
                                        "}")
            self.ui.editPass.setDisabled(False)        
            self.ui.editPass.setStyleSheet("background-color: white")      
            self.ui.labelNetSel.setDisabled(False)                       
            self.ui.labelPass.setDisabled(False)     

            # Блок "получение IP автоматически"          
            self.ui.checkBox.setDisabled(True)  
            self.ui.editIP.setDisabled(True) 
            self.ui.editIP.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.editNetmask.setDisabled(True) 
            self.ui.editNetmask.setStyleSheet("background-color: rgb(240, 240, 240)")  
            self.ui.editDHCP.setDisabled(True) 
            self.ui.editDHCP.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.editDNS.setDisabled(True) 
            self.ui.editDNS.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelIP.setDisabled(True) 
            self.ui.labelNetmask.setDisabled(True) 
            self.ui.labelDHCP.setDisabled(True) 
            self.ui.labelDNS.setDisabled(True) 
        else:
            self.ui.pushButton.setDisabled(True) 
            self.ui.label_3.setDisabled(True)
            self.ui.editNetSel.setDisabled(True)   
            self.ui.editNetSel.setStyleSheet("background-color: rgb(240, 240, 240)")         
            self.ui.editPass.setDisabled(True)  
            self.ui.editPass.setStyleSheet("background-color: rgb(240, 240, 240)")          
            self.ui.labelNetSel.setDisabled(True)            
            self.ui.labelPass.setDisabled(True) 
            self.ui.checkBox.setDisabled(False) 
            self.checkBox_clicked()   


    def checkBox_3_clicked(self): # VLAN
        if self.ui.checkBox_3.isChecked():
            self.lineEdit_5.setStyleSheet("background-color: white")
            self.lineEdit_5.setDisabled(False) 
            #self.lineEdit_5.setText(MySettings.mysettings.value("lineEdit_5.text"))
            self.lineEdit_5.setText(FormLogo.FormLogo.mysettings2.value("123"))
            #FormLogo.FormLogo.mysettings2.setValue("123",444)
            print('main.mysettings2.value in FormSettings=', FormLogo.FormLogo.mysettings2.value("123"))
        else:
            self.lineEdit_5.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.lineEdit_5.setDisabled(True)
            self.lineEdit_5.setText('')


    def checkBox_4_clicked(self): # Включить/Выключить VPN        
        if self.ui.checkBox_4.isChecked():                    
            self.ui.comboBox.setDisabled(False) 
            self.ui.comboBox.setStyleSheet("background-color: white")    
            self.ui.lineEdit.setDisabled(False) 
            self.ui.lineEdit.setStyleSheet("background-color: white") 
            self.ui.label_4.setDisabled(False) 
            self.ui.lineEdit_2.setDisabled(False) 
            self.ui.lineEdit_2.setStyleSheet("background-color: white") 
            self.ui.label_5.setDisabled(False)                           
            self.ui.editLog3.setDisabled(False)   
            self.ui.editLog3.setStyleSheet("background-color: white")          
            self.ui.labelNetSel_2.setDisabled(False)            
            self.ui.editPass_2.setDisabled(False)
            self.ui.editPass_2.setStyleSheet("background-color: white")
            self.ui.labelPass_2.setDisabled(False)
            self.ui.pushButton_2.setDisabled(False)    
            self.ui.label.setDisabled(False)       
            self.ui.comboBox.setStyleSheet("QComboBox"
                                        "{"
                                            "color:black;"
                                            "background-color: white;"                                            
                                        "}")                           
            self.ui.comboBox.setCurrentText('IPsec/L2TP')  # Убрать, когда будет добавлен еще один VPN    
            self.comboBox_activated()   
        else:                        
            self.ui.comboBox.setDisabled(True) 
            self.ui.comboBox.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.lineEdit.setDisabled(True) 
            self.ui.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.label_4.setDisabled(True) 
            self.ui.lineEdit_2.setDisabled(True) 
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.label_5.setDisabled(True)                           
            self.ui.editLog3.setDisabled(True)   
            self.ui.editLog3.setStyleSheet("background-color: rgb(240, 240, 240)")          
            self.ui.labelNetSel_2.setDisabled(True)            
            self.ui.editPass_2.setDisabled(True)
            self.ui.editPass_2.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelPass_2.setDisabled(True)
            self.ui.pushButton_2.setDisabled(True)    
            self.ui.label.setDisabled(True)            
            self.comboBox_activated()        


    def comboBox_activated(self): # Выбор VPN
        strVPN=self.ui.comboBox.currentText().rstrip('\n').strip('\n').replace("\t", "") 
        if strVPN=="OpenVPN" and self.ui.checkBox_4.isChecked():
            self.ui.lineEdit.setDisabled(True) 
            self.ui.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.lineEdit.setText('')            
            self.ui.label_4.setDisabled(True) 
            self.ui.lineEdit_2.setDisabled(True) 
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.lineEdit_2.setText('')  
            self.ui.label_5.setDisabled(True)                           
            self.ui.editLog3.setDisabled(False)   
            self.ui.editLog3.setStyleSheet("background-color: white")  
            self.ui.editLog3.setText(MySettings.mysettings.value("editLog3.text.openvpn"))         
            self.ui.labelNetSel_2.setDisabled(False)            
            self.ui.editPass_2.setDisabled(False)
            self.ui.editPass_2.setStyleSheet("background-color: white")
            self.ui.editPass_2.setText(MySettings.mysettings.value("editPass_2.text.openvpn")) 
            self.ui.labelPass_2.setDisabled(False)
            self.ui.pushButton_2.setDisabled(False)   
            self.ui.pushButton_2.setStyleSheet("background-color: white") 
            self.ui.label.setDisabled(False)             
        elif strVPN=="IPsec/L2TP" and self.ui.checkBox_4.isChecked():
            self.ui.lineEdit.setDisabled(False) 
            self.ui.lineEdit.setStyleSheet("background-color: white") 
            self.ui.lineEdit.setText(MySettings.mysettings.value("lineEdit.text.l2tp"))
            self.ui.label_4.setDisabled(False) 
            self.ui.lineEdit_2.setDisabled(False) 
            self.ui.lineEdit_2.setStyleSheet("background-color: white") 
            self.ui.lineEdit_2.setText(MySettings.mysettings.value("lineEdit_2.text.l2tp"))
            self.ui.label_5.setDisabled(False)                           
            self.ui.editLog3.setDisabled(False)   
            self.ui.editLog3.setStyleSheet("background-color: white")     
            self.ui.editLog3.setText(MySettings.mysettings.value("editLog3.text.l2tp"))     
            self.ui.labelNetSel_2.setDisabled(False)            
            self.ui.editPass_2.setDisabled(False)
            self.ui.editPass_2.setStyleSheet("background-color: white")
            self.ui.editPass_2.setText(MySettings.mysettings.value("editPass_2.text.l2tp")) 
            self.ui.labelPass_2.setDisabled(False)
            self.ui.pushButton_2.setDisabled(True)    
            self.ui.pushButton_2.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.label.setDisabled(True) 
        

    def comboBox_2_activated(self): # Выбор Подключения Web/RDP
        strConnect=self.ui.comboBox_2.currentText().rstrip('\n').strip('\n').replace("\t", "")
        self.ui.comboBox_2.setStyleSheet("QComboBox"
                                        "{"
                                            "color:black;"
                                            "background-color: white;"                                            
                                        "}")  
        if strConnect=="Web":      
            self.ui.lineEdit_3.setText(MySettings.mysettings.value("lineEdit_3.text")) 
            self.ui.lineEdit_3.setDisabled(False)   
            self.ui.lineEdit_3.setStyleSheet("background-color: white")
            self.ui.label_6.setDisabled(False)            
            self.ui.editAdrRDP.setText('')                         
            self.ui.editAdrRDP.setDisabled(True)  
            self.ui.editAdrRDP.setStyleSheet("background-color: rgb(240, 240, 240)")    
            self.ui.labelAdrRDP.setDisabled(True)        
            self.ui.editLog2.setText('')  
            self.ui.editLog2.setDisabled(True)  
            self.ui.editLog2.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelLog2.setDisabled(True)      
            self.ui.editPass2.setText('')  
            self.ui.editPass2.setDisabled(True) 
            self.ui.editPass2.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelPass2.setDisabled(True)
            self.ui.checkBox_5.setChecked(False)
            self.ui.checkBox_5.setDisabled(True)   
            self.ui.labelSettRDP.setText('')                       

        elif strConnect=="RDP":            
            self.ui.lineEdit_3.setText('') 
            self.ui.lineEdit_3.setDisabled(True)   
            self.ui.lineEdit_3.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.label_6.setDisabled(True)            
            self.ui.editAdrRDP.setText(MySettings.mysettings.value("editAdrRDP.text"))                         
            self.ui.editAdrRDP.setDisabled(False)  
            self.ui.editAdrRDP.setStyleSheet("background-color: white")
            self.ui.labelAdrRDP.setDisabled(False)
            self.ui.editLog2.setText(MySettings.mysettings.value("editLog2.text"))  
            self.ui.editLog2.setDisabled(False)  
            self.ui.editLog2.setStyleSheet("background-color: white")
            self.ui.labelLog2.setDisabled(False)      
            self.ui.editPass2.setText(MySettings.mysettings.value("editPass2.text"))  
            self.ui.editPass2.setDisabled(False) 
            self.ui.editPass2.setStyleSheet("background-color: white")
            self.ui.labelPass2.setDisabled(False)
            self.ui.labelSettRDP.setText('') 
            if MySettings.mysettings.value("checkBox_5.isChecked")=='true':
                self.ui.checkBox_5.setChecked(True)
            else:
                self.ui.checkBox_5.setChecked(False)             
            self.ui.checkBox_5.setDisabled(False)      
            

    def buttonReset_clicked(self): #Сброс пароля        
        self.ui.labelNotify.setText("")   
        self.ui.editNewPass.setText("")   
        self.ui.labelNotify.setDisabled(False)
        self.ui.labelNewPass.setDisabled(False)        
        self.ui.editNewPass.setDisabled(False)    
        self.ui.editNewPass.setStyleSheet("background-color: white")     
        self.ui.buttonTake.setDisabled(False)


    def buttonTake_clicked(self):  #Принять (пароль)       
        if not self.ui.editNewPass.text(): # .rstrip(' ')
            self.ui.labelNotify.setStyleSheet("color: red")
            self.ui.labelNotify.setText("Введите пароль")            
        else:
            
            filePassword=open('pass.txt', 'w')            
            filePassword.write(self.ui.editNewPass.text())               
            filePassword.close()    
            self.ui.editNewPass.setText('')
            self.ui.labelNotify.setStyleSheet("color: black")
            self.ui.labelNotify.setText("Пароль принят")  
            self.ui.labelNotify.setDisabled(True) # ???         
            self.ui.labelNewPass.setDisabled(True)        
            self.ui.editNewPass.setDisabled(True)        
            self.ui.buttonTake.setDisabled(True) 


    def buttonTakeSett_clicked(self): #Сохранить/принять настройки        
        self.ui.labelSettEth.setText("") 
        self.ui.labelSettWiFi.setText("") 
        self.ui.labelSettRDP.setText("")        

        if self.ui.editNewPass.text()!='':
            self.ui.labelNotify.setStyleSheet("color: red")
            self.ui.labelNotify.setText('Пароль не был принят')  
                
        # Wi-Fi
        str_wifi=self.ui.editNetSel.currentText().rstrip('\n').strip('\n').replace("\t", "")       
        if (self.ui.checkBox_2.isChecked()):            
            if (str_wifi!="" and len(self.ui.editPass.text())>=8 and len(self.ui.editPass.text())<=64):  # >=8      
                if (self.loginwifi == self.ui.editNetSel.currentText() and self.psk == self.ui.editPass.text()):
                    self.ui.labelSettWiFi.setStyleSheet("color: black")                    
                    self.ui.labelSettWiFi.setText("")   
                else:          
                    self.setCursor(QtCore.Qt.BusyCursor)                
                    os.system('wpa_passphrase "' + self.ui.editNetSel.currentText() + '" ' + self.ui.editPass.text() + "> wpa_pass.py")             
                    with open('wpa_pass.py', 'r') as file:
                        lines = file.readlines()
                    i=0
                    for line in lines:     
                        if ("psk=" in line): 
                            str_psk = lines[i]                                              
                            psk = str_psk.replace("\t", "").replace("psk=", "").replace(" ", "").rstrip('\n').replace(" ", "")
                        i=i+1    

                    path_str='/etc/wpa_supplicant/wpa_supplicant.conf'            
                    with open(path_str, 'r+') as file: # не создается, если нет
                        lines = file.readlines()
                    os.system("sudo chmod u+x " + path_str)
            
                    flag = False
                    i=0
                    for line in lines:     
                        if ("network={" in line):                                               
                            flag = True                                       
                            lines[i]="network={\n"           
                        if ("ssid=" in line and flag==True):            
                            lines[i] = ""
                            lines[i] = '\tssid="'+self.ui.editNetSel.currentText()+'"\n'
                        if ("psk=" in line and flag==True):            
                            lines[i] = ""
                            lines[i] = '\tpsk=' + psk + '\n'                
                        i=i+1      
                
                    with open(path_str, 'w+') as file:
                        file.writelines(lines)                
                        file.close()
                        if (flag == False): # пишем в конец файла                    
                            file=open(path_str, 'w+')
                            file.writelines(lines)                 
                            file.write("network={\n")                    
                            file.write('\tssid="'+self.ui.editNetSel.currentText()+'"\n')
                            file.write('\tpsk=' + psk + '\n')                
                            file.write('}') 
            
                    with open("/etc/network/interfaces", 'w+') as file:           
                        file.write('auto lo\n')
                        file.write('iface lo inet loopback\n')
                        file.write('auto wlan0\n')
                        file.write('allow-hotplug wlan0\n')
                        file.write('iface wlan0 inet manual\n')
                        file.write('\twpa-conf '+path_str+' \n')
                        file.write('iface wlan0 inet dhcp\n')       

                    file=open('/etc/dhcpcd.conf', 'r+')
                    lines = file.readlines()
                    flag = False                    
                    for i,line in enumerate(lines):                   
                        if ("nodhcp" in line):                     
                            lines[i] = "" 
                            flag = True
                        if ("interface eth0" in line) and flag == True:            
                            lines[i] = ""
                        if ("static ip_address=" in line) and flag == True:            
                            lines[i] = ""
                        if ("static netmask=" in line) and flag == True:          
                            lines[i] = ""
                        if ("static routers=" in line) and flag == True:            
                            lines[i] = ""
                        if ("static domain_name_servers=" in line) and flag == True:           
                            lines[i] = ""         
                    file=open('/etc/dhcpcd.conf', 'w+')
                    file.writelines(lines) 
                    file.close()
                            
                    self.loginwifi = self.ui.editNetSel.currentText()  
                    self.psk = self.ui.editPass.text()
                    self.signalUpWiFi.emit() # Настройки сохранены                       
            else: 
                self.ui.labelSettWiFi.setStyleSheet("color: red")
                self.ui.labelSettWiFi.setText("Ввод недопустимых значений")

        else: #Ethernet                        
            if self.ui.checkBox.isChecked(): #динамический IP-адрес     
                print('123=', MySettings.mysettings.value("lineEdit_5.text"))
                if (str(self.ui.checkBox.isChecked()).lower() != str(MySettings.mysettings.value("checkBox.isChecked"))) or \
                        (str(self.ui.checkBox_3.isChecked()).lower() != str(MySettings.mysettings.value("checkBox_3.isChecked"))) or \
                        (self.lineEdit_5.text() != MySettings.mysettings.value("lineEdit_5.text"))    :                            

                    self.setCursor(QtCore.Qt.BusyCursor) 

                    try:
                        file = open('/etc/dhcpcd.conf', 'r+')
                    except: 
                        os.system("sudo touch /etc/dhcpcd.conf")
                        file = open('/etc/dhcpcd.conf', 'r+')

                    lines = file.readlines()
                    flag = False
                
                    for i,line in enumerate(lines):                   
                        if ("nodhcp" in line):                     
                            lines[i] = "" 
                            flag = True
                        if ("interface eth0" in line) and flag == True:            
                            lines[i] = ""
                        if ("static ip_address=" in line) and flag == True:            
                            lines[i] = ""
                        if ("static netmask=" in line) and flag == True:          
                            lines[i] = ""
                        if ("static routers=" in line) and flag == True:            
                            lines[i] = ""
                        if ("static domain_name_servers=" in line) and flag == True:           
                            lines[i] = ""  
                        if ("static gateway=" in line) and flag == True:           
                            lines[i] = ""   
                    #file.close()
                    with open('/etc/dhcpcd.conf', 'w+') as file:
                        file.writelines(lines)                     

                    try:
                        file = open('/etc/network/interfaces', 'w+')
                    except: 
                        os.system("sudo touch /etc/network/interfaces")
                        file = open('/etc/network/interfaces', 'w+')
                              
                    file.write('auto lo\n')
                    file.write('iface lo inet loopback\n')
                    file.write('auto eth0\n')
                    file.write('iface eth0 inet dhcp\n')
                    if self.ui.checkBox_3.isChecked(): # VLAN
                        if self.lineEdit_5.text().replace(' ','') == '':
                            self.lineEdit_5.setText('1')                            
                        file.write(f'auto eth0.{self.lineEdit_5.text()}\n')
                        file.write(f'iface eth0.{self.lineEdit_5.text()} inet dhcp\n')                        
                    print('741=', self.ui.checkBox_3.isChecked())
                    MySettings.mysettings.setValue("checkBox.isChecked", self.ui.checkBox.isChecked())
                    MySettings.mysettings.setValue("checkBox_3.isChecked", self.ui.checkBox_3.isChecked())
                    MySettings.mysettings.setValue("lineEdit_5.text", self.lineEdit_5.text())
                                        
                    self.signalUpEth.emit()
                else:
                    pass # Настройки были сохранены ранее

            else: #статический IP-адрес
                flag = True
                flag3, flag4 = False, False

                str0 = self.ui.editIP.text().rstrip('\n').split(".",4)      # IP
                str1 = self.ui.editNetmask.text().rstrip('\n').split(".",4) # Netmask
                str2 = self.ui.editDHCP.text().rstrip('\n').split(".",4)    # DHCP
                str3 = self.ui.editDNS.text().rstrip('\n').split(".",4)     # DNS
                                
                for i in range(4):
                    if not str0[i].isdigit():                    
                        flag = False
                    if not str1[i].isdigit():                    
                        flag = False
                    if str2[i].isdigit():                   
                        flag3 = True
                    if str3[i].isdigit():                  
                        flag4 = True                    

                if flag:
                    if (self.ui.editIP.text()==MySettings.mysettings.value("editIP.text.static") and 
                            self.ui.editNetmask.text()==MySettings.mysettings.value("editNetmask.text.static") and
                            self.ui.editDHCP.text()==MySettings.mysettings.value("editDHCP.text.static") and 
                            self.ui.editDNS.text()==MySettings.mysettings.value("editDNS.text.static") and                            
                            str(self.ui.checkBox.isChecked()).lower() == str(MySettings.mysettings.value("checkBox.isChecked")) and
                            str(self.ui.checkBox_3.isChecked()).lower() == str(MySettings.mysettings.value("checkBox_3.isChecked")) and
                            self.lineEdit_5.text()==MySettings.mysettings.value("lineEdit_5.text")):                             
                        #pass
                        print('1234=', MySettings.mysettings.value("lineEdit_5.text"))
                    else:
                        self.setCursor(QtCore.Qt.BusyCursor)                         
                        try:
                            file = open('/etc/dhcpcd.conf', 'r+')
                        except: 
                            os.system("sudo touch /etc/dhcpcd.conf")
                            file = open('/etc/dhcpcd.conf', 'r+')

                        lines = file.readlines()            
                        flag = False           
                        flag_dhcp = True
                        flag_dns = True                        
                                                
                        for i,line in enumerate(lines):                                                 
                            if ("nodhcp" in line):                                               
                                flag = True                                       
                                lines[i]="nodhcp\n"                    
                            if "interface eth0" == line and flag == True:                                          
                                lines[i] = "interface eth0\n"

                            if ("static ip_address=" in line) and flag == True:                            
                                lines[i] = 'static ip_address=' + self.ui.editIP.text() + '\n'
                            if ("static netmask=" in line) and flag == True:                        
                                lines[i] = 'static netmask=' + self.ui.editNetmask.text() + '\n'
                                                        
                            if ("static routers=" in line) and flag:                                
                                if '...' in self.ui.editDHCP.text():
                                    lines[i] = ''
                                else:
                                    lines[i] = 'static routers=' + self.ui.editDHCP.text() + '\n'
                                flag_dhcp = False

                            if ("static domain_name_servers=" in line) and flag:                                       
                                if bool(self.ui.editDNS.text().count('...')):
                                    lines[i] = ''
                                else:
                                    lines[i] = 'static domain_name_servers=' + self.ui.editDNS.text() + '\n'
                                flag_dns = False                            

                        if flag_dhcp and flag3 and flag:
                            lines.append(f'static routers={self.ui.editDHCP.text()}\n')
                        if flag_dns and flag4 and flag:
                            lines.append(f'static domain_name_servers={self.ui.editDNS.text()}\n')      

                        if self.ui.checkBox_3.isChecked(): # VLAN
                            flagVLAN = False
                            if self.lineEdit_5.text().replace(' ','') == '':
                                self.lineEdit_5.setText('1')    
                            print('dhcp vlan')
                            for i,line in enumerate(lines):    
                                if ("interface eth0." in line):                                          
                                    lines[i] = str(f'interface eth0.{self.lineEdit_5.text()}\n')      
                                    flagVLAN = True                              
                                if ("static ip_address=" in line) and flagVLAN:                            
                                    lines[i] = 'static ip_address=' + self.ui.editIP.text() + '\n'
                                if ("static netmask=" in line) and flagVLAN:                        
                                    lines[i] = 'static netmask=' + self.ui.editNetmask.text() + '\n'                                                            
                                
                                if ("static routers=" in line) and flagVLAN:                                
                                    if '...' in self.ui.editDHCP.text():
                                        lines[i] = ''
                                    else:
                                        lines[i] = 'static routers=' + self.ui.editDHCP.text() + '\n'
                                    flag_dhcp = False

                                if ("static domain_name_servers=" in line) and flagVLAN:                                       
                                    if bool(self.ui.editDNS.text().count('...')):
                                        lines[i] = ''
                                    else:
                                        lines[i] = 'static domain_name_servers=' + self.ui.editDNS.text() + '\n'
                                    flag_dns = False                            

                            if flag_dhcp and flag3 and flag:
                                lines.append(f'static routers={self.ui.editDHCP.text()}\n')
                            if flag_dns and flag4 and flag:
                                lines.append(f'static domain_name_servers={self.ui.editDNS.text()}\n')    
                        else:
                            flagNoVPN = False  
                            for i,line in enumerate(lines):                                                          
                                if ("interface eth0." in line) and flag == True:            
                                    lines[i] = ""
                                    flagNoVPN = True
                                if ("static ip_address=" in line) and flagNoVPN:            
                                    lines[i] = ""
                                if ("static netmask=" in line) and flagNoVPN:          
                                    lines[i] = ""
                                if ("static routers=" in line) and flagNoVPN:            
                                    lines[i] = ""
                                if ("static domain_name_servers=" in line) and flagNoVPN:           
                                    lines[i] = ""  
                                if ("static gateway=" in line) and flagNoVPN:           
                                    lines[i] = ""                  
                        
                        with open('/etc/dhcpcd.conf', 'w+') as file:
                            file.writelines(lines)                            

                        if (flag == False): #пишем в конец файла                    
                            file=open('/etc/dhcpcd.conf', 'w+')
                            file.writelines(lines)                 
                            file.write("\nnodhcp\n")
                            file.write('interface eth0\n')
                            file.write(f'static ip_address={self.ui.editIP.text()}\n')
                            file.write(f'static netmask={self.ui.editNetmask.text()}\n')
                            if self.ui.editDHCP.text()=='...':
                                pass
                            else:
                                file.write(f'static routers={self.ui.editDHCP.text()}\n') 
                            if self.ui.editDNS.text()=='...':
                                pass
                            else:
                                file.write(f'static domain_name_servers={self.ui.editDNS.text()}\n') 

                            if self.ui.checkBox_3.isChecked(): #VLAN                                
                                file.write(f'interface eth0.{self.lineEdit_5.text()}\n')
                                file.write(f'static ip_address={self.ui.editIP.text()}\n')
                                file.write(f'static netmask={self.ui.editNetmask.text()}\n')
                                if self.ui.editDHCP.text()=='...':
                                    pass
                                else:
                                    file.write(f'static routers={self.ui.editDHCP.text()}\n') 
                                if self.ui.editDNS.text()=='...':
                                    pass
                                else:
                                    file.write(f'static domain_name_servers={self.ui.editDNS.text()}\n')  
                            file.close()
                        
                        try:
                            file=open("/etc/network/interfaces", 'w+')
                        except: 
                            os.system("sudo touch /etc/network/interfaces")
                            file=open("/etc/network/interfaces", 'w+')
                                     
                        file.write('auto lo\n')
                        file.write('iface lo inet loopback\n')
                        file.write('auto eth0\n')
                        file.write('iface eth0 inet static\n')
                        file.write(f'address {self.ui.editIP.text()}\n')
                        file.write(f'netmask {self.ui.editNetmask.text()}\n')
                        if self.ui.editDNS.text().count('...'):
                            pass
                        else:
                            file.write(f'gateway {self.ui.editDHCP.text()}\n')
                        if self.ui.editDNS.text().count('...'):
                            pass
                        else:
                            file.write(f'dns-nameservers {self.ui.editDNS.text()}\n')                             
                        
                        if self.ui.checkBox_3.isChecked(): # VLAN 
                            if self.lineEdit_5.text() is None:
                                self.lineEdit_5.setText('1')
                            file.write(f'auto eth0.{self.lineEdit_5.text()}\n')
                            file.write(f'iface eth0.{self.lineEdit_5.text()} inet static\n')
                            file.write(f'address {self.ui.editIP.text()}\n')
                            file.write(f'netmask {self.ui.editNetmask.text()}\n')
                            if self.ui.editDNS.text().count('...'):
                                pass
                            else:
                                file.write(f'gateway {self.ui.editDHCP.text()}\n')
                            if self.ui.editDNS.text().count('...'):
                                pass
                            else:
                                file.write(f'dns-nameservers {self.ui.editDNS.text()}\n')                                          
                        
                        file.close()

                        MySettings.mysettings.setValue("checkBox.isChecked", self.ui.checkBox.isChecked())
                        MySettings.mysettings.setValue("editIP.text.static", self.ui.editIP.text()) 
                        MySettings.mysettings.setValue("editNetmask.text.static", self.ui.editNetmask.text()) 
                        MySettings.mysettings.setValue("editDHCP.text.static", self.ui.editDHCP.text())
                        MySettings.mysettings.setValue("editDNS.text.static", self.ui.editDNS.text())                        
                        MySettings.mysettings.setValue("checkBox.isChecked", self.ui.checkBox.isChecked())
                        MySettings.mysettings.setValue("checkBox_3.isChecked", self.ui.checkBox_3.isChecked())                        
                        MySettings.mysettings.setValue("lineEdit_5.text", self.lineEdit_5.text())
                        
                        self.signalUpEth.emit()                        
                else:
                    self.ui.labelSettEth.setStyleSheet("color: red")
                    self.ui.labelSettEth.setText("Ввод недопустимых значений")            
        # VPN
        if self.ui.checkBox_4.isChecked():       
            
            if self.ui.comboBox.currentText()=='OpenVPN':      
                if (self.ui.comboBox.currentText()==MySettings.mysettings.value("comboBox.text") and                        
                        self.ui.editLog3.text()==MySettings.mysettings.value("editLog3.text.openvpn") and 
                        self.ui.editPass_2.text()==MySettings.mysettings.value("editPass_2.text.openvpn")):
                    pass
                else:
                    MySettings.mysettings.setValue("comboBox.text", self.ui.comboBox.currentText())                 
                    MySettings.mysettings.setValue("editLog3.text.openvpn", self.ui.editLog3.text())
                    MySettings.mysettings.setValue("editPass_2.text.openvpn", self.ui.editPass_2.text())
                    self.ui.label_2.setStyleSheet("color: black")
                    self.ui.label_2.setText("Настройки сохранены")             

                    if self.certificate != None:
                        os.system(f'sudo cp {self.certificate} /etc/openvpn/client.conf')

                    if os.path.exists('/etc/openvpn/client.conf'):    
                        self.setCursor(QtCore.Qt.BusyCursor)        
                        nameUser=os.getlogin()
                        with open('/home/' + nameUser + '/pass_vpn.txt', 'w+') as file:                    
                            file.write(f'{self.ui.editLog3.text()}\n{self.ui.editPass_2.text()}')  

                        with open('/etc/openvpn/client.conf', 'r+') as file: 
                            lines = file.readlines()     
                        
                        flag_user = True 
                        for i,line in enumerate(lines):     
                            if ("auth-user-pass" in line):                         
                                flag_user = False                                    
                                lines[i]=f'auth-user-pass /home/{nameUser}/pass_vpn.txt\n'     
                                
                        if flag_user:
                            lines.append(f'\nauth-user-pass /home/{nameUser}/pass_vpn.txt')
                            
                        with open('/etc/openvpn/client.conf', 'w+') as file:     
                            file.writelines(lines)

                        self.signalUpVPN.emit()
                    else:
                        self.ui.label_2.setStyleSheet("color: red")
                        self.ui.label_2.setText("Ввод недопустимых значений")

            if self.ui.comboBox.currentText()=='IPsec/L2TP':
                if (self.ui.comboBox.currentText()==MySettings.mysettings.value("comboBox.text") and
                        self.ui.lineEdit.text()==MySettings.mysettings.value("lineEdit.text.l2tp") and 
                        self.ui.lineEdit_2.text()==MySettings.mysettings.value("lineEdit_2.text.l2tp") and
                        self.ui.editLog3.text()==MySettings.mysettings.value("editLog3.text.l2tp") and 
                        self.ui.editPass_2.text()==MySettings.mysettings.value("editPass_2.text.l2tp") and
                        self.ui.editAdrRDP.text()==MySettings.mysettings.value("editAdrRDP.text")):
                    if str(self.ui.checkBox_4.isChecked()).lower() == str(MySettings.mysettings.value("checkBox_4.isChecked")).lower():
                        pass
                    else:                
                        self.setCursor(QtCore.Qt.BusyCursor)        
                        self.signalUpVPN.emit()   
                else:
                    if (self.ui.lineEdit.text()!='' and self.ui.lineEdit_2.text()!='' and self.ui.editLog3.text()!="" and self.ui.editPass_2.text()!= ""):   
                        self.setCursor(QtCore.Qt.BusyCursor)
                        with open('/etc/ipsec.conf', 'r+') as file: 
                            lines = file.readlines() 
                            flag=False
                            for i,line in enumerate(lines): 
                                if "conn myvpn" in line:
                                    flag=True                                                 
                                if ("  right=" in line) and flag:                          
                                    lines[i]=f'  right={self.ui.lineEdit.text()}\n'  
                        file=open('/etc/ipsec.conf', 'w+')
                        file.writelines(lines)  
                        file.close()    

                        os.system('sudo chmod 600 /etc/ipsec.secrets')
                        with open('/etc/ipsec.secrets', 'w+') as file:                    
                            file.write(f': PSK "{self.ui.lineEdit_2.text()}"')                          

                        with open('/etc/xl2tpd/xl2tpd.conf', 'r+') as file: 
                            lines = file.readlines() 
                            flag=False
                            for i,line in enumerate(lines): 
                                if "[lac myvpn]" in line:
                                    flag=True                                                 
                                if ("lns =" in line) and flag:                          
                                    lines[i]=f'lns = {self.ui.lineEdit.text()}\n'  
                        file=open('/etc/xl2tpd/xl2tpd.conf', 'w+')
                        file.writelines(lines)  
                        file.close()    

                        with open('/etc/ppp/options.l2tpd.client', 'r+') as file: 
                            lines = file.readlines()                         
                            for i,line in enumerate(lines): 
                                if "name" in line:
                                    lines[i]=f'name "{self.ui.editLog3.text()}"\n'                                               
                                if ("password" in line) and flag:                          
                                    lines[i]=f'password "{self.ui.editPass_2.text()}"'  
                        file=open('/etc/ppp/options.l2tpd.client', 'w+')
                        file.writelines(lines)  
                        file.close()                                            

                        os.system(f'echo {self.ui.lineEdit.text()} > ip_server_vpn.txt')
                        os.system(f'echo {self.ui.editAdrRDP.text()} > ip_rdp.txt')                                    
                        
                        MySettings.mysettings.setValue("comboBox.text", self.ui.comboBox.currentText()) 
                        MySettings.mysettings.setValue("lineEdit.text.l2tp", self.ui.lineEdit.text()) 
                        MySettings.mysettings.setValue("lineEdit_2.text.l2tp", self.ui.lineEdit_2.text())
                        MySettings.mysettings.setValue("editLog3.text.l2tp", self.ui.editLog3.text())
                        MySettings.mysettings.setValue("editPass_2.text.l2tp", self.ui.editPass_2.text())
                        
                        self.ui.label_2.setStyleSheet("color: black")
                        self.ui.label_2.setText("Настройки сохранены")
                        self.signalUpVPN.emit()                                           
                    else:
                        self.ui.label_2.setStyleSheet("color: red")
                        self.ui.label_2.setText("Ввод недопустимых значений")   

            MySettings.mysettings.setValue("checkBox_4.isChecked", self.ui.checkBox_4.isChecked())            
        else:            
            if str(self.ui.checkBox_4.isChecked()).lower() == str(MySettings.mysettings.value("checkBox_4.isChecked")).lower():
                pass
            else:
                if MySettings.mysettings.value("comboBox.text")=='IPsec/L2TP':
                    os.system('sudo route del default dev ppp0')
                    os.system('sudo echo "d myvpn" > /var/run/xl2tpd/l2tp-control && sudo ipsec down myvpn')
                    os.system(f"sudo systemctl disable vpnscript.service")                    
                elif MySettings.mysettings.value("comboBox.text")=='OpenVPN':
                    pass
                self.signalDownVPN.emit()
                self.ui.label_2.setStyleSheet("color: black")                     
                self.ui.label_2.setText("VPN отключен")
                MySettings.mysettings.setValue("checkBox_4.isChecked", self.ui.checkBox_4.isChecked())             

        # Connection RDP/Web  
        if self.ui.comboBox_2.currentText()=='Web' and (self.ui.comboBox_2.currentText()!=MySettings.mysettings.value('comboBox_2.text') or self.ui.lineEdit_3.text() != self.mysettings.value('lineEdit_3.text')):       
            if self.ui.lineEdit_3.text() != '':     
                nameUser=os.getlogin()            
                with open("/home/" + nameUser + "/runrdp", 'w+') as file:    
                    line=self.ui.lineEdit_3.text()                    
                    if ('http://' in line) or ('https://' in line):            
                        file.write(f'sudo -u {nameUser} chromium {self.ui.lineEdit_3.text()}') 
                    else:
                        file.write(f'sudo -u {nameUser} chromium https://{self.ui.lineEdit_3.text()}')

                MySettings.mysettings.setValue("comboBox_2.text", self.ui.comboBox_2.currentText())
                MySettings.mysettings.setValue("lineEdit_3.text", self.ui.lineEdit_3.text())

                self.ui.labelSettRDP.setStyleSheet("color: black")                    
                self.ui.labelSettRDP.setText("Настройки сохранены")
            elif (self.ui.comboBox_2.currentText()=='Web' and self.ui.lineEdit_3.text() == MySettings.mysettings.value('lineEdit_3.text')):
                pass
            elif (self.ui.comboBox_2.currentText()=='Web' and self.ui.lineEdit_3.text() == ''):
                self.ui.labelSettRDP.setStyleSheet("color: red")
                self.ui.labelSettRDP.setText("Ввод недопустимых значений")
        
        if self.ui.comboBox_2.currentText()=='RDP' or self.ui.comboBox_2.currentText()!=MySettings.mysettings.value('comboBox_2.text') or self.ui.editAdrRDP.text()!=self.mysettings.value('editAdrRDP.text'):
            flag = True            
            if (self.ui.comboBox_2.currentText()=='RDP' and self.ui.editAdrRDP.text() != ""):                
                
                if self.ui.checkBox_5.isChecked():   
                    flagUSB = True
                else:
                    flagUSB = False

                # Используем freerdp
                nameUser=os.getlogin()                            
                file=open("/home/" + nameUser + "/runrdp", 'w+')         
                    
                if (self.ui.editLog2.text().rstrip('\n')=="" and self.ui.editPass2.text().rstrip('\n')==""):
                    if flagUSB:
                        os.system('sudo mkdir /media/root && sudo chmod 777 /media/root')
                        os.system('sudo udiskie -a &')
                        file.write("xfreerdp /v:"+self.ui.editAdrRDP.text().rstrip('\n')+" /drive:sda1,/media/root")
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                    else:
                        os.system('sudo rmdir /media/root')
                        #os.system('sudo udiskie -a &')
                        file.write("xfreerdp /v:"+self.ui.editAdrRDP.text().rstrip('\n'))
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone\n")
                if (self.ui.editLog2.text().rstrip('\n')!="" and self.ui.editPass2.text().rstrip('\n')==""):
                    if flagUSB:
                        os.system('sudo mkdir /media/root && sudo chmod 777 /media/root')
                        #os.system('sudo mkdir /media/sda1')
                        os.system('sudo udiskie -a &')
                        file.write("xfreerdp /v:"+self.ui.editAdrRDP.text().rstrip('\n')+" /u:"+self.ui.editLog2.text().rstrip(' ').rstrip('\n').strip('\n')) 
                        file.write(" /drive:sda1,/media/root /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                    else:
                        os.system('sudo rmdir /media/root')
                        #os.system('sudo udiskie -a &')
                        file.write("xfreerdp /v:"+self.ui.editAdrRDP.text().rstrip('\n')+" /u:"+self.ui.editLog2.text().rstrip(' ').rstrip('\n').strip('\n'))
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                if (self.ui.editLog2.text().rstrip('\n')!="" and self.ui.editPass2.text().rstrip('\n')!=""):
                    if flagUSB:
                        os.system('sudo mkdir /media/root && sudo chmod 777 /media/root')
                        #os.system('sudo mkdir /media/sda1')
                        os.system('sudo udiskie -a &')
                        file.write("xfreerdp /v:"+self.ui.editAdrRDP.text().rstrip('\n')+" /u:"+self.ui.editLog2.text().rstrip(' ').rstrip('\n').strip('\n'))
                        file.write(" /p:"+self.ui.editPass2.text().rstrip(' ').rstrip('\n').strip('\n')+" /drive:sda1,/media/root")
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                    else:
                        os.system('sudo rmdir /media/root')
                        file.write("xfreerdp /v:"+self.ui.editAdrRDP.text().rstrip('\n')+" /u:"+self.ui.editLog2.text().rstrip(' ').rstrip('\n').strip('\n'))
                        file.write(" /p:"+self.ui.editPass2.text().rstrip(' ').rstrip('\n').strip('\n')+" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                file.close()

                os.system(f"chmod 755 /home/{nameUser}/runrdp")
                os.system(f"chown {nameUser}:{nameUser} /home/{nameUser}/runrdp")
                self.ip_rdp = self.ui.editAdrRDP.text().rstrip('\n')
                self.login_rdp = self.ui.editLog2.text().rstrip('\n')                
                
                # Сохранение настроек RDP
                MySettings.mysettings.setValue("comboBox_2.text", self.ui.comboBox_2.currentText())                     
                MySettings.mysettings.setValue("editAdrRDP.text", self.ui.editAdrRDP.text()) 
                MySettings.mysettings.setValue("editLog2.text", self.ui.editLog2.text()) 
                MySettings.mysettings.setValue("editPass2.text", self.ui.editPass2.text()) 
                MySettings.mysettings.setValue("checkBox_5.isChecked", self.ui.checkBox_5.isChecked()) 
                                
                self.ui.labelSettRDP.setStyleSheet("color: black")                    
                self.ui.labelSettRDP.setText("Настройки сохранены")      
            elif (self.ui.comboBox_2.currentText()=='RDP' and self.ui.editAdrRDP.text() == ""):
                self.ui.labelSettRDP.setStyleSheet("color: red")
                self.ui.labelSettRDP.setText("Ввод недопустимых значений")
            

    def buttonReboot_clicked(self):           
        os.system("reboot")
        

    def buttonTurnOff_clicked(self):
        os.system("shutdown -h now")     


    def showSettingsEthernet(self):
        if not os.path.isfile('/etc/dhcpcd.conf'):
            os.system('sudo cp dhcpcd.conf /etc/')

        flag = False
        flag1 = False 
        flag2 = False
        flag3 = False 
        flag4 = False
        
        with open('/etc/dhcpcd.conf', 'r') as file:
            lines = file.readlines()
            for i,line in enumerate(lines):        
                if (flag and flag1 and flag2 and flag3 and flag4):
                    pass
                else:           
                    if ("nodhcp" in line):         
                        flag = True            
                    if ("static ip_address=" in line) and flag == True:                
                        s = lines[i]                   
                        s = s.replace("static ip_address=", "")    
                        self.ui.editIP.setText(str(s.rstrip('\n')))
                        flag1 = True 
                    if ("static netmask=" in line) and flag == True:                   
                        s = lines[i]     
                        s = s.replace("static netmask=", "")   
                        self.ui.editNetmask.setText(s.rstrip('\n'))
                        flag2 = True 
                    if ("static routers=" in line) and flag == True:                              
                        s = lines[i]                 
                        s = s.replace("static routers=", "") 
                        self.ui.editDHCP.setText(s.rstrip('\n'))
                        flag3 = True 
                    if ("static domain_name_servers=" in line) and flag == True:                  
                        s = lines[i]      
                        s = s.replace("static domain_name_servers=", "")     
                        self.ui.editDNS.setText(s.rstrip('\n'))  
                        flag4 = True                     

        if (flag == False):
            self.ui.checkBox.setChecked(True)
            self.ui.editIP.setDisabled(True)
            self.ui.editNetmask.setDisabled(True)
            self.ui.editDHCP.setDisabled(True)        
            self.ui.editDNS.setDisabled(True)   
            self.ui.labelIP.setDisabled(True)        
            self.ui.labelNetmask.setDisabled(True)        
            self.ui.labelDHCP.setDisabled(True)       
            self.ui.labelDNS.setDisabled(True)  


    def showSettingsEthernet_interfaces(self):        
        flag = False       
        
        with open('/etc/network/interfaces', 'r') as file:
            lines = file.readlines()
            for i,line in enumerate(lines):                         
                if ("iface eth0 inet static" in line):         
                    flag = True            
                if ("address " in line) and flag == True:                
                    s = lines[i]                   
                    s = s.replace("address ", "")    
                    self.ui.editIP.setText(str(s.rstrip('\n')))                    
                if ("netmask " in line) and flag == True:                   
                    s = lines[i]     
                    s = s.replace("netmask ", "")   
                    self.ui.editNetmask.setText(s.rstrip('\n'))                    
                if ("gateway " in line) and flag == True:                              
                    s = lines[i]                 
                    s = s.replace("gateway ", "") 
                    self.ui.editDHCP.setText(s.rstrip('\n'))                    
                if ("dns-nameservers " in line) and flag == True:                  
                    s = lines[i]      
                    s = s.replace("dns-nameservers ", "")     
                    self.ui.editDNS.setText(s.rstrip('\n'))              

        if (flag == False):
            self.ui.checkBox.setChecked(True)
            self.ui.editIP.setDisabled(True)
            self.ui.editNetmask.setDisabled(True)
            self.ui.editDHCP.setDisabled(True)        
            self.ui.editDNS.setDisabled(True)   
            self.ui.labelIP.setDisabled(True)        
            self.ui.labelNetmask.setDisabled(True)        
            self.ui.labelDHCP.setDisabled(True)       
            self.ui.labelDNS.setDisabled(True)

    def readListWiFi(self): # Чтение списка
        nameUser=os.getlogin()
        os.system("sudo chmod 755 /home/" + nameUser + "/list_wifi.py")
        os.system("sudo chown " + nameUser + ":" + nameUser + " /home/" + nameUser + "/list_wifi.py")        
        with open("/home/" + nameUser + "/list_wifi.py", 'r') as file:
            lines = file.readlines()       

        self.ui.editNetSel.clear()
        self.ui.editNetSel.addItems([" "])
        
        for line in lines:                   
            if ("ESSID:" in line):         
                tmp=line
                tmp = tmp.replace("ESSID:", "")
                tmp = tmp.rstrip('\n')                     
                tmp = tmp.rstrip('\"')                  
                tmp = tmp.strip(' ')
                tmp = tmp.strip('\"')                 
                self.ui.editNetSel.addItems([tmp])   
                

    def showSettings(self):                  
        if MySettings.mysettings.value("checkBox.isChecked")=='true':  
            self.ui.checkBox.setChecked(True)            
        self.checkBox_clicked() 
        if MySettings.mysettings.value("checkBox_3.isChecked")=='true':  
            self.ui.checkBox_3.setChecked(True)
        elif MySettings.mysettings.value("checkBox_3.isChecked")=='false':  
            self.ui.checkBox_3.setChecked(False)
        self.checkBox_3_clicked()


    def showSettingsVPN(self):       
        if MySettings.mysettings.value("checkBox_4.isChecked")=='true':
            self.ui.checkBox_4.setChecked(True)                     
        else:
            self.ui.checkBox_4.setChecked(False)  
            self.ui.comboBox.setDisabled(True) 
            self.ui.comboBox.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.lineEdit.setDisabled(False) 
            self.ui.lineEdit.setStyleSheet("background-color: red") 
            self.ui.label_4.setDisabled(True) 
            self.ui.lineEdit_2.setDisabled(True) 
            self.ui.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.label_5.setDisabled(True)                           
            self.ui.editLog3.setDisabled(True)   
            self.ui.editLog3.setStyleSheet("background-color: rgb(240, 240, 240)")          
            self.ui.labelNetSel_2.setDisabled(True)            
            self.ui.editPass_2.setDisabled(True)
            self.ui.editPass_2.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelPass_2.setDisabled(True)
            self.ui.pushButton_2.setDisabled(True)    
            self.ui.label.setDisabled(True)                                

        self.ui.comboBox.setCurrentText(MySettings.mysettings.value("comboBox.text"))          

        if self.ui.comboBox.currentText()=='IPsec/L2TP' and MySettings.mysettings.value("checkBox_4.isChecked")=='true':                    
            self.ui.lineEdit.setText(MySettings.mysettings.value("lineEdit.text.l2tp"))
            self.ui.lineEdit_2.setText(MySettings.mysettings.value("lineEdit_2.text.l2tp"))
            self.ui.editLog3.setText(MySettings.mysettings.value("editLog3.text.l2tp"))
            self.ui.editPass_2.setText(MySettings.mysettings.value("editPass_2.text.l2tp"))
            self.ui.pushButton_2.setDisabled(True)    
            self.ui.pushButton_2.setStyleSheet("background-color: rgb(240, 240, 240)") 
            self.ui.label.setDisabled(True)            
        elif self.ui.comboBox.currentText()=='OpenVPN' and MySettings.mysettings.value("checkBox_4.isChecked")=='true':    
            self.ui.lineEdit.setText('')
            self.ui.lineEdit_2.setText('')        
            self.ui.editLog3.setText(MySettings.mysettings.value("editLog3.text.openvpn"))
            self.ui.editPass_2.setText(MySettings.mysettings.value("editPass_2.text.openvpn"))   
                        

    def showSettingsRDP(self):    
        self.ui.comboBox_2.setCurrentText(MySettings.mysettings.value("comboBox_2.text"))

        if self.ui.comboBox_2.currentText()=='Web':             
            self.ui.lineEdit_3.setDisabled(False)     
            self.ui.lineEdit_3.setStyleSheet("background-color: white")   
            self.ui.lineEdit_3.setText(MySettings.mysettings.value("lineEdit_3.text"))
            self.ui.editAdrRDP.setDisabled(True)
            self.ui.editAdrRDP.setText('')   
            self.ui.editAdrRDP.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelAdrRDP.setDisabled(True)         
            self.ui.editLog2.setDisabled(True)
            self.ui.editLog2.setText('')
            self.ui.editLog2.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelLog2.setDisabled(True) 
            self.ui.editPass2.setDisabled(True)
            self.ui.editPass2.setText('')
            self.ui.editPass2.setStyleSheet("background-color: rgb(240, 240, 240)")
            self.ui.labelPass2.setDisabled(True)            
            self.ui.checkBox_5.setChecked(False)
            self.ui.checkBox_5.setDisabled(True)         

        elif self.ui.comboBox_2.currentText()=='RDP':
            self.ui.lineEdit_3.setText('') 
            self.ui.lineEdit_3.setDisabled(True)   
            self.ui.label_6.setDisabled(True)
            self.ui.editAdrRDP.setText(MySettings.mysettings.value("editAdrRDP.text"))                         
            self.ui.editAdrRDP.setDisabled(False)  
            self.ui.labelAdrRDP.setDisabled(False)
            self.ui.editLog2.setText(MySettings.mysettings.value("editLog2.text"))  
            self.ui.editLog2.setDisabled(False)  
            self.ui.labelLog2.setDisabled(False)      
            self.ui.editPass2.setText(MySettings.mysettings.value("editPass2.text"))  
            self.ui.editPass2.setDisabled(False) 
            self.ui.labelPass2.setDisabled(False)
            if MySettings.mysettings.value("checkBox_5.isChecked")=='true':
                self.ui.checkBox_5.setChecked(True)
            else:
                self.ui.checkBox_5.setChecked(False)            
            self.ui.checkBox_5.setDisabled(False)    