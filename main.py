from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (QApplication, QMainWindow)
from PySide6.QtGui import QIcon
from ui_Cadastro import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("ConsultaMAX - Consulte e Cadastre Empresas")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow
    window.show
    app.exec()