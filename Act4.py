import os
from PyQt5 import QtGui, QtCore

from Tarea import *

class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def _init_(self, *args, **kwargs):
        QtWidgets.QMainWindow._init_(self, *args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.actualizar)

    def actualizar(self):
        lin1=self.lineEdit.text()
        lin2=self.lineEdit_2.text()
        lin3=self.lineEdit_3.text()

        lin2=(lin2+"\n")*int(lin3)
        archi1=open(f"{lin1}.txt","w")
        archi1.write(f"{lin2}.\n")

        contador = 0
        contador2 = 0
        for letra in lin2:
        	if letra.lower() in "aeiou":
        	   contador += 1

        for letra in lin2:
        	if letra.lower() in "bcdfghjklmnpqrstvwxyz":
        	   contador2 += 1

        self.lineEdit_5.setText(f" {contador}")
        self.lineEdit_4.setText(f" {contador2} ")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()