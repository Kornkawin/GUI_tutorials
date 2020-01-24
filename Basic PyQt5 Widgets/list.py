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
        self.setGeometry(0,30,1920,1000)
        self.setWindowTitle("Using Lists widget")
        self.UI()
        
    def UI(self):
        self.addRecord = QLineEdit(self)
        self.addRecord.move(100,50)
        self.listWidget=QListWidget(self)
        self.listWidget.move(100,80)
        
        list1 = ["Batman", "Superman", "Spiderman"]
        self.listWidget.addItems(list1)
        self.listWidget.addItem("Human")
        
#        for number in range(5,11):
#            self.listWidget.addItem(str(number))
        
        ####################################################
        
        btnAdd = QPushButton("Add", self)
        btnAdd.move(360,80)
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete = QPushButton("Delete", self)
        btnDelete.move(360,110)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet = QPushButton("Get", self)
        btnGet.move(360,140)
        btnGet.clicked.connect(self.funcGet)
        btnDeleteAll = QPushButton("Delete All", self)
        btnDeleteAll.move(360,170)
        btnDeleteAll.clicked.connect(self.funcDeleteAll)
        
        self.show()
        
    def funcAdd(self):
        val = self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText("")
        
    def funcDelete(self):
        index = self.listWidget.currentRow()
        # print chosen row index
        print(index)
        self.listWidget.takeItem(index)
        
    def funcGet(self):
        val = self.listWidget.currentItem().text()
        print(val)
    
    def funcDeleteAll(self):
        self.listWidget.clear()
        
def main():
    App= QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()
        