import sys
from PyQt5 import QtCore, QtGui, QtWidgets

Conversions = (
    ('Gram(gr)', 1),
    ('Desigram(dg)', 0.1),
    ('Santigram(cg)', 0.01),
    ('Miligram(mg)', 0.001),
    ('Mikrogram(µg)', 0.000001),
    ('Dekagram(dak)', 10),
    ('Hektogram(hg)', 100),
    ('Kilogram(kg)', 1000),
    ('Kental(q)', 453.59237),
    ('Ton(t)', 1000000),
    ('Karat(kr)', 0.2),
    ('Ons(oz)', 28.349523125),
    ('Stone(st)', 6350.29318),
    ('Pound(lb)', 453.59237),
)

class Ui_MainWindow_agirlik(object):
    def setupUi(self, MainWindow_agirlik):
        MainWindow_agirlik.setObjectName("MainWindow_agirlik")
        MainWindow_agirlik.resize(600, 500)  # Sayfa boyutu 600x500 olarak ayarlandı
        self.centralwidget = QtWidgets.QWidget(MainWindow_agirlik)
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
        
        # Birinci Birim ComboBox
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 200, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont("Arial", 11))
        for unit, _ in Conversions:
            self.comboBox.addItem(unit)
        
        # İkinci Birim ComboBox
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 320, 200, 35))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(QtGui.QFont("Arial", 11))
        for unit, _ in Conversions:
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

        # Dönüştürme Butonu
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))  # Arial fontu ve yazı boyutu 11
        self.pushButton.clicked.connect(self.convert_weight)

        # Yer Değiştirme Butonları
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

        MainWindow_agirlik.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_agirlik)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))  # Menü çubuğu boyutu ayarlandı
        self.menubar.setObjectName("menubar")
        MainWindow_agirlik.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_agirlik)
        self.statusbar.setObjectName("statusbar")
        MainWindow_agirlik.setStatusBar(self.statusbar)
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.retranslateUi(MainWindow_agirlik)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_agirlik)

    def retranslateUi(self, MainWindow_agirlik):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_agirlik.setWindowTitle(_translate("MainWindow_agirlik", "AĞIRLIK"))
        self.label.setText(_translate("MainWindow_agirlik", "AĞIRLIK"))

    def convert_weight(self):
        from_unit = self.comboBox.currentText()
        to_unit = self.comboBox_2.currentText()
        input_value = float(self.lineEdit.text())

        from_value = next(item[1] for item in Conversions if item[0] == from_unit)
        to_value = next(item[1] for item in Conversions if item[0] == to_unit)

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
    MainWindow_agirlik = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_agirlik()
    ui.setupUi(MainWindow_agirlik)
    MainWindow_agirlik.show()
    sys.exit(app.exec_())
