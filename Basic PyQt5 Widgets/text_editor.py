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
        self.setWindowTitle("Using Text Editor")
        self.UI()
        
    def UI(self):
        self.editor= QTextEdit(self)
        self.editor.move(150,80)
        # If you don't want to accept rich text in editor.
#        self.editor.setAcceptRichText(False)
        
        button= QPushButton("Send", self)
        button.move(330,280)
        button.clicked.connect(self.getValue)
        
        self.show()
        
    def getValue(self):
        # Convert rich text to plain text. Then, print.
        text= self.editor.toPlainText()
        print(text)
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        