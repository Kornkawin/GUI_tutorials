# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:32:49 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,550,250)
        self.setWindowTitle("This is Window's title!")
        
        self.show()
        
App= QApplication(sys.argv)
window= Window()
sys.exit(App.exec_())
        