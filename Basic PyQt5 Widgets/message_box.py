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
        self.setWindowTitle("Using Message Box")
        self.UI()
        
    def UI(self):
        button= QPushButton("Click ME!",self)
        button.setFont(font)
        button.move(200,150)
        button.clicked.connect(self.messageBox)
        self.show()
        
    def messageBox(self):
#        mbox= QMessageBox.question(self, "Warning!!", "Are you sure to exit?", 
#                                   QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel, 
#                                   QMessageBox.No)
#        if mbox==QMessageBox.Yes:
#            sys.exit()
#        elif mbox==QMessageBox.No:
#            print("You clicked No Button.")
        mbox= QMessageBox.information(self, "Information", "You logged out!")
                
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        