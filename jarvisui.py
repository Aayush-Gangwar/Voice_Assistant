# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jarvis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# this file is py version of gui of system.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Voice_assistant(object):
    def setupUi(self, Voice_assistant):
# defines all gif,label,button,text , links used in user interface of system.
        Voice_assistant.setObjectName("Voice_assistant")
        Voice_assistant.resize(1929, 870)
        self.centralwidget = QtWidgets.QWidget(Voice_assistant)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-60, 0, 1971, 1141))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("gui_jpg\Black_Template.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, -90, 551, 341))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("gui_jpg\initial.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 800, 151, 50))
        self.pushButton.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"font: 75 italic 18pt \"Segoe UI\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1070, 800, 151, 51))
        self.pushButton_2.setStyleSheet("color: rgb(170, 85, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(42, 117, 255);\n"
"font: 75 italic 18pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.voice_label = QtWidgets.QLabel(self.centralwidget)
        self.voice_label.setGeometry(QtCore.QRect(670, 100, 611, 501))
        self.voice_label.setText("")
        self.voice_label.setPixmap(QtGui.QPixmap("gui_jpg/flo-motion_5sec.gif"))
        self.voice_label.setScaledContents(True)
        self.voice_label.setObjectName("voice_label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(1550, 40, 361, 71))
        self.textBrowser.setStyleSheet("background-color: Transparent;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color:rgb(2, 200, 144)")
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1520, 20, 401, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("gui_jpg/button_background.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1520, 170, 401, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("gui_jpg/button_background.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(1540, 190, 361, 71))
        self.textBrowser_2.setStyleSheet("background-color: Transparent;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color:rgb(2, 200, 144)")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1520, 300, 401, 101))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("gui_jpg/button_background.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(1540, 310, 361, 71))
        self.textBrowser_3.setStyleSheet("background-color: Transparent;\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color:rgb(2, 200, 144)")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.circle_gif = QtWidgets.QLabel(self.centralwidget)
        self.circle_gif.setGeometry(QtCore.QRect(1470, 560, 451, 291))
        self.circle_gif.setText("")
        self.circle_gif.setPixmap(QtGui.QPixmap("gui_jpg\moving_circle.gif"))
        self.circle_gif.setScaledContents(True)
        self.circle_gif.setObjectName("circle_gif")
        self.Youtube = QtWidgets.QPushButton(self.centralwidget)
        self.Youtube.setGeometry(QtCore.QRect(110, 600, 151, 91))
        self.Youtube.setStyleSheet("background:transparent")
        self.Youtube.setObjectName("Youtube")
        self.whatsappweb_button = QtWidgets.QPushButton(self.centralwidget)
        self.whatsappweb_button.setGeometry(QtCore.QRect(150, 760, 161, 91))
        self.whatsappweb_button.setStyleSheet("background:transparent")
        self.whatsappweb_button.setObjectName("whatsappweb_button")
        self.mail_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.mail_pushbutton.setGeometry(QtCore.QRect(110, 410, 161, 111))
        self.mail_pushbutton.setStyleSheet("background:transparent")
        self.mail_pushbutton.setObjectName("mail_pushbutton")
        self.chrome = QtWidgets.QPushButton(self.centralwidget)
        self.chrome.setGeometry(QtCore.QRect(110, 250, 121, 111))
        self.chrome.setStyleSheet("background:transparent")
        self.chrome.setObjectName("chrome")
        self.chrome_label = QtWidgets.QLabel(self.centralwidget)
        self.chrome_label.setGeometry(QtCore.QRect(30, 240, 141, 121))
        self.chrome_label.setText("")
        self.chrome_label.setPixmap(QtGui.QPixmap("gui_jpg\google.png")) 
        self.chrome_label.setScaledContents(True)
        self.chrome_label.setObjectName("chrome_label")
        self.mail_background = QtWidgets.QLabel(self.centralwidget)
        self.mail_background.setGeometry(QtCore.QRect(40, 410, 161, 111))
        self.mail_background.setText("")
        self.mail_background.setPixmap(QtGui.QPixmap("gui_jpg\gmail.png"))
        self.mail_background.setScaledContents(True)
        self.mail_background.setObjectName("mail_background")
        self.youtube_label = QtWidgets.QLabel(self.centralwidget)
        self.youtube_label.setGeometry(QtCore.QRect(30, 590, 161, 111))
        self.youtube_label.setText("")
        self.youtube_label.setPixmap(QtGui.QPixmap("gui_jpg\youtube.png"))
        self.youtube_label.setScaledContents(True)
        self.youtube_label.setObjectName("youtube_label")
        self.whatsapp_web_label = QtWidgets.QLabel(self.centralwidget)
        self.whatsapp_web_label.setGeometry(QtCore.QRect(50, 750, 161, 91))
        self.whatsapp_web_label.setText("")
        self.whatsapp_web_label.setPixmap(QtGui.QPixmap("gui_jpg\whatsapp.png"))
        self.whatsapp_web_label.setScaledContents(True)
        self.whatsapp_web_label.setObjectName("whatsapp_web_label")
        self.spotify_button = QtWidgets.QPushButton(self.centralwidget)
        self.spotify_button.setGeometry(QtCore.QRect(370, 460, 181, 101))
        self.spotify_button.setStyleSheet("background:transparent")
        self.spotify_button.setObjectName("spotify_button")
        self.spotify_gif = QtWidgets.QLabel(self.centralwidget)
        self.spotify_gif.setGeometry(QtCore.QRect(360, 400, 181, 121))
        self.spotify_gif.setText("")
        self.spotify_gif.setPixmap(QtGui.QPixmap("gui_jpg\spotify.png"))
        self.spotify_gif.setScaledContents(True)
        self.spotify_gif.setObjectName("spotify_gif")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.label_10.raise_()
        self.textBrowser.raise_()
        self.voice_label.raise_()
        self.label_3.raise_()
        self.circle_gif.raise_()
        self.textBrowser_2.raise_()
        self.textBrowser_3.raise_()
        self.Youtube.raise_()
        self.whatsappweb_button.raise_()
        self.mail_pushbutton.raise_()
        self.chrome.raise_()
        self.chrome_label.raise_()
        self.mail_background.raise_()
        self.youtube_label.raise_()
        self.whatsapp_web_label.raise_()
        self.spotify_button.raise_()
        self.spotify_gif.raise_()
        Voice_assistant.setCentralWidget(self.centralwidget)
        self.retranslateUi(Voice_assistant)
        QtCore.QMetaObject.connectSlotsByName(Voice_assistant)
        Voice_assistant.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, Voice_assistant):
        _translate = QtCore.QCoreApplication.translate
        Voice_assistant.setWindowTitle(_translate("Voice_assistant", "MainWindow"))
        self.pushButton.setText(_translate("Voice_assistant", "START"))
        self.pushButton_2.setText(_translate("Voice_assistant", "EXIT"))
        self.Youtube.setText(_translate("Voice_assistant", "PushButton"))
        self.whatsappweb_button.setText(_translate("Voice_assistant", "PushButton"))
        self.mail_pushbutton.setText(_translate("Voice_assistant", "PushButton"))
        self.chrome.setText(_translate("Voice_assistant", "PushButton"))
        self.spotify_button.setText(_translate("Voice_assistant", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Voice_assistant = QtWidgets.QMainWindow()
    ui = Ui_Voice_assistant()
    ui.setupUi(Voice_assistant)
    Voice_assistant.show()
    sys.exit(app.exec_())
