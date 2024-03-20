from PyQt5 import QtCore
#from flask import Flask, render_template, request, redirect, url_for #, stream_template, Response
import webbrowser
from os import system, getlogin

class MyThread_wsgi(QtCore.QThread):      
    
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)         

    def run(self):
        system("uwsgi --http :5000 --module app_flask:app")