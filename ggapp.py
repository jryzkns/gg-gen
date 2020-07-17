from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit

from PyQt5.QtWidgets import QPushButton, QFileDialog
from PyQt5.QtCore import QSize

from gglib.productioncontext import ProductionContext
from gglib.gossiplib import generate

import os

class GGApp(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 140))

        preambley = 20
        self.preambleLabel = QLabel(self)
        self.preambleLabel.setText('preamble:')
        self.preambleLine = QLineEdit(self)
        self.preambleLine.move(80, preambley)
        self.preambleLine.resize(300, 32)
        self.preambleLabel.move(20, preambley)

        preambley = 60
        self.responseLabel = QLabel(self)
        self.responseLabel.setText('response:')
        self.responseLine = QLineEdit(self)
        self.responseLine.move(80, preambley)
        self.responseLine.resize(300, 32)
        self.responseLabel.move(20, preambley)

        confirmy = 100
        self.pybutton = QPushButton("Generate!", self)
        self.pybutton.clicked.connect(self.onConfirmClick)
        self.pybutton.resize(300,32)
        self.pybutton.move(80, confirmy) 

    def onConfirmClick(self):

        generate(
            ProductionContext(  
                self.preambleLine.text(),
                self.responseLine.text(),
                QFileDialog.getSaveFileName(self)[0]),
            "base.jpg",
            "arial.ttf", "Helvetica 33 Thin Extended.ttf")

