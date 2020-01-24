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
        self.setWindowTitle("Using LineEdits")
        self.UI()
        
    def UI(self):
        self.nameTextBox= QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please enter your name")
        self.nameTextBox.move(150,50)
        self.passTextBox= QLineEdit(self)
        self.passTextBox.setPlaceholderText("Please enter your password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(150,80)
        
        Button= QPushButton("Save", self)
        Button.move(180,130)
        Button.clicked.connect(self.getValues)
    
        self.show()
        
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
        