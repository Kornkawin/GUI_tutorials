# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:32:49 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,550,250)
        self.setWindowTitle("Using Labels")
        self.UI()
        
    def UI(self):
        text1=QLabel("Hello python", self)
        text1.move(100,50)
        text2=QLabel("Hello world", self)
        text2.move(200,50)
        self.show()
        
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        