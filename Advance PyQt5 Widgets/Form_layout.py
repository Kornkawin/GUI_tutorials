# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:58:33 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Form Layout")
        self.setGeometry(350,150,400,400)
        self.UI()
        
    def UI(self):
        formLayout = QFormLayout()
#        formLayout.setRowWrapPolicy(QFormLayout.WrapAllRows)
        
        nameText = QLabel("Name: ")
        name_input = QLineEdit()
        pwdText = QLabel("Password: ")
        pwd_input = QLineEdit()
        
        hbox = QHBoxLayout()
        hbox.addStretch()
        hbox.addWidget(QPushButton("Enter"))
        hbox.addWidget(QPushButton("Exit"))
        
        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLineEdit())
        hbox1.addWidget(QLineEdit())
        
        formLayout.addRow(nameText, hbox1)
        formLayout.addRow(pwdText, pwd_input)
        formLayout.addRow(QLabel("Country: "), QComboBox())
#        formLayout.addRow(QPushButton("Enter"), QPushButton("Exit"))
        formLayout.addRow(hbox)
        
        self.setLayout(formLayout)
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()