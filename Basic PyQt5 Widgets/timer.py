# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:32:49 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer

# If you want to set font by yourself.
font = QFont("Times", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,550,550)
        self.setWindowTitle("Using Text Editor")
        self.UI()
        
    def UI(self):
        self.colorLabel= QLabel(self)
        self.colorLabel.resize(250,250)
        self.colorLabel.setStyleSheet("background-color: green")
        self.colorLabel.move(40,20)
        
        ############Buttons################
        btnStart= QPushButton("Start", self)
        btnStart.move(80,300)
        btnStart.clicked.connect(self.start)
        btnStop= QPushButton("Stop", self)
        btnStop.move(190,300)
        btnStop.clicked.connect(self.stop)
        
        ############Timer################
        self.timer= QTimer()
        # 1000 milliseconds = 1 second
        self.timer.setInterval(1000)
        # change color every timeout (1 second)
        self.timer.timeout.connect(self.changeColor)
        self.value = 0
        
        self.show()
        
    def changeColor(self):
        if self.value == 0:
            self.colorLabel.setStyleSheet("background-color: yellow")
            self.value = 1
        elif self.value == 1:
            self.colorLabel.setStyleSheet("background-color: green")
            self.value = 0
            
    def start(self):
        self.timer.start()
        
    def stop(self):
        self.timer.stop()
        
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    # we can start timer at the start of application by this method.
    window.start()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        