# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

Conversions = {
    "Ohm(Ω)": 1,
    "Miliohm(mΩ)": 0.001,
    "Mikroohm(µΩ)": 1e-6,
    "Nanoohm(nΩ)": 1e-9,
    "Kiloohm(kΩ)": 1000,
    "Megaohm(MΩ)": 1e6,
    "Gigaohm(GΩ)": 1e9,
    "Planck Empedansı": 29.9792458,
    "Nicelenmiş Hall Direnci": 25812.807574,
    "ESU Direnci": 8987551787.368,
    "EMU Direnci": 1e-9,
    "Statohm": 898755200000,
    "Volt/Amper": 1,
    "Abohm": 1e-9
}


class Ui_MainWindow_direnc(object):
    def setupUi(self, MainWindow_direnc):
        MainWindow_direnc.setObjectName("MainWindow_direnc")
        MainWindow_direnc.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow_direnc)
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
        self.label.setText("DİRENÇ")
        
        # Birinci Birim ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 200, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont("Arial", 11))
        self.comboBox.addItems(Conversions.keys())
        
        # İkinci Birim ComboBox
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 320, 200, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(QtGui.QFont("Arial", 11))
        self.comboBox_2.addItems(Conversions.keys())
        
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
        
        MainWindow_direnc.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_direnc)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_direnc.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_direnc)
        self.statusbar.setObjectName("statusbar")
        MainWindow_direnc.setStatusBar(self.statusbar)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.retranslateUi(MainWindow_direnc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_direnc)

        # Dönüştürme Butonu
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))  # Arial fontu ve yazı boyutu 11
        self.pushButton.clicked.connect(self.convert_resistance)
        
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

    def retranslateUi(self, MainWindow_direnc):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_direnc.setWindowTitle(_translate("MainWindow_direnc", "DİRENÇ"))
        
        

    def convert_resistance(self):
        from_unit = self.comboBox.currentText()
        to_unit = self.comboBox_2.currentText()
        input_value = float(self.lineEdit.text())

        from_value = Conversions[from_unit]
        to_value = Conversions[to_unit]

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
    MainWindow_direnc = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_direnc()
    ui.setupUi(MainWindow_direnc)
    MainWindow_direnc.show()
    sys.exit(app.exec_())
