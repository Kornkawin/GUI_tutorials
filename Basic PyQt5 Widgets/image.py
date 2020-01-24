# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 09:32:49 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,1000,1000)
        self.setWindowTitle("Using Image")
        self.UI()
        
    def UI(self):
        self.image= QLabel(self)
        self.image.setPixmap(QPixmap('G:/_ATOM/GUI/image/logo.png'))
        self.image.move(150,50)
        removeButton= QPushButton("Remove", self)
        removeButton.move(150,800)
        removeButton.clicked.connect(self.removeImage)
        showButton= QPushButton("Show", self)
        showButton.move(260,800)
        showButton.clicked.connect(self.showImage)
        self.show()
        
    def removeImage(self):
        self.image.close()
    def showImage(self):
        self.image.show()
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        