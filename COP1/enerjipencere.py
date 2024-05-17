# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

Conversions = (
    ('Joule', 1),
    ('DekaJoule', 10),
    ('HektoJoule', 100),
    ('KiloJoule', 1000),
    ('MegaJoule', 1e6),
    ('GigaJoule', 1e9),
    ('DesiJoule', 0.1),
    ('SantiJoule', 0.01),
    ('MiliJoule', 0.001),
    ('MikroJoule', 1e-6),
    ('NanoJoule', 1e-9),
    ('Kalori', 4.184),
    ('KiloKalori', 4184),
    ('BeygirGücü Saat', 2.6845195376961728e+6),
    ('BTU', 1055.05585262),
    ('Elektron Volt', 1.602176634e-19),
    ('Erg', 1e-7),
    ('KiloWatt Saat', 3.6e+6)
)


class Ui_MainWindow_enerji(object):
    def setupUi(self, MainWindow_enerji):
        MainWindow_enerji.setObjectName("MainWindow_enerji")
        MainWindow_enerji.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow_enerji)
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
        self.label.setText("ENERJİ")
        
        # Birinci Birim ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 200, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont("Arial", 11))
        for unit, _ in Conversions:
            self.comboBox.addItem(unit)
        
        # İkinci Birim ComboBox
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 320, 200, 35))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setFont(QtGui.QFont("Arial", 11))
        for unit, _ in Conversions:
            self.comboBox_3.addItem(unit)
        
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
        
        MainWindow_enerji.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_enerji)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_enerji.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_enerji)
        self.statusbar.setObjectName("statusbar")
        MainWindow_enerji.setStatusBar(self.statusbar)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.retranslateUi(MainWindow_enerji)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_enerji)

        # Dönüştürme Butonu
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))  # Arial fontu ve yazı boyutu 11
        self.pushButton.clicked.connect(self.convert_energy)
        
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

    def retranslateUi(self, MainWindow_enerji):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_enerji.setWindowTitle(_translate("MainWindow_enerji", "ENERJİ"))

    def convert_energy(self):
        from_unit = self.comboBox.currentText()
        to_unit = self.comboBox_3.currentText()
        input_value = float(self.lineEdit.text())

        from_value = next(item[1] for item in Conversions if item[0] == from_unit)
        to_value = next(item[1] for item in Conversions if item[0] == to_unit)

        result = input_value * from_value / to_value
        formatted_result = '{:.12f}'.format(result)
        self.lineEdit_2.setText(str(result))
        
    def swap_values(self):
        temp = self.lineEdit.text()
        self.lineEdit.setText(self.lineEdit_2.text())
        self.lineEdit_2.setText(temp)
        
    def swap_units(self):
        temp = self.comboBox.currentIndex()
        self.comboBox.setCurrentIndex(self.comboBox_3.currentIndex())
        self.comboBox_3.setCurrentIndex(temp)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_enerji = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_enerji()
    ui.setupUi(MainWindow_enerji)
    MainWindow_enerji.show()
    sys.exit(app.exec_())
