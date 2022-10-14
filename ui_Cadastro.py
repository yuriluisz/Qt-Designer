# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1097, 709)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(202, 202, 202);")
        self.Main = QWidget(MainWindow)
        self.Main.setObjectName(u"Main")
        self.Main.setStyleSheet(u"*{\n"
"\n"
"	border:none;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.Main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LCont = QFrame(self.Main)
        self.LCont.setObjectName(u"LCont")
        self.LCont.setMaximumSize(QSize(200, 16777215))
        self.LCont.setFrameShape(QFrame.StyledPanel)
        self.LCont.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LCont)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.LCont)
        self.frame.setObjectName(u"frame")
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.LCont)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(135, 135, 135);\n"
"}\n"
"\n"
"\n"
"QToolBox::tab{\n"
"\n"
"	border-raius:5px;\n"
"\n"
"	text-align::left;\n"
"}\n"
"\n"
"QToolBox{\n"
"	\n"
"	text-align:left;\n"
"	\n"
"	background-color: rgb(135, 135, 135);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(156, 156, 156);\n"
"	border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:15px;\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 156, 528))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(120, 12))
        self.btn_home.setSizeIncrement(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_Cadastro = QPushButton(self.page)
        self.btn_Cadastro.setObjectName(u"btn_Cadastro")
        self.btn_Cadastro.setMinimumSize(QSize(120, 12))
        self.btn_Cadastro.setSizeIncrement(QSize(0, 30))
        self.btn_Cadastro.setFont(font1)
        self.btn_Cadastro.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_Cadastro)

        self.btn_contatos = QPushButton(self.page)
        self.btn_contatos.setObjectName(u"btn_contatos")
        self.btn_contatos.setMinimumSize(QSize(120, 12))
        self.btn_contatos.setSizeIncrement(QSize(0, 30))
        self.btn_contatos.setFont(font1)
        self.btn_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_contatos)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(120, 12))
        self.btn_sobre.setSizeIncrement(QSize(0, 30))
        self.btn_sobre.setFont(font1)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 156, 528))
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 10, 131, 351))
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.frame_4)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.horizontalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.LCont)

        self.RCont = QFrame(self.Main)
        self.RCont.setObjectName(u"RCont")
        self.RCont.setFrameShape(QFrame.StyledPanel)
        self.RCont.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.RCont)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Cabec = QFrame(self.RCont)
        self.Cabec.setObjectName(u"Cabec")
        self.Cabec.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(32)
        self.Cabec.setFont(font2)
        self.Cabec.setFrameShape(QFrame.StyledPanel)
        self.Cabec.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Cabec)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.Cabec)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(185, 185, 185);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/barra-de-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignLeft)

        self.label = QLabel(self.Cabec)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(16)
        self.label.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Cabec)

        self.Main_2 = QFrame(self.RCont)
        self.Main_2.setObjectName(u"Main_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_2.sizePolicy().hasHeightForWidth())
        self.Main_2.setSizePolicy(sizePolicy)
        self.Main_2.setStyleSheet(u"background-color: rgb(184, 184, 184);")
        self.Main_2.setFrameShape(QFrame.StyledPanel)
        self.Main_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.Main_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Pages = QStackedWidget(self.Main_2)
        self.Pages.setObjectName(u"Pages")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.verticalLayout_7 = QVBoxLayout(self.Home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Icon = QLabel(self.Home)
        self.Icon.setObjectName(u"Icon")

        self.verticalLayout_7.addWidget(self.Icon)

        self.Pages.addWidget(self.Home)
        self.Cadastro = QWidget()
        self.Cadastro.setObjectName(u"Cadastro")
        self.Cadastro.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.Cadastro)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabWidget = QTabWidget(self.Cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.tabWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_11 = QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.tab)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.title = QLabel(self.frame_6)
        self.title.setObjectName(u"title")

        self.gridLayout.addWidget(self.title, 0, 0, 1, 4)

        self.linNome = QLineEdit(self.frame_6)
        self.linNome.setObjectName(u"linNome")

        self.gridLayout.addWidget(self.linNome, 1, 0, 1, 1)

        self.linNome_2 = QLineEdit(self.frame_6)
        self.linNome_2.setObjectName(u"linNome_2")

        self.gridLayout.addWidget(self.linNome_2, 1, 1, 1, 3)

        self.linLogra = QLineEdit(self.frame_6)
        self.linLogra.setObjectName(u"linLogra")

        self.gridLayout.addWidget(self.linLogra, 2, 0, 1, 4)

        self.linNum = QLineEdit(self.frame_6)
        self.linNum.setObjectName(u"linNum")

        self.gridLayout.addWidget(self.linNum, 3, 0, 1, 2)

        self.linCompl = QLineEdit(self.frame_6)
        self.linCompl.setObjectName(u"linCompl")

        self.gridLayout.addWidget(self.linCompl, 3, 2, 1, 1)

        self.linBairro = QLineEdit(self.frame_6)
        self.linBairro.setObjectName(u"linBairro")

        self.gridLayout.addWidget(self.linBairro, 3, 3, 1, 1)

        self.linMunic = QLineEdit(self.frame_6)
        self.linMunic.setObjectName(u"linMunic")

        self.gridLayout.addWidget(self.linMunic, 4, 0, 1, 2)

        self.linUF = QLineEdit(self.frame_6)
        self.linUF.setObjectName(u"linUF")

        self.gridLayout.addWidget(self.linUF, 4, 2, 1, 1)

        self.linCep = QLineEdit(self.frame_6)
        self.linCep.setObjectName(u"linCep")

        self.gridLayout.addWidget(self.linCep, 4, 3, 1, 1)

        self.linTel = QLineEdit(self.frame_6)
        self.linTel.setObjectName(u"linTel")

        self.gridLayout.addWidget(self.linTel, 5, 0, 1, 1)

        self.linEmail = QLineEdit(self.frame_6)
        self.linEmail.setObjectName(u"linEmail")

        self.gridLayout.addWidget(self.linEmail, 5, 1, 1, 3)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.Cadast = QPushButton(self.tab)
        self.Cadast.setObjectName(u"Cadast")
        self.Cadast.setMinimumSize(QSize(120, 31))
        self.Cadast.setFont(font1)
        self.Cadast.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(156, 156, 156);\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"}\n"
"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_11.addWidget(self.Cadast, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_10 = QVBoxLayout(self.tab_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Titl = QLabel(self.tab_2)
        self.Titl.setObjectName(u"Titl")

        self.verticalLayout_10.addWidget(self.Titl)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.painel = QTableWidget(self.tab_2)
        if (self.painel.columnCount() < 9):
            self.painel.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.painel.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.painel.setObjectName(u"painel")
        self.painel.setStyleSheet(u"QHeaderView::section {\n"
"background-color: rgb(112, 112, 112);\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(236, 236, 236);\n"
"}")

        self.horizontalLayout_6.addWidget(self.painel)

        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius:15px;\n"
"	background-color: rgb(218, 218, 218);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btnGer = QPushButton(self.frame_5)
        self.btnGer.setObjectName(u"btnGer")
        self.btnGer.setMinimumSize(QSize(120, 30))
        font4 = QFont()
        font4.setPointSize(10)
        self.btnGer.setFont(font4)
        self.btnGer.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(70, 212, 104);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_9.addWidget(self.btnGer)

        self.btnAlt = QPushButton(self.frame_5)
        self.btnAlt.setObjectName(u"btnAlt")
        self.btnAlt.setMinimumSize(QSize(120, 30))
        self.btnAlt.setFont(font4)
        self.btnAlt.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(231, 231, 31);\n"
"border-radius:15px;\n"
"}")

        self.verticalLayout_9.addWidget(self.btnAlt)

        self.btnExcl = QPushButton(self.frame_5)
        self.btnExcl.setObjectName(u"btnExcl")
        self.btnExcl.setMinimumSize(QSize(120, 30))
        self.btnExcl.setFont(font4)
        self.btnExcl.setStyleSheet(u"QPushButton:hover{\n"
"background-color: rgb(220, 0, 0);\n"
"border-radius:15px;\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_9.addWidget(self.btnExcl)

        self.spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.spacer1)


        self.horizontalLayout_6.addWidget(self.frame_5)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.Cadastro)
        self.Contatos = QWidget()
        self.Contatos.setObjectName(u"Contatos")
        self.verticalLayout_12 = QVBoxLayout(self.Contatos)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.cntt = QLabel(self.Contatos)
        self.cntt.setObjectName(u"cntt")

        self.verticalLayout_12.addWidget(self.cntt)

        self.Pages.addWidget(self.Contatos)
        self.Sobre = QWidget()
        self.Sobre.setObjectName(u"Sobre")
        self.verticalLayout_6 = QVBoxLayout(self.Sobre)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.Sobre)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_10 = QLabel(self.Sobre)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_6.addWidget(self.label_10)

        self.Pages.addWidget(self.Sobre)

        self.verticalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.Main_2)

        self.frame_3 = QFrame(self.RCont)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Inf = QLabel(self.frame_3)
        self.Inf.setObjectName(u"Inf")
        font5 = QFont()
        font5.setPointSize(9)
        self.Inf.setFont(font5)

        self.horizontalLayout_3.addWidget(self.Inf, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.RCont)

        MainWindow.setCentralWidget(self.Main)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CadastroMAX</span></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_Cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Page 1", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Usuario: Chepyz</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\">Sistema: Cadastro</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\">Status: Ativo</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\">Val: 13/03/2999</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CadastroMAX</span></p></body></html>", None))
        self.Icon.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/icons/Consulta MAX (512\u00a0\u00d7\u00a0512\u00a0px) (1).png\"/></p></body></html>", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Empresa</span></p></body></html>", None))
        self.linNome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.linNome_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.linLogra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None))
        self.linNum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.linCompl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None))
        self.linBairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.linMunic.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None))
        self.linUF.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.linCep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.linTel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.linEmail.setPlaceholderText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.Cadast.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Casastro", None))
        self.Titl.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Empresas</span></p></body></html>", None))
        ___qtablewidgetitem = self.painel.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.painel.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.painel.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem3 = self.painel.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"lOGRADOURO", None));
        ___qtablewidgetitem4 = self.painel.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.painel.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.painel.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem7 = self.painel.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem8 = self.painel.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        self.btnGer.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btnAlt.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btnExcl.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.cntt.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Contatos</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/icon/icons/instagram.png\"/> - <span style=\" font-size:16pt; font-weight:600;\">cadastromax_</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><img src=\":/icon/icons/o-email.png\"/> - <span style=\" font-size:16pt; font-weight:600;\">cadastromax@suporte.com</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p><p align=\"center\"><img src=\":/icon/icons/youtube.png\"/> - <span style=\" font-size:16pt; font-weight:600;\">CadastroMAX</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Sobre a CadastroMAX</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Nos somos uma empresa qualificada em consultas e cadastros de empresas</span></p><p align=\"center\"><span style=\" font-size:12pt;\"> em bancos de dados registrados, trabalhamos com a criacao dos bancos com o intuito de</span></p><p align=\"center\"><span style=\" font-size:12pt;\"> organizar, acelerar e facilitar o processo de cadastros das empresas.</span></p></body></html>", None))
        self.Inf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">CadastroMAX  CNPJ 453.456.4532-567  CEP 7456-324 </span></p></body></html>", None))
    # retranslateUi

