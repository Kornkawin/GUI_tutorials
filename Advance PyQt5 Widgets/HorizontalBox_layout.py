# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:36:10 2020

@author: Kornkawin
"""

'''
    Professional way to develop applications.
'''

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Horizontal Box Layout")
        self.setGeometry(350,150,400,400)
        self.UI()
        
    def UI(self):
        hbox = QHBoxLayout()
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")
        button3 = QPushButton("Button3")
        
        # Before widgets added, Push left to right
        hbox.addStretch()
        
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        hbox.addWidget(button3)
        
        # After widgets added, Push right to left
        hbox.addStretch()
        
        # If there are 2 ways stretch, widgets at the center.
        
        # Add HBoxLayout to Window
        self.setLayout(hbox)
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()