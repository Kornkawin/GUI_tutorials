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
        self.setWindowTitle("Using Buttons")
        self.UI()
        
    def UI(self):
        self.text=QLabel("My Text", self)
        self.text.move(150,50)
        enterButton= QPushButton("Enter", self)
        enterButton.move(100,80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton= QPushButton("Exit", self)
        exitButton.move(200,80)
        exitButton.clicked.connect(self.exitFunc)
        self.show()
        
    def enterFunc(self):
        self.text.setText(r"You clicked 'Enter'")
        self.text.resize(150,20)
    
    def exitFunc(self):
        self.text.setText(r"You clicked 'Exit'")
        self.text.resize(150,20)
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        