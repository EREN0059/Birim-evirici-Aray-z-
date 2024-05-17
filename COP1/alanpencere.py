# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_alan(object):
    def setupUi(self, MainWindow_alan):
        MainWindow_alan.setObjectName("MainWindow_alan")
        MainWindow_alan.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow_alan)
        self.centralwidget.setObjectName("centralwidget")
        
        # Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 30, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: #737373;")  # Rengi ayarlandı
        self.label.setText("ALAN")
        
        # Birinci Birim ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 210, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont("Arial", 11))
        self.comboBox.addItems(["Nanaometrekare(nm²)", "Mikrometrekare(µs²)", "Milimetrekare(mm²)", "Santimetrekare(cm²)",
                                "Desimetrekare(dm²)", "Metrekare(m²)", "Dekametrekare(dam²)", "Hektometrekare(hm²)",
                                "Kilometrekare(km²)", "İnçkare(in²)", "Fit(foot/feet)kare(ft²)", "Yardakare(yd²)",
                                "Milkare(mi²)"])
        
        # İkinci Birim ComboBox
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 320, 210, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(QtGui.QFont("Arial", 11))
        self.comboBox_2.addItems(["Nanaometrekare(nm²)", "Mikrometrekare(µs²)", "Milimetrekare(mm²)", "Santimetrekare(cm²)",
                                "Desimetrekare(dm²)", "Metrekare(m²)", "Dekametrekare(dam²)", "Hektometrekare(hm²)",
                                "Kilometrekare(km²)", "İnçkare(in²)", "Fit(foot/feet)kare(ft²)", "Yardakare(yd²)",
                                "Milkare(mi²)"])
        
        # İlk Değer Giriş Kutusu
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 130, 250, 35))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QtGui.QFont("Arial", 11))
        self.lineEdit.setPlaceholderText("Değer giriniz")
        self.lineEdit.setStyleSheet("border-radius: 4px;")
        
        # İkinci Değer Giriş Kutusu
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 320, 250, 35))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(QtGui.QFont("Arial", 11))
        self.lineEdit_2.setPlaceholderText("Sonuç")
        self.lineEdit_2.setStyleSheet("border-radius: 4px;")
        
        MainWindow_alan.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_alan)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_alan.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_alan)
        self.statusbar.setObjectName("statusbar")
        MainWindow_alan.setStatusBar(self.statusbar)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.retranslateUi(MainWindow_alan)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_alan)

        # Dönüştürme Butonu
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(235, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))  # Arial fontu ve yazı boyutu 11
        self.pushButton.clicked.connect(self.convert_area)
        
        # Değiştirme Butonları
        self.swapValuesButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapValuesButton.setGeometry(QtCore.QRect(405, 205, 75, 75))
        self.swapValuesButton.setObjectName("swapValuesButton")
        self.swapValuesButton.setText("")
        self.swapValuesButton.clicked.connect(self.swap_values)
        self.swapValuesButton.setStyleSheet("background-image: url(logolar/degistir.png); background-color: white;")
        
        self.swapUnitsButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapUnitsButton.setGeometry(QtCore.QRect(80, 205, 75, 75))
        self.swapUnitsButton.setObjectName("swapUnitsButton")
        self.swapUnitsButton.setText("")
        self.swapUnitsButton.clicked.connect(self.swap_units)
        self.swapUnitsButton.setStyleSheet("background-image: url(logolar/degistir.png); background-color: white;")

    def retranslateUi(self, MainWindow_alan):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_alan.setWindowTitle(_translate("MainWindow_alan", "ALAN"))

    def convert_area(self):
        units = {
            "Nanaometrekare(nm²)": 1e-18, "Mikrometrekare(µs²)": 1e-12, "Milimetrekare(mm²)": 1e-6, "Santimetrekare(cm²)": 1e-4,
            "Desimetrekare(dm²)": 1e-2, "Metrekare(m²)": 1.0, "Dekametrekare(dam²)": 1e1, "Hektometrekare(hm²)": 1e2,
            "Kilometrekare(km²)": 1e6, "İnçkare(in²)": 0.00064516, "Fit(foot/feet)kare(ft²)": 0.092903, "Yardakare(yd²)": 0.836127,
            "Milkare(mi²)": 2.58999e6
        }

        from_unit = self.comboBox.currentText()
        to_unit = self.comboBox_2.currentText()
        input_value = float(self.lineEdit.text())

        from_value = units[from_unit]
        to_value = units[to_unit]

        result = input_value * from_value / to_value
        self.lineEdit_2.setText(str(result))
        
    def swap_values(self):
        temp = self.lineEdit.text()
        self.lineEdit.setText(self.lineEdit_2.text())
        self.lineEdit_2.setText(temp)
        
    def swap_units(self):
        temp = self.comboBox.currentIndex()
        self.comboBox.setCurrentIndex(self.comboBox_2.currentIndex())
        self.comboBox_2.setCurrentIndex(temp)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_alan = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_alan()
    ui.setupUi(MainWindow_alan)
    MainWindow_alan.show()
    sys.exit(app.exec_())
