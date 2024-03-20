#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for #, stream_template, Response
import json, jsonify
from contextlib import contextmanager
import webbrowser
from Settings import *
from os import system, getlogin
from FormSettings import *

app = Flask(__name__, static_folder="static")
   
@app.route('/') # , methods=['GET','POST']
def logo():           
    return render_template('passwd.html')    # , utc_dt=datetime.datetime.utcnow()

    
@app.route('/settings')
def settings():
    return render_template('settings.html') # , posts=posts'''


@app.route('/off', methods=['GET','POST'])
def off():
    if request.method == 'POST':
        os.system("shutdown -h now")    

@app.route('/reboot', methods=['GET','POST'])
def reboot():
    if request.method == 'POST':
        os.system("sudo reboot")
    #FormSettings.buttonReboot_clicked()

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':  
        
        out_str = save_sattings(vlan_check=request.form.get('vlan_check'),vlan=request.form.get('vlan'), 
            ip_check=request.form.get('ip_check'), ip=request.form.get('ip'), netmask=request.form.get('netmask'), 
            gateway=request.form.get('gateway'), dns=request.form.get('dns'),
            pass_adm=request.form.get('pass_adm'),             
            vpn_check=request.form.get('vpn_check'), select_vpn=request.form.get('select_vpn'), 
            ip_vpn=request.form.get('ip_vpn'), ip_sec=request.form.get('ip_sec'),
            login_vpn=request.form.get('login_vpn'), pass_vpn=request.form.get('pass_vpn'),
            #sert=request.form.get('sert'),
            select_rdp_web=request.form.get('select_rdp_web'), adr_web=request.form.get('adr_web'),
            adr_rdp=request.form.get('adr_rdp'), login_rdp=request.form.get('login_rdp'), passwd_rdp=request.form.get('passwd_rdp'), 
            usb_check=request.form.get('usb_check')
        )                
        #return (''), 204
        return render_template('settings.html', s1=out_str[0], s2=out_str[1], s3=out_str[2], s4=out_str[3])
    else:
        return (''), 205
    

@app.route('/validate', methods=['GET','POST'])
def validate():
    if request.method == 'POST':
        passwd=request.form.get('passwd') 
        nameUser=os.getlogin()         
        if nameUser=='rock':
            with open(f'/home/{nameUser}/pass.txt', 'r+') as file: 
                passwd_file = file.readline()          
        else:
            with open('pass.txt', 'r+') as file: 
                passwd_file = file.readline()  
                
        if passwd == passwd_file:
            return render_template('settings.html')
        else:            
            return render_template('passwd.html', s='Неверный пароль')
     

if __name__ == "__main__":       
    host_name = os.system("hostname")
    webbrowser.open_new(f'http://{host_name}:5000/')
    app.run() # host='127.0.0.1', port=80 # debug=True