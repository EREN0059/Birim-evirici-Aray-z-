from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindows_sicaklik(object):
    def setupUi(self, MainWindows_sicaklik):
        MainWindows_sicaklik.setObjectName("MainWindows_sicaklik")
        MainWindows_sicaklik.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindows_sicaklik)
        self.centralwidget.setObjectName("centralwidget")
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 200, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont("Arial", 11))
        
        self.comboBox.addItems(["Celsius", "Kelvin", "Fahrenheit", "Rankine", "Reaumur"])
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(320, 130, 250, 35))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(QtGui.QFont("Arial", 11))
        self.lineEdit_3.setPlaceholderText("Değer giriniz")
        self.lineEdit_3.setStyleSheet("border-radius: 4px;")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 320, 200, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(QtGui.QFont("Arial", 11))
        self.comboBox_2.addItems(["Celsius", "Kelvin", "Fahrenheit", "Rankine", "Reaumur"])
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 320, 250, 35))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(QtGui.QFont("Arial", 11))
        self.lineEdit_4.setPlaceholderText("Sonuç")
        self.lineEdit_4.setStyleSheet("border-radius: 4px;")
        MainWindows_sicaklik.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindows_sicaklik)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        MainWindows_sicaklik.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindows_sicaklik)
        self.statusbar.setObjectName("statusbar")
        MainWindows_sicaklik.setStatusBar(self.statusbar)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))  # Dönüştür butonunun fontu Arial ve boyutu 11 oldu
        self.pushButton.clicked.connect(self.convert_temperature)
        self.pushButton.clicked.connect(self.button_clicked)
        
        self.swapValuesButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapValuesButton.setGeometry(QtCore.QRect(405, 205, 75, 75))
        self.swapValuesButton.setObjectName("swapValuesButton")
        self.swapValuesButton.setText("")
        self.swapValuesButton.clicked.connect(self.swap_values)
        self.swapValuesButton.setStyleSheet("background-image: url(logolar/degistir.png);background-color: white; ")


        self.swapUnitsButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapUnitsButton.setGeometry(QtCore.QRect(80, 205, 75, 75))
        self.swapUnitsButton.setObjectName("swapUnitsButton")
        self.swapUnitsButton.setText("")
        self.swapUnitsButton.clicked.connect(self.swap_units)
        self.swapUnitsButton.setStyleSheet("background-image: url(logolar/degistir.png); background-color: white;")

        self.retranslateUi(MainWindows_sicaklik)
        QtCore.QMetaObject.connectSlotsByName(MainWindows_sicaklik)

    def retranslateUi(self, MainWindows_sicaklik):
        _translate = QtCore.QCoreApplication.translate
        MainWindows_sicaklik.setWindowTitle(_translate("MainWindows_sicaklik", "SICAKLIK"))
        self.label.setText(_translate("MainWindows_sicaklik", "SICAKLIK"))


    def convert_temperature(self):
        from_unit = self.comboBox.currentText()
        to_unit = self.comboBox_2.currentText()
        input_value = float(self.lineEdit_3.text())

        if from_unit == "Celsius":
            if to_unit == "Celsius":
                result = input_value
            elif to_unit == "Kelvin":
                result = input_value + 273.15
            elif to_unit == "Fahrenheit":
                result = input_value * 9/5 + 32
            elif to_unit == "Rankine":
                result = (input_value + 273.15) * 9/5
            elif to_unit == "Reaumur":
                result = input_value * 4/5
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                result = input_value - 273.15
            elif to_unit == "Kelvin":
                result = input_value
            elif to_unit == "Fahrenheit":
                result = input_value * 9/5 - 459.67
            elif to_unit == "Rankine":
                result = input_value * 9/5
            elif to_unit == "Reaumur":
                result = (input_value - 273.15) * 4/5
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                result = (input_value - 32) * 5/9
            elif to_unit == "Kelvin":
                result = (input_value + 459.67) * 5/9
            elif to_unit == "Fahrenheit":
                result = input_value
            elif to_unit == "Rankine":
                result = input_value + 459.67
            elif to_unit == "Reaumur":
                result = (input_value - 32) * 4/9
        elif from_unit == "Rankine":
            if to_unit == "Celsius":
                result = (input_value - 491.67) * 5/9
            elif to_unit == "Kelvin":
                result = input_value * 5/9
            elif to_unit == "Fahrenheit":
                result = input_value - 459.67
            elif to_unit == "Rankine":
                result = input_value
            elif to_unit == "Reaumur":
                result = (input_value - 491.67) * 4/9
        elif from_unit == "Reaumur":
            if to_unit == "Celsius":
                result = input_value * 5/4
            elif to_unit == "Kelvin":
                result = input_value * 5/4 + 273.15
            elif to_unit == "Fahrenheit":
                result = input_value * 9/4 + 32
            elif to_unit == "Rankine":
                result = (input_value * 5/4 + 273.15) * 9/5
            elif to_unit == "Reaumur":
                result = input_value

        self.lineEdit_4.setText(str(result))
        
    def swap_values(self):
        temp = self.lineEdit_3.text()
        self.lineEdit_3.setText(self.lineEdit_4.text())
        self.lineEdit_4.setText(temp)

    def swap_units(self):
        temp = self.comboBox.currentIndex()
        self.comboBox.setCurrentIndex(self.comboBox_2.currentIndex())
        self.comboBox_2.setCurrentIndex(temp)
    
    def button_clicked(self):
        self.pushButton.setStyleSheet("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindows_sicaklik = QtWidgets.QMainWindow()
    ui = Ui_MainWindows_sicaklik()
    ui.setupUi(MainWindows_sicaklik)
    MainWindows_sicaklik.show()
    sys.exit(app.exec_())
