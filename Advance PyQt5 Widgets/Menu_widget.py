# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:58:33 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Menu Widget")
        self.setGeometry(350,150,600,600)
        self.UI()
        
    def UI(self):
        #################### Main Menu ###################
        menubar = self.menuBar()
        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        code = menubar.addMenu("Code")
        help_ = menubar.addMenu("Help")
        
        ################### Sub Menu Items ###############
        new = QAction("New Project", self)
        new.setShortcut("Ctrl+O")
        file.addAction(new)
        open_ = QAction("Open", self)
        file.addAction(open_)
        exit_ = QAction("Exit", self)
        exit_.setIcon((QIcon("icons/exit.png")))
        exit_.triggered.connect(self.exitFunc)
        file.addAction(exit_)
        
        self.show()
        
    def exitFunc(self):
        mbox = QMessageBox.information(self, "Warning", "Are you sure to exit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if mbox == QMessageBox.Yes:
            sys.exit()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()