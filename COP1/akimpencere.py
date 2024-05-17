import sys
from PyQt5 import QtCore, QtGui, QtWidgets

Conversions = {
    "Amper(A)": 1,
    "Miliamper(mA)": 0.001,
    "Mikroamper(µA)": 1e-6,
    "Nanoamper(nA)": 1e-9,
    "Kiloamper(kA)": 1000,
    "Megaamper(MA)": 1e6,
    "Gigaamper(GA)": 1e9,
    "Coulomb/Saniye(C/s)": 1,
    "Biot": 10,
    "Elektromanyetik Akım Birimi": 10,
    "Elektrostatik Akım Birimi": 0.000000000333564,
    "Franklin/Saniye": 0.000000000333564,
    "Gauss Elektrik Akımı":  0.000000000333564,
    "Gilbert": 0.79577471999735,
    "Siemens Volt": 1,
    "Volt/Ohm": 1,
    "Watt/Ohm": 1,
    "Weber/Henry": 1
}

class Ui_MainWindow_akim(object):
    def setupUi(self, MainWindow_akim):
        MainWindow_akim.setObjectName("MainWindow_akim")
        MainWindow_akim.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow_akim)
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
        self.label.setText("AKIM")
        
        # Birinci Birim ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 200, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont("Arial", 11))
        for unit in Conversions.keys():
            self.comboBox.addItem(unit)
        
        # İkinci Birim ComboBox
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 320, 200, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(QtGui.QFont("Arial", 11))
        for unit in Conversions.keys():
            self.comboBox_2.addItem(unit)
        
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
        
        MainWindow_akim.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_akim)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_akim.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_akim)
        self.statusbar.setObjectName("statusbar")
        MainWindow_akim.setStatusBar(self.statusbar)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))  # Arial fontu ve yazı boyutu 11
        self.pushButton.clicked.connect(self.convert_current)

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

        self.retranslateUi(MainWindow_akim)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_akim)

    def retranslateUi(self, MainWindow_akim):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_akim.setWindowTitle(_translate("MainWindow_akim", "AKIM"))

    def convert_current(self):
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
    MainWindow_akim = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_akim()
    ui.setupUi(MainWindow_akim)
    MainWindow_akim.show()
    sys.exit(app.exec_())
