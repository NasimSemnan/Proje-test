from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 439)
        MainWindow.setStyleSheet("background-color: rgb(48, 76, 107);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt = QtWidgets.QLineEdit(self.centralwidget)
        self.txt.setGeometry(QtCore.QRect(20, 30, 311, 51))
        self.txt.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                               "color: rgb(255, 255, 255);\n"
                               "font: 16pt \"B Zar\";\n"
                               "border-radius:10px;\n"
                               "border:2px;")
        self.txt.setObjectName("txt")
        self.btn_dasad = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dasad.setGeometry(QtCore.QRect(20, 110, 75, 51))
        self.btn_dasad.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                     "font: 18pt \"B Tir\";")
        self.btn_dasad.setObjectName("btn_dasad")
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_c.setGeometry(QtCore.QRect(100, 110, 75, 51))
        self.btn_c.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_c.setObjectName("btn_c")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(180, 110, 75, 51))
        self.btn_back.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                    "font: 18pt \"B Tir\";")
        self.btn_back.setObjectName("btn_back")
        self.btn_taq = QtWidgets.QPushButton(self.centralwidget)
        self.btn_taq.setGeometry(QtCore.QRect(260, 110, 75, 51))
        self.btn_taq.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                   "font: 18pt \"B Tir\";")
        self.btn_taq.setObjectName("btn_taq")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(180, 170, 75, 51))
        self.btn_9.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_9.setObjectName("btn_9")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(20, 170, 75, 51))
        self.btn_7.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_7.setObjectName("btn_7")
        self.btn_zarb = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zarb.setGeometry(QtCore.QRect(260, 170, 75, 51))
        self.btn_zarb.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                    "font: 18pt \"B Zar\";")
        self.btn_zarb.setObjectName("btn_zarb")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 170, 75, 51))
        self.btn_8.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_8.setObjectName("btn_8")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(180, 230, 75, 51))
        self.btn_6.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_6.setObjectName("btn_6")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(20, 230, 75, 51))
        self.btn_4.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_4.setObjectName("btn_4")
        self.btn_menha = QtWidgets.QPushButton(self.centralwidget)
        self.btn_menha.setGeometry(QtCore.QRect(260, 230, 75, 51))
        self.btn_menha.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                     "font: 18pt \"B Tir\";")
        self.btn_menha.setObjectName("btn_menha")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 230, 75, 51))
        self.btn_5.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_5.setObjectName("btn_5")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(180, 290, 75, 51))
        self.btn_3.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_3.setObjectName("btn_3")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(20, 290, 75, 51))
        self.btn_1.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_1.setObjectName("btn_1")
        self.btn_jam = QtWidgets.QPushButton(self.centralwidget)
        self.btn_jam.setGeometry(QtCore.QRect(260, 290, 75, 51))
        self.btn_jam.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                   "font: 18pt \"B Tir\";")
        self.btn_jam.setObjectName("btn_jam")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 290, 75, 51))
        self.btn_2.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 18pt \"B Tir\";")
        self.btn_2.setObjectName("btn_2")
        self.btn_delnigh = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delnigh.setGeometry(QtCore.QRect(180, 350, 75, 51))
        self.btn_delnigh.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                       "font: 18pt \"B Tir\";")
        self.btn_delnigh.setObjectName("btn_delnigh")
        self.btn_jammenha = QtWidgets.QPushButton(self.centralwidget)
        self.btn_jammenha.setGeometry(QtCore.QRect(20, 350, 75, 51))
        self.btn_jammenha.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                        "font: 18pt \"B Zar\";\n"
                                        "font: 18pt \"B Tir\";")
        self.btn_jammenha.setObjectName("btn_jammenha")
        self.btn_mosavi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mosavi.setGeometry(QtCore.QRect(260, 350, 75, 51))
        self.btn_mosavi.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                      "font: 18pt \"B Tir\";")
        self.btn_mosavi.setObjectName("btn_mosavi")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(100, 350, 75, 51))
        self.btn_0.setStyleSheet("background-color: rgb(57, 84, 132);\n"
                                 "font: 19pt \"B Zar\";")
        self.btn_0.setObjectName("btn_0")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 354, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_dasad.setText(_translate("MainWindow", "%"))
        self.btn_c.setText(_translate("MainWindow", "C"))
        self.btn_back.setText(_translate("MainWindow", "back"))
        self.btn_taq.setText(_translate("MainWindow", "÷"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_zarb.setText(_translate("MainWindow", "×"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_menha.setText(_translate("MainWindow", "-"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_jam.setText(_translate("MainWindow", "+"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_delnigh.setText(_translate("MainWindow", "."))
        self.btn_jammenha.setText(_translate("MainWindow", "+/-"))
        self.btn_mosavi.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
