# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormSettingsD.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(665, 732)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 20, 631, 691))
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(30, 610, 561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.labelSettings = QtWidgets.QLabel(self.widget)
        self.labelSettings.setGeometry(QtCore.QRect(260, 10, 101, 17))
        self.labelSettings.setObjectName("labelSettings")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 630, 567, 27))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.buttonTurnOff = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonTurnOff.setObjectName("buttonTurnOff")
        self.horizontalLayout.addWidget(self.buttonTurnOff)
        self.buttonTakeSett = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonTakeSett.setObjectName("buttonTakeSett")
        self.horizontalLayout.addWidget(self.buttonTakeSett)
        self.buttonReboot = QtWidgets.QPushButton(self.layoutWidget)
        self.buttonReboot.setObjectName("buttonReboot")
        self.horizontalLayout.addWidget(self.buttonReboot)
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 270, 261, 112))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.labelNetSel = QtWidgets.QLabel(self.layoutWidget1)
        self.labelNetSel.setObjectName("labelNetSel")
        self.gridLayout.addWidget(self.labelNetSel, 1, 3, 1, 2)
        self.editPass = QtWidgets.QLineEdit(self.layoutWidget1)
        self.editPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPass.setObjectName("editPass")
        self.gridLayout.addWidget(self.editPass, 2, 0, 1, 3)
        self.labelPass = QtWidgets.QLabel(self.layoutWidget1)
        self.labelPass.setObjectName("labelPass")
        self.gridLayout.addWidget(self.labelPass, 2, 3, 1, 2)
        self.labelSettWiFi = QtWidgets.QLabel(self.layoutWidget1)
        self.labelSettWiFi.setText("")
        self.labelSettWiFi.setObjectName("labelSettWiFi")
        self.gridLayout.addWidget(self.labelSettWiFi, 3, 0, 1, 5)
        self.editNetSel = QtWidgets.QComboBox(self.layoutWidget1)
        self.editNetSel.setObjectName("editNetSel")
        self.gridLayout.addWidget(self.editNetSel, 1, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 2)
        self.layoutWidget2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 51, 244, 127))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.labelAdm = QtWidgets.QLabel(self.layoutWidget2)
        self.labelAdm.setObjectName("labelAdm")
        self.gridLayout_5.addWidget(self.labelAdm, 0, 0, 1, 2)
        self.labelNewPass = QtWidgets.QLabel(self.layoutWidget2)
        self.labelNewPass.setObjectName("labelNewPass")
        self.gridLayout_5.addWidget(self.labelNewPass, 1, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 3, 0, 1, 1)
        self.buttonReset = QtWidgets.QPushButton(self.layoutWidget2)
        self.buttonReset.setObjectName("buttonReset")
        self.gridLayout_5.addWidget(self.buttonReset, 3, 1, 1, 1)
        self.buttonTake = QtWidgets.QPushButton(self.layoutWidget2)
        self.buttonTake.setObjectName("buttonTake")
        self.gridLayout_5.addWidget(self.buttonTake, 3, 2, 1, 1)
        self.labelNotify = QtWidgets.QLabel(self.layoutWidget2)
        self.labelNotify.setText("")
        self.labelNotify.setObjectName("labelNotify")
        self.gridLayout_5.addWidget(self.labelNotify, 4, 0, 1, 3)
        self.editNewPass = QtWidgets.QLineEdit(self.layoutWidget2)
        self.editNewPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editNewPass.setObjectName("editNewPass")
        self.gridLayout_5.addWidget(self.editNewPass, 2, 0, 1, 3)
        self.layoutWidget3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget3.setGeometry(QtCore.QRect(33, 400, 262, 205))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_4.addWidget(self.checkBox_4, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_4.addWidget(self.lineEdit_2, 2, 0, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 3, 1, 1)
        self.editLog3 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.editLog3.setObjectName("editLog3")
        self.gridLayout_4.addWidget(self.editLog3, 3, 0, 1, 3)
        self.labelNetSel_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.labelNetSel_2.setObjectName("labelNetSel_2")
        self.gridLayout_4.addWidget(self.labelNetSel_2, 3, 3, 1, 1)
        self.editPass_2 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.editPass_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.editPass_2.setObjectName("editPass_2")
        self.gridLayout_4.addWidget(self.editPass_2, 4, 0, 1, 3)
        self.labelPass_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.labelPass_2.setObjectName("labelPass_2")
        self.gridLayout_4.addWidget(self.labelPass_2, 4, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 5, 0, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 5, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 5, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 6, 0, 1, 4)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 0, 1, 1, 2)
        self.layoutWidget4 = QtWidgets.QWidget(self.widget)
        self.layoutWidget4.setGeometry(QtCore.QRect(340, 260, 263, 211))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelLog2 = QtWidgets.QLabel(self.layoutWidget4)
        self.labelLog2.setObjectName("labelLog2")
        self.gridLayout_2.addWidget(self.labelLog2, 5, 2, 1, 1)
        self.labelPass2 = QtWidgets.QLabel(self.layoutWidget4)
        self.labelPass2.setObjectName("labelPass2")
        self.gridLayout_2.addWidget(self.labelPass2, 6, 2, 1, 1)
        self.editPass2 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.editPass2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.editPass2.setObjectName("editPass2")
        self.gridLayout_2.addWidget(self.editPass2, 6, 0, 1, 2)
        self.labelConnection = QtWidgets.QLabel(self.layoutWidget4)
        self.labelConnection.setObjectName("labelConnection")
        self.gridLayout_2.addWidget(self.labelConnection, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 0, 1, 2)
        self.editAdrRDP = QtWidgets.QLineEdit(self.layoutWidget4)
        self.editAdrRDP.setObjectName("editAdrRDP")
        self.gridLayout_2.addWidget(self.editAdrRDP, 4, 0, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.labelAdrRDP = QtWidgets.QLabel(self.layoutWidget4)
        self.labelAdrRDP.setObjectName("labelAdrRDP")
        self.gridLayout_2.addWidget(self.labelAdrRDP, 4, 2, 1, 1)
        self.editLog2 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.editLog2.setObjectName("editLog2")
        self.gridLayout_2.addWidget(self.editLog2, 5, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget4)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_2.addWidget(self.checkBox_5, 7, 0, 1, 3)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.labelSettRDP = QtWidgets.QLabel(self.layoutWidget4)
        self.labelSettRDP.setText("")
        self.labelSettRDP.setObjectName("labelSettRDP")
        self.gridLayout_6.addWidget(self.labelSettRDP, 1, 0, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.widget)
        self.layoutWidget5.setGeometry(QtCore.QRect(30, 51, 261, 201))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelDNS = QtWidgets.QLabel(self.layoutWidget5)
        self.labelDNS.setObjectName("labelDNS")
        self.gridLayout_3.addWidget(self.labelDNS, 5, 4, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 0, 2, 1, 2)
        self.editNetmask = QtWidgets.QLineEdit(self.layoutWidget5)
        self.editNetmask.setObjectName("editNetmask")
        self.gridLayout_3.addWidget(self.editNetmask, 3, 0, 1, 4)
        self.editDHCP = QtWidgets.QLineEdit(self.layoutWidget5)
        self.editDHCP.setObjectName("editDHCP")
        self.gridLayout_3.addWidget(self.editDHCP, 4, 0, 1, 4)
        self.labelSettEth = QtWidgets.QLabel(self.layoutWidget5)
        self.labelSettEth.setLineWidth(1)
        self.labelSettEth.setText("")
        self.labelSettEth.setObjectName("labelSettEth")
        self.gridLayout_3.addWidget(self.labelSettEth, 6, 0, 1, 5)
        self.labelDHCP = QtWidgets.QLabel(self.layoutWidget5)
        self.labelDHCP.setObjectName("labelDHCP")
        self.gridLayout_3.addWidget(self.labelDHCP, 4, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(38, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 1, 1, 1)
        self.labelNetmask = QtWidgets.QLabel(self.layoutWidget5)
        self.labelNetmask.setObjectName("labelNetmask")
        self.gridLayout_3.addWidget(self.labelNetmask, 3, 4, 1, 1)
        self.editIP = QtWidgets.QLineEdit(self.layoutWidget5)
        self.editIP.setObjectName("editIP")
        self.gridLayout_3.addWidget(self.editIP, 2, 0, 1, 4)
        self.labelEth = QtWidgets.QLabel(self.layoutWidget5)
        self.labelEth.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelEth.setObjectName("labelEth")
        self.gridLayout_3.addWidget(self.labelEth, 0, 0, 1, 1)
        self.editDNS = QtWidgets.QLineEdit(self.layoutWidget5)
        self.editDNS.setObjectName("editDNS")
        self.gridLayout_3.addWidget(self.editDNS, 5, 0, 1, 4)
        self.labelIP = QtWidgets.QLabel(self.layoutWidget5)
        self.labelIP.setObjectName("labelIP")
        self.gridLayout_3.addWidget(self.labelIP, 2, 4, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget5)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.labelSettings.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600;\">Настройки</span></p></body></html>"))
        self.pushButton_3.setText(_translate("Form", "Информация об устройстве"))
        self.buttonTurnOff.setText(_translate("Form", "Выключить"))
        self.buttonTakeSett.setText(_translate("Form", "Принять настройки"))
        self.buttonReboot.setText(_translate("Form", "Перезагрузка"))
        self.checkBox_2.setText(_translate("Form", "Wi-Fi:"))
        self.labelNetSel.setText(_translate("Form", "Выбор сети"))
        self.labelPass.setText(_translate("Form", "Пароль"))
        self.label_3.setText(_translate("Form", "Обновить"))
        self.labelAdm.setText(_translate("Form", "Администрирование :"))
        self.labelNewPass.setText(_translate("Form", "Новый пароль администратора :"))
        self.buttonReset.setText(_translate("Form", "Сброс пароля"))
        self.buttonTake.setText(_translate("Form", "Принять"))
        self.checkBox_4.setText(_translate("Form", "VPN:"))
        self.label_4.setText(_translate("Form", "IP сервера"))
        self.label_5.setText(_translate("Form", "IPsec PSK"))
        self.labelNetSel_2.setText(_translate("Form", "Логин"))
        self.labelPass_2.setText(_translate("Form", "Пароль"))
        self.label.setText(_translate("Form", "Сертификат"))
        self.comboBox.setItemText(0, _translate("Form", "IPsec/L2TP"))
        self.labelLog2.setText(_translate("Form", "Логин"))
        self.labelPass2.setText(_translate("Form", "Пароль"))
        self.labelConnection.setText(_translate("Form", "Подключение :"))
        self.comboBox_2.setItemText(0, _translate("Form", "RDP"))
        self.comboBox_2.setItemText(1, _translate("Form", "Web"))
        self.labelAdrRDP.setText(_translate("Form", "Адрес RDP"))
        self.label_6.setText(_translate("Form", "Адрес Web"))
        self.checkBox_5.setText(_translate("Form", "Проброс USB по RDP"))
        self.labelDNS.setText(_translate("Form", "DNS"))
        self.checkBox_3.setText(_translate("Form", "VLAN"))
        self.labelDHCP.setText(_translate("Form", "Gateway"))
        self.labelNetmask.setText(_translate("Form", "Netmask"))
        self.labelEth.setText(_translate("Form", "<html><head/><body><p>Ethernet :</p></body></html>"))
        self.labelIP.setText(_translate("Form", "IP"))
        self.checkBox.setText(_translate("Form", "Получение IP автоматически"))
