# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:38:24 2020

@author: Kornkawin
"""

import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QMessageBox, QWidget, QApplication
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint


# If you want to set font by yourself.
fontText = QFont("Times", 14)
fontButton = QFont("Arial", 12)

# Score
comScore = 0
playerScore = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,30,1920,1000)
        self.setWindowTitle("Rock Paper Scissors Game")
        self.UI()
        
    def UI(self):
        ######################## Scores ######################
        self.scoreComputerText = QLabel("Computer Score: ", self)
        self.scoreComputerText.move(30,20)
        self.scoreComputerText.setFont(fontText)
        self.scoreComputerText.resize(400,20)
        self.scorePlayerText = QLabel("Your Score: ", self)
        self.scorePlayerText.move(330,20)
        self.scorePlayerText.setFont(fontText)
        self.scorePlayerText.resize(400,20)
        ####################### Images #######################
        self.imageComputer = QLabel(self)
        self.imageComputer.setPixmap(QPixmap("image/Rock_com.png"))
        self.imageComputer.move(200,400)
        self.imagePlayer = QLabel(self)
        self.imagePlayer.setPixmap(QPixmap("image/Rock_user.png"))
        self.imagePlayer.move(1400,400)
        self.imageVersus = QLabel(self)
        self.imageVersus.setPixmap(QPixmap("image/vs.png"))
        self.imageVersus.move(700,300)
        ####################### Button #######################
        btnStart = QPushButton("Start", self)
        btnStart.setFont(fontButton)
        btnStart.move(30, 50)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.move(130, 50)
        btnStop.setFont(fontButton)
        btnStop.clicked.connect(self.stop)
        ###################### Timers ########################
        self.timer = QTimer()
        # 100 milliseconds
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.playgame)
        
        self.show()
        
    def start(self):
        self.timer.start()
        
    def stop(self):
        global comScore
        global playerScore
        self.timer.stop()
        
        # 1 Rock, 2 Paper, 3 Scissors
        if self.rndCom == 1 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Information", "Draw Game")
        elif self.rndCom == 1 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score: {}".format(playerScore))
        elif self.rndCom == 1 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "You Lose")
            comScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(comScore))
        elif self.rndCom == 2 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Information", "You Lose")
            comScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(comScore))
        elif self.rndCom == 2 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "Information", "Draw Game")
        elif self.rndCom == 2 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score: {}".format(playerScore))
        elif self.rndCom == 3 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Information", "You Win")
            playerScore += 1
            self.scorePlayerText.setText("Your Score: {}".format(playerScore))
        elif self.rndCom == 3 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "Information", "You Lose")
            comScore += 1
            self.scoreComputerText.setText("Computer Score: {}".format(comScore))
        elif self.rndCom == 3 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Information", "Draw Game")
        
        print(playerScore, comScore)
        
        if comScore == 3 or playerScore == 3:
            mbox = QMessageBox.information(self, "Information", "Game Over")
            sys.exit()
            
    def playgame(self):
        self.rndCom = randint(1,3)
        self.rndPlayer = randint(1,3)
        
        if self.rndCom == 1:
            self.imageComputer.setPixmap(QPixmap("image/rock_com.png"))
        elif self.rndCom == 2:
            self.imageComputer.setPixmap(QPixmap("image/paper_com.png"))
        elif self.rndCom == 3:
            self.imageComputer.setPixmap(QPixmap("image/Scissors_com.png"))
        
        if self.rndPlayer == 1:
            self.imagePlayer.setPixmap(QPixmap("image/rock_user.png"))
        elif self.rndPlayer == 2:
            self.imagePlayer.setPixmap(QPixmap("image/paper_user.png"))
        elif self.rndPlayer == 3:
            self.imagePlayer.setPixmap(QPixmap("image/Scissors_user.png"))
            
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())
    
if __name__=="__main__":
    main()