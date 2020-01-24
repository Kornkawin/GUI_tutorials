# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:58:33 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

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
        
        ################### ToolBar #######################
        tb = self.addToolBar("My Toolbar")
        
        # add text under icon in toolbar
        tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        newTb = QAction(QIcon('icons/folder.png'), "New", self)
        tb.addAction(newTb)
        openTb = QAction(QIcon('icons/empty.png'), "Open", self)
        tb.addAction(openTb)
        saveTb = QAction(QIcon('icons/save.png'), "Save", self)
        tb.addAction(saveTb)
        exitTb = QAction(QIcon('icons/exit.png'), "Exit", self)
        exitTb.triggered.connect(self.exitFunc)
        tb.addAction(exitTb)
        # add common function by .actionTriggered.connect()
        tb.actionTriggered.connect(self.btnFunc)
        # try adding combo box widget in the toolbar.
        self.combo = QComboBox()
        self.combo.addItems(["Spider", "Superman", "Batman"])
        tb.addWidget(self.combo)
        self.show()
        
    # This is a common function for the other three buttons.    
    def btnFunc(self, btn):
        if btn.text() == "New":
            print("You clicked new button")
        elif btn.text() == "Open":
            print("You clicked open button")
        else:
            print("You clicked save button")
    
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