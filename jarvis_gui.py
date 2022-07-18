# importing neccessary python libraries used for system.
from jarvisui import  Ui_Voice_assistant
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore  import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer,QTime, QDate
from PyQt5.uic import loadUiType
import Main
from bs4 import BeautifulSoup
import sys
import requests
import webbrowser
import os

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        Main.face_lock()    # on clicking start button ..system will start from face lock module and further task execution.

startexe=MainThread()  # exe system will start from class.

class Gui_start(QMainWindow):   # class to start gui or user interface on starting.
    def __init__(self):
        super().__init__()                                      
        self.gui=Ui_Voice_assistant()                    # defines various gif,push button,text browser functions.
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)
        self.gui.whatsappweb_button.clicked.connect(self.whatsapp_app)
        self.gui.mail_pushbutton.clicked.connect(self.mail_app)
        self.gui.spotify_button.clicked.connect(self.spotify_app)
        self.gui.chrome.clicked.connect(self.chrome_ap)
        self.gui.Youtube.clicked.connect(self.yt_app)
 
    def chrome_ap(self):            # function of opening chrome
        webbrowser.open("https://www.google.com/")
    
    def yt_app(self):                # function of opening youtube
        webbrowser.open("https://www.youtube.com/")
    
    def mail_app(self):                # function of opening mail 
        webbrowser.open("www.gmail.com")
    
    def whatsapp_app(self):           # function of opening whatsapp web
        webbrowser.open("https://web.whatsapp.com/")
    
    def spotify_app(self):            # function of opening spotify
        webbrowser.open("https://open.spotify.com/")
    

    def startTask(self):                 # it will start all gif used in gui
        self.gui.label3=QtGui.QMovie("gui_jpg\initial.gif")
        self.gui.label_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4=QtGui.QMovie("gui_jpg/flo-motion_5sec.gif")
        self.gui.voice_label.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5=QtGui.QMovie("gui_jpg\moving_circle.gif")
        self.gui.circle_gif.setMovie(self.gui.label5)
        self.gui.label5.start()

        
        timer=QTimer(self)
        timer.timeout.connect(self.timedate)
        timer.start(999)
        startexe.start() #start button.
    
    def timedate(self):              # function to show time and date shown in gui
        ti_me=QTime.currentTime()
        time=ti_me.toString()
        d_ate=QDate.currentDate()
        date=d_ate.toString()
        label_time="Time :"+time  #string fromate for time
        label_date="Date :"+date   #string fromate for date

        ip_ad=requests.get('https://api.ipify.org').text
        url= 'https://get.geojs.io/v1/ip/geo/'+ip_ad+".json"    # revel user location.
        r=requests.get(url)
        r=r.json()
        city=r['city']
        label_temp="Location :"+ city
      
        #fill text browser according to their label.
        self.gui.textBrowser.setText(label_time)
        self.gui.textBrowser_2.setText(label_date)
        self.gui.textBrowser_3.setText(label_temp)
        
    

guiapp=QApplication(sys.argv)
jarvis_gui=Gui_start()   #system will start from this.
jarvis_gui.show()
sys.exit(guiapp.exec_())   # system will close from this.




        

    

