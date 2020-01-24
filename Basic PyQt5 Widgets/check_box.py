# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:32:49 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,550,250)
        self.setWindowTitle("Using CheckBox")
        self.UI()
        
    def UI(self):
        self.name= QLineEdit(self)
        self.name.setPlaceholderText("Enter your name")
        self.surname= QLineEdit(self)
        self.surname.setPlaceholderText("Enter your surname")
        self.name.move(150,50)
        self.surname.move(150,80)
        self.remember= QCheckBox("Remember me", self)
        self.remember.move(150,110)
        button= QPushButton("Submit", self)
        button.move(200,140)
        button.clicked.connect(self.submit)
        
        self.show()
        
    def submit(self):
        if self.remember.isChecked():
            print("Name: {} \nSurname: {} \nRemember me checked!".format(self.name.text(), self.surname.text()))
        else:
            print("Name: {} \nSurname: {} \nRemember me not checked!".format(self.name.text(), self.surname.text()))
        
    def getValues(self):
        name=self.nameTextBox.text()
        password=self.passTextBox.text()
        print(name,password)
        self.setWindowTitle("Your name is: {} Your password is: {}".format(name,password))
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        