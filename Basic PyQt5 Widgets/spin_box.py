# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:32:49 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

# If you want to set font by yourself.
font = QFont("Times", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,550,250)
        self.setWindowTitle("Using Spin Box")
        self.UI()
        
    def UI(self):
        self.spinBox= QSpinBox(self)
        self.spinBox.move(150,100)
        self.spinBox.setFont(font)
#        self.spinBox.setMinimum(25)
#        self.spinBox.setMaximum(60)
        self.spinBox.setRange(25,60)
#        self.spinBox.setPrefix("$ ")
        self.spinBox.setSuffix(" cm")
        self.spinBox.setSingleStep(5) 
#        self.spinBox.valueChanged.connect(self.getValue)
        button= QPushButton("Send", self)
        button.move(150,140)
        button.clicked.connect(self.getValue)
        self.show()
                
    def getValue(self):
        value = self.spinBox.value()
        print(value)
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        