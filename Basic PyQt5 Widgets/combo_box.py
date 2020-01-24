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
        self.setWindowTitle("Using ComboBox")
        self.UI()
        
    def UI(self):
        self.combo= QComboBox(self)
        self.combo.move(150,100)
        self.combo.addItem("Python")
        self.combo.addItems(["C", "C++", "C#"])
                             
        list1= ["Batman", "Spiderman", "Superman"]
        for name in list1:
            self.combo.addItem(name)
        
        for number in range(18,101):
            self.combo.addItem(str(number))
                             
        button= QPushButton("Save", self)
        button.move(150,130)
        button.clicked.connect(self.getValue)
        
        self.show()
        
    def getValue(self):
        value= self.combo.currentText()
        print(value)
            
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        