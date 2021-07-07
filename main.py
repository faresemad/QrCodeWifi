#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv
from PyQt5.uic import loadUi
from os import system , remove
import wifi_qrcode
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("index.ui",self)
        self.setWindowTitle("QrCode Geberator By Fares Emad")    # Set A Title For My App
        self.setWindowIcon(QIcon("icon.ico"))    # Set A Icon For My App
        self.setWindowIconText("logo")
        self.setFont(QFont("Arial Black")) # Set A Font For My App
        self.handelUi()
        self.handelEvent()
        #==Selector Goes Here==#
#========================================================================================#
    def handelUi(self):
        self.qrlable = self.findChild(QLabel , "label")
        self.wifiname = self.findChild(QLineEdit , "lineEdit")
        self.wifipassword = self.findChild(QLineEdit , "lineEdit_2")
        self.combox = self.findChild(QComboBox , "comboBox")
        self.eye = self.findChild(QPushButton , "pushButton")
        self.generator = self.findChild(QPushButton , "pushButton_2")
    def handelEvent(self):
        self.eye.setIcon(QIcon("eye.ico"))
        self.eye.setCheckable(True)
        self.eye.clicked.connect(self.checkEye)
        self.combox.addItems(["WPA","WPA2","WEP"])
        self.generator.clicked.connect(self.handelgenerator)
#========================================================================================#
        #==Function Here==#
#========================================================================================#
    def checkEye(self):
        if self.eye.isChecked():
            self.wifipassword.setEchoMode(QLineEdit.Normal)
        else:
            self.wifipassword.setEchoMode(QLineEdit.Password)
    def handelgenerator(self):
        ssid = self.wifiname.text()
        mode = self.combox.currentText()
        passwd = self.wifipassword.text()

        try:
            system(f"python -m wifi_qrcode wifi --ssid {ssid} --auth {mode} --password {passwd}")
        except Exception:
            system(f"python3 -m wifi_qrcode wifi --ssid {ssid} --auth {mode} --password {passwd}")

        try:
            self.qrlable.setPixmap(QPixmap("qrcode.png"))
            remove("qrcode.png")
        except Exception:
            pass
        self.wifiname.clear();self.wifipassword.clear()
#========================================================================================#
def run():
    try:
        app=QApplication(argv)
        myapp=Mainwindow()
        myapp.show()
        app.exec_()
    except Exception as error:
        print(error)
if __name__ == "__main__":
    run()