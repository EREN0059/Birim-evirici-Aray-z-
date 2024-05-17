import sys
from PyQt5 import QtCore, QtGui, QtWidgets

Conversions = (
    ('Hertz (Hz)', 1),
    ('Terahertz (THz)', 1e12),
    ('Gigahertz (GHz)', 1e9),
    ('Megahertz (MHz)', 1e6),
    ('Kilohertz (kHz)', 1e3),
    ('Hectohertz (hHz)', 1e2),
    ('Dekahertz (daHz)', 1e1),
    ('Decihertz (dHz)', 1e-1),
    ('Centihertz (cHz)', 1e-2),
    ('Milihertz (mHz)', 1e-3),
    ('Microhertz (µHz)', 1e-6),
    ('Terametre Cinsinden Dalga Boyu ', 3335.64095198152),
    ('Gigametre Cinsinden Dalga Boyu ', 3.335640951981521),
    ('Megametre Cinsinden Dalga Boyu ', 0.0033356409519815205),
    ('Kilometre Cinsinden Dalga Boyu ', 3.3356409519815205e-06),
    ('Hektometre Cinsinden Dalga Boyu ', 3.3356409519815204e-07),
    ('Dekametre Cinsinden Dalga Boyu ', 3.3356409519815205e-08),
    ('Metre Cinsinden Dalga Boyu ', 3.3356409519815204e-09),
    ('Santimetre Cinsinden Dalga Boyu ', 3.3356409519815207e-10),
    ('Milimetre Cinsinden Dalga Boyu ', 3.33564095198152e-11),
    ('Mikrometre Cinsinden Dalga Boyu ', 3.3356409519815203e-12),
    ('Nanometre Cinsinden Dalga Boyu ', 0.0033356409519815205),
    ('Elektron Compton Dalga Boyu ', 8.093300932874052e-21),
    ('Proton Compton Dalga Boyu ', 4.407749377071106e-24),
    ('Nötron Compton Dalga Boyu ', 4.4016821130299884e-24)
)


class Ui_MainWindow_frekans(object):
    def setupUi(self, MainWindow_frekans):
        MainWindow_frekans.setObjectName("MainWindow_frekans")
        MainWindow_frekans.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow_frekans)
        self.centralwidget.setObjectName("centralwidget")
        
        # Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 321, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: #737373;")  # Rengi ayarlandı
        self.label.setText("FREKANS")
        
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
        
        MainWindow_frekans.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_frekans)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_frekans.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_frekans)
        self.statusbar.setObjectName("statusbar")
        MainWindow_frekans.setStatusBar(self.statusbar)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.retranslateUi(MainWindow_frekans)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_frekans)

        # Dönüştürme Butonu
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))  # Arial fontu ve yazı boyutu 11
        self.pushButton.clicked.connect(self.convert_frequency)
        
        # Değiştirme Butonları
        self.swapValuesButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapValuesButton.setGeometry(QtCore.QRect(405, 205, 75, 75))
        self.swapValuesButton.setObjectName("swapValuesButton")
        self.swapValuesButton.setText("")
        self.swapValuesButton.clicked.connect(self.swap_values)
        self.swapValuesButton.setStyleSheet("background-image: url(logolar/degistir.png); background-color: white;")
        
        self.swapUnitsButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapUnitsButton.setGeometry(QtCore.QRect(95, 205, 75, 75))
        self.swapUnitsButton.setObjectName("swapUnitsButton")
        self.swapUnitsButton.setText("")
        self.swapUnitsButton.clicked.connect(self.swap_units)
        self.swapUnitsButton.setStyleSheet("background-image: url(logolar/degistir.png); background-color: white;")

    def retranslateUi(self, MainWindow_frekans):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_frekans.setWindowTitle(_translate("MainWindow_frekans", "FREKANS"))

    def convert_frequency(self):
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
    MainWindow_frekans = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_frekans()
    ui.setupUi(MainWindow_frekans)
    MainWindow_frekans.show()
    sys.exit(app.exec_())
