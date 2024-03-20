import os
import MySettings
import FormLogo

def save_sattings(**kwargs):      
    '''kwargs.setdefault('vlan_check'), kwargs.setdefault('vlan'), 
        kwargs.setdefault('ip_check'), kwargs.setdefault('ip'), kwargs.setdefault('netmask'), 
        kwargs.setdefault('gateway'), kwargs.setdefault('dns'), 
        kwargs.setdefault('pass_adm'),
        kwargs.setdefault('vpn_check'), kwargs.setdefault('select_vpn'), kwargs.setdefault('ip_vpn'), 
        kwargs.setdefault('ip_sec'), kwargs.setdefault('login_vpn'), kwargs.setdefault('pass_vpn'),
        #kwargs.setdefault('sert'),
        kwargs.setdefault('select_rdp_web'), kwargs.setdefault('adr_web'), kwargs.setdefault('adr_rdp'), 
        kwargs.setdefault('login_rdp'), kwargs.setdefault('passwd_rdp'), kwargs.setdefault('usb_check')
    '''
    list_out=['', '', '', '']
    
    if kwargs.setdefault('ip_check')=='on': #динамический IP-адрес
        try:
            #os.write('sudo chown rock /etc/network/interfaces')
            #os.write('sudo chmode 777 /etc/network/interfaces')
            file = open('/etc/network/interfaces', 'w+')
        except: 
            #os.write('sudo chown rock /etc/network/interfaces')
            os.system("sudo touch /etc/network/interfaces")
            file = open('/etc/network/interfaces', 'w+')
                        
        file.write('auto lo\n')
        file.write('iface lo inet loopback\n')
        file.write('auto eth0\n')
        file.write('iface eth0 inet dhcp\n')

        if (kwargs.setdefault('vlan_check')=='on' and kwargs.setdefault('vlan')!=''): # VLAN
            file.write(f'auto eth0.{kwargs.setdefault("vlan")}\n')
            file.write(f'iface eth0.{kwargs.setdefault("vlan")} inet dhcp\n')     
            
        file.close()  
        '''print('147=', kwargs.setdefault('vlan'))
        MySettings.mysettings.setValue("checkBox.isChecked", (kwargs.setdefault('ip_check')=='on'))
        MySettings.mysettings.setValue("checkBox_3.isChecked", (kwargs.setdefault('vlan_check')=='on'))
        MySettings.mysettings.setValue("lineEdit_5.text", kwargs.setdefault('vlan'))
        print('148=', MySettings.mysettings.value("lineEdit_5.text"))''' 
        #global FormLogo.FormLogo.mysettings2        
        FormLogo.FormLogo.mysettings2.setValue("123", kwargs.setdefault('vlan'))        
        print('FormLogo.FormLogo.mysettings2.value("123")=', FormLogo.FormLogo.mysettings2.value("123"), kwargs.setdefault('vlan'))
        list_out[0]='Данные сохранены'       
                 
        
    else: #статический IP-адрес                       
        try:
            file=open("/etc/network/interfaces", 'w+')
        except: 
            os.system("sudo touch /etc/network/interfaces")
            file=open("/etc/network/interfaces", 'w+')
                                
        file.write('auto lo\n')
        file.write('iface lo inet loopback\n')
        file.write('auto eth0\n')
        file.write('iface eth0 inet static\n')
        file.write(f'address {kwargs.setdefault("ip")}\n')
        file.write(f'netmask {kwargs.setdefault("netmask")}\n')
        
        if kwargs.setdefault("gateway")!='' and (kwargs.setdefault("gateway") is not None):
            file.write(f'gateway {kwargs.setdefault("gateway")}\n')
        if kwargs.setdefault("dns")!='' and (kwargs.setdefault("dns") is not None):
            file.write(f'dns-nameservers {kwargs.setdefault("dns")}\n')                             
            
        if (kwargs.setdefault("vlan_check")=='on' and kwargs.setdefault('vlan')!=''): # VLAN                 
            file.write(f'auto eth0.{kwargs.setdefault("vlan")}\n')
            file.write(f'iface eth0.{kwargs.setdefault("vlan")} inet static\n')
            file.write(f'address {kwargs.setdefault("ip")}\n')
            file.write(f'netmask {kwargs.setdefault("netmask")}\n')
            if kwargs.setdefault("gateway")!='' and (kwargs.setdefault("gateway") is not None):                    
                file.write(f'gateway {kwargs.setdefault("gateway")}\n')
            if kwargs.setdefault("dns")!='' and (kwargs.setdefault("dns") is not None):                    
                file.write(f'dns-nameservers {kwargs.setdefault("dns")}\n')                                    
            
        file.close()       
        list_out[0]='Данные сохранены' 
        
        
    # Пароль администратора                     
    if (kwargs.setdefault('pass_adm')!='' and (kwargs.setdefault('pass_adm') is not None)):         
        with open("pass.txt", 'w+') as file_pass: 
            file_pass.write(kwargs.setdefault('pass_adm'))            
        list_out[1]='Данные сохранены'        
        

    # VPN
    if kwargs.setdefault("vpn_check")=='on':     
        
        if kwargs.setdefault("select_vpn")=='IPsec/L2TP':
            if (kwargs.setdefault("ip_vpn") is not None and kwargs.setdefault("ip_sec") is not None and 
                    kwargs.setdefault("login_vpn") is not None and kwargs.setdefault("pass_vpn") is not None):   
                
                with open('/etc/ipsec.conf', 'r+') as file: 
                    lines = file.readlines() 
                    flag=False
                    for i,line in enumerate(lines): 
                        if "conn myvpn" in line:
                            flag=True                                                 
                        if ("  right=" in line) and flag:                          
                            lines[i]=f'  right={kwargs.setdefault("ip_vpn")}\n'   
                file=open('/etc/ipsec.conf', 'w+')
                file.writelines(lines)  
                file.close()    

                os.system('sudo chmod 600 /etc/ipsec.secrets')
                with open('/etc/ipsec.secrets', 'w+') as file:                    
                    file.write(f': PSK "{kwargs.setdefault("ip_sec")}"')                          

                with open('/etc/xl2tpd/xl2tpd.conf', 'r+') as file: 
                    lines = file.readlines() 
                    flag=False
                    for i,line in enumerate(lines): 
                        if "[lac myvpn]" in line:
                            flag=True                                                 
                        if ("lns =" in line) and flag:                          
                            lines[i]=f'lns = {kwargs.setdefault("ip_vpn")}\n' 
                file=open('/etc/xl2tpd/xl2tpd.conf', 'w+')
                file.writelines(lines)  
                file.close()    

                with open('/etc/ppp/options.l2tpd.client', 'r+') as file: 
                    lines = file.readlines()                         
                    for i,line in enumerate(lines): 
                        if "name" in line:
                            lines[i]=f'name "{kwargs.setdefault("login_vpn")}"\n'                                               
                        if ("password" in line) and flag:                          
                            lines[i]=f'password "{kwargs.setdefault("pass_vpn")}"'  
                file=open('/etc/ppp/options.l2tpd.client', 'w+')
                file.writelines(lines)  
                file.close()         
                
                list_out[2]='Данные сохранены'                                   

                os.system(f'echo {kwargs.setdefault("ip_vpn")} > ip_server_vpn.txt')
                os.system(f'echo {kwargs.setdefault("rdp")} > ip_rdp.txt')                
            else:
                pass

            os.system('sudo route del default dev ppp0')
            os.system('sudo echo "d myvpn" > /var/run/xl2tpd/l2tp-control && sudo ipsec down myvpn')
            os.system(f"sudo systemctl disable vpnscript.service")  
                       
            #list_out[2]='Данные сохранены' 
        
    # Connection RDP/Web        
    if kwargs.setdefault('select_rdp_web')=='web':       
        if kwargs.setdefault('adr_web')!='': 
            nameUser=os.getlogin()            
            with open("/home/" + nameUser + "/runrdp", 'w+') as file:    
                line=kwargs.setdefault('adr_web')                                 
                if ('http://' in line) or ('https://' in line):            
                    file.write(f'sudo -u {nameUser} chromium {kwargs.setdefault("adr_web")} --kiosk') 
                else:
                    file.write(f'sudo -u {nameUser} chromium https://{kwargs.setdefault("adr_web")} --kiosk')   
            list_out[3]='Данные сохранены'     
        else:
            list_out[3]=''    
    
    elif kwargs.setdefault('select_rdp_web')=='rdp':        
        flag = True            
        if kwargs.setdefault('adr_rdp')!='':           
            if kwargs.setdefault('usb_check') == 'on':   
                flagUSB = True
            else:
                flagUSB = False

            # Используем freerdp            
            nameUser=os.getlogin()                
                
            if (kwargs.setdefault('login_rdp')=='') and (kwargs.setdefault('passwd_rdp')==''):
                if flagUSB:
                    os.system('sudo mkdir /media/root && sudo chmod 777 /media/root')
                    os.system('sudo udiskie -a &')
                    with open("/home/" + nameUser + "/runrdp", 'w+') as file: 
                        file.write("xfreerdp /v:"+kwargs.setdefault('adr_rdp')+" /drive:sda1,/media/root")
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                else:
                    os.system('sudo rmdir /media/root')
                    #os.system('sudo udiskie -a &')
                    with open("/home/" + nameUser + "/runrdp", 'w+') as file: 
                        file.write("xfreerdp /v:"+kwargs.setdefault('adr_rdp'))
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone\n")
                list_out[3]='Данные сохранены'  

            if (kwargs.setdefault('login_rdp')!='') and (kwargs.setdefault('passwd_rdp')==''):               
                if flagUSB:
                    os.system('sudo mkdir /media/root && sudo chmod 777 /media/root')
                    #os.system('sudo mkdir /media/sda1')
                    os.system('sudo udiskie -a &')
                    with open("/home/" + nameUser + "/runrdp", 'w+') as file: 
                        file.write("xfreerdp /v:"+kwargs.setdefault('adr_rdp')+" /u:"+kwargs.setdefault('login_rdp')) 
                        file.write(" /drive:sda1,/media/root /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                else:
                    os.system('sudo rmdir /media/root')
                    #os.system('sudo udiskie -a &')
                    with open("/home/" + nameUser + "/runrdp", 'w+') as file: 
                        file.write("xfreerdp /v:"+kwargs.setdefault('adr_rdp')+" /u:"+kwargs.setdefault('login_rdp'))
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                list_out[3]='Данные сохранены'  

            if (kwargs.setdefault('login_rdp')!='') and (kwargs.setdefault('passwd_rdp')!=''):
                if flagUSB:
                    os.system('sudo mkdir /media/root && sudo chmod 777 /media/root')
                    #os.system('sudo mkdir /media/sda1')
                    os.system('sudo udiskie -a &')
                    with open("/home/" + nameUser + "/runrdp", 'w+') as file: 
                        file.write("xfreerdp /v:"+kwargs.setdefault('adr_rdp')+" /u:"+kwargs.setdefault('login_rdp'))
                        file.write(" /p:"+kwargs.setdefault('passwd_rdp')+" /drive:sda1,/media/root")
                        file.write(" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                else:
                    os.system('sudo rmdir /media/root')
                    with open("/home/" + nameUser + "/runrdp", 'w+') as file: 
                        file.write("xfreerdp /v:"+kwargs.setdefault('adr_rdp')+" /u:"+kwargs.setdefault('login_rdp'))
                        file.write(" /p:"+kwargs.setdefault('passwd_rdp')+" /f /kbd-type:en-us /bpp:32 /sec:tls /network:auto /cert-ignore /sound /video /microphone \n")
                list_out[3]='Данные сохранены'  
                
            os.system(f"chmod 755 /home/{nameUser}/runrdp")
            os.system(f"chown {nameUser}:{nameUser} /home/{nameUser}/runrdp")
            #list_out[3]='Данные сохранены'        
    
    return list_out