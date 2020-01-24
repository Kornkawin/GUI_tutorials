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
        self.setWindowTitle("Vertical Box Layout")
        self.setGeometry(350,150,400,400)
        self.UI()
        
    def UI(self):
        vbox = QVBoxLayout()
        button1 = QPushButton("Save")
        button2 = QPushButton("Exit")
        button3 = QPushButton("Hello")
        
        # Before widgets added, Push Top to Bottom
        vbox.addStretch()
        
        vbox.addWidget(button1)
        vbox.addWidget(button2)
        vbox.addWidget(button3)
        
        # After widgets added, Push Bottom to Top
        vbox.addStretch()
        
        # If there are 2 ways stretch, widgets at the center.
        
        # Add VBoxLayout to Window
        self.setLayout(vbox)
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()