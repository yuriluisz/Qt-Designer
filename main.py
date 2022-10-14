import sys

'''from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtCore import QCoreApplication'''

from ui_Cadastro import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class mainwindow(Ui_MainWindow):
    def __init__(self):
        super(mainwindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ConsultaMAX - Consulte e Cadastre Empresas")


if __name__ == "__main__":
    app = QtWidgets(sys.argv)
    window = mainwindow
    window.show()
    app.exec()
