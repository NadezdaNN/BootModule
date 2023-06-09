import os
from PyQt5 import QtCore

class MyThreadNet(QtCore.QObject):   
    
    signalSetCursor = QtCore.pyqtSignal()  
    signalSetTextEth0 = QtCore.pyqtSignal() 
    signalSetTextWiFi = QtCore.pyqtSignal() 
    signalPushButton = QtCore.pyqtSignal()
    signalSetTextVPN = QtCore.pyqtSignal()
    
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)  
        self.nameUser=os.getlogin()             
        self.flag_listWiFi = False #True
        self.flag_upWiFi = False
        self.flag_upEth = False
        self.flag_upVPN = False
        self.flag_upVPN2 = False
        self.flag_upOpenVPN = False
        self.flag_downVPN = False

        
    def run(self):
        while self.flag_listWiFi:                     
            os.system(f"sudo chmod 755 /home/{self.nameUser}/list_wifi.py")
            os.system(f"sudo chown {self.nameUser}:{self.nameUser} /home/{self.nameUser}/list_wifi.py")  
            os.system('sudo ifconfig wlan0 up')
            os.system(f"sudo iwlist scan | grep ESSID > /home/{self.nameUser}/list_wifi.py")            
            
            name = os.popen('uname -r').read().rstrip('\n')             
            if name =='5.15.0-56-generic': # for Ubuntu
                os.system("sudo cp file_wifi_Ubuntu.txt /home/" + self.nameUser + "/list_wifi.py")             

            self.signalPushButton.emit()
            self.flag_listWiFi = False    

        while self.flag_upWiFi:
            path_str='/etc/wpa_supplicant/wpa_supplicant.conf'
            os.system('sudo systemctl disable dhcpcd')
            os.system('sudo systemctl enable networking')            
            os.system('sudo ifconfig wlan0 up')                   
            os.system('sudo iwconfig wlan0 essid ssid')                   
            os.system('sudo wpa_supplicant -B -Dwext -iwlan0 -c' + path_str) #Запускаем утилиту wpa_supplicant на установку соединения   
            os.system('sudo ifconfig eth0 down')            
            self.signalSetTextWiFi.emit()
            self.flag_upWiFi = False

        while self.flag_upEth:            
            os.system('sudo systemctl disable networking && sudo systemctl enable dhcpcd && sudo systemctl restart networking.service')            
            self.signalSetTextEth0.emit()
            self.flag_upEth = False  

        while self.flag_upVPN:
            # IPsec/L2TP   
            os.system('sudo chmod 600 /etc/ipsec.secrets')
            os.system('sudo chmod 600 /etc/ppp/options.l2tpd.client')            
            os.system('sudo ipsec restart && sudo service xl2tpd restart && sudo ipsec up myvpn && sudo chmod 777 /var/run/xl2tpd/l2tp-control && sudo echo "c myvpn" > /var/run/xl2tpd/l2tp-control')
            
            str_ip = os.popen("ip route | grep 'default via'").read().rstrip('\n')  
            str_tmp = str_ip.replace('default via ', "")
            j = str_tmp.index(' ') 
            str_ip = str(str_tmp[:j].rstrip('\n').replace(" ",""))
            ip_server_vpn=os.system('cat ip_server_vpn.txt')
            ip_rdp=os.system('cat ip_rdp.txt')            

            os.system(f"sudo route add {ip_server_vpn} gw {str_ip} && sudo route add {ip_rdp} gw {str_ip} && sudo route add default dev ppp0")
            
            self.signalSetTextVPN.emit()
            self.flag_upVPN = False  

        while self.flag_upVPN2:
            # IPsec/L2TP   
            os.system('sudo chmod 600 /etc/ipsec.secrets')
            os.system('sudo chmod 600 /etc/ppp/options.l2tpd.client')    
            #os.system('sudo chmod 777 /var/run/xl2tpd/l2tp-control')
            os.system('sudo ipsec restart && sudo service xl2tpd restart && sudo ipsec up myvpn && sudo chmod 777 /var/run/xl2tpd/l2tp-control && sudo echo "c myvpn" > /var/run/xl2tpd/l2tp-control')
            
            str_ip = os.popen("ip route | grep 'default via'").read().rstrip('\n')  
            str_tmp = str_ip.replace('default via ', "")

            try:
                j = str_tmp.index(' ') 
                str_ip = str(str_tmp[:j].rstrip('\n').replace(" ",""))
                ip_server_vpn=os.system('cat ip_server_vpn.txt')
                ip_rdp=os.system('cat ip_rdp.txt')
                os.system(f"sudo route add {ip_server_vpn} gw {str_ip} && sudo route add {ip_rdp} gw {str_ip} && sudo route add default dev ppp0")
            except:
                pass  
            finally:
                self.flag_upVPN2 = False 

        while self.flag_downVPN:            
            os.system('sudo chmod 777 /var/run/xl2tpd/l2tp-control && sudo echo "d myvpn" > /var/run/xl2tpd/l2tp-control && sudo ipsec down myvpn')            
            #os.system(f"sudo systemctl disable vpnscript.service")
            self.flag_downVPN = False 

        while self.flag_upOpenVPN:
            #OpenVPN
            #os.system('sudo /etc/init.d/openvpn start')
            #os.system("sudo openvpn /etc/openvpn/client.conf") 
            #os.system('echo "TEST" | sudo systemd-tty-ask-password-agent')
            #os.system('echo "Aa12345678" | sudo systemd-tty-ask-password-agent')
            os.system('sudo service openvpn start')
            os.system('sudo openvpn --config /etc/openvpn/client.conf --daemon')    
            self.signalSetTextVPN.emit()
            self.flag_upOpenVPN = False              

        self.signalSetCursor.emit()


    def listWiFi(self):
        self.flag_listWiFi = True           
        self.run()


    def upWiFi(self):
        self.flag_upWiFi = True          
        self.run()


    def upEth(self):
        self.flag_upEth = True            
        self.run()


    def upVPN(self):
        self.flag_upVPN = True            
        self.run()
        

    def upVPN2(self):
        self.flag_upVPN2 = True            
        self.run()


    def downVPN(self):
        self.flag_downVPN = True          
        self.run()


    def upOpenVPN(self):
        self.flag_upOpenVPN = True          
        self.run()