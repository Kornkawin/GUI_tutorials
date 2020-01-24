# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 14:58:33 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Slider Widget")
        self.setGeometry(350,150,600,500)
        self.UI()
        
    def UI(self):
        vbox = QVBoxLayout()
#        self.slider = QSlider()    # Vertical
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.getValue)
        self.text1 = QLabel("0")
        self.text1.setAlignment(Qt.AlignCenter)
        self.text2 = QLabel("Hello Python")
        
        vbox.addStretch()
        vbox.addWidget(self.text1)
        vbox.addWidget(self.text2)
        vbox.addWidget(self.slider)
        
        self.setLayout(vbox)
        self.show()
        
    def getValue(self):
        val = self.slider.value()
        print(val)
        self.text1.setText(str(val))
        fontSize = self.slider.value()
        font = QFont("Times", fontSize)
        self.text2.setFont(font)
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()