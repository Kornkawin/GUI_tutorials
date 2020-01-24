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
        self.setWindowTitle("Vertical Box & Horizontal Box Layout")
        self.setGeometry(350,150,400,400)
        self.UI()
        
    def UI(self):
        mainLayout = QVBoxLayout()
        topLayout = QHBoxLayout()
        bottomLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addLayout(bottomLayout)
        
        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()
        
        topLayout.setContentsMargins(20,10,20,10) # param: left, top, right, bottom
        topLayout.addWidget(cbox)
        topLayout.addWidget(rbtn)
        topLayout.addWidget(combo)
        
        bottomLayout.setContentsMargins(20,10,150,10)
        bottomLayout.addWidget(btn1)
        bottomLayout.addWidget(btn2)
        
        self.setLayout(mainLayout)
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()