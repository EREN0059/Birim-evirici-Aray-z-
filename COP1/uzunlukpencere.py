import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_uzunluk(object):
    def setupUi(self, MainWindow_uzunluk):
        MainWindow_uzunluk.setObjectName("MainWindow_uzunluk")
        MainWindow_uzunluk.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow_uzunluk)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 40, 321, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("UZUNLUK")
        self.label.setStyleSheet("color: #737373;")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 130, 200, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont("Arial", 11))
        self.comboBox.addItems(["Petametre(Pm)", "Terametre(Tm)", "Gigametre(Gm)", "Megametre(Mm)", "Kilometre(Km)", 
                                "Hektometre(Hm)", "Dekametre(Dam)", "Metre(m)", "Desimetre(dm)", "Santimetre(cm)",
                                "Milimetre(mm)", "Mikrometre(µm)", "Nanometre(nm)", "Pikometre(pm)", "Pika(pc)",
                                "Mil(mi)", "Yarda(yd)", "Feet(ft)", "İnç(in)", "Punto(pt)"])
        
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
        self.comboBox_2.addItems(["Petametre(Pm)", "Terametre(Tm)", "Gigametre(Gm)", "Megametre(Mm)", "Kilometre(Km)", 
                                "Hektometre(Hm)", "Dekametre(Dam)", "Metre(m)", "Desimetre(dm)", "Santimetre(cm)",
                                "Milimetre(mm)", "Mikrometre(µm)", "Nanometre(nm)", "Pikometre(pm)", "Pika(pc)",
                                "Mil(mi)", "Yarda(yd)", "Feet(ft)", "İnç(in)", "Punto(pt)"])
        
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(320, 320, 250, 35))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(QtGui.QFont("Arial", 11))
        self.lineEdit_4.setPlaceholderText("Sonuç")
        self.lineEdit_4.setStyleSheet("border-radius: 4px;")
        
        MainWindow_uzunluk.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_uzunluk)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_uzunluk.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_uzunluk)
        self.statusbar.setObjectName("statusbar")
        MainWindow_uzunluk.setStatusBar(self.statusbar)
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(415, 390, 60, 60))
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-image: url(logolar/return.png);")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 390, 100, 60))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Dönüştür")
        self.pushButton.setFont(QtGui.QFont("Arial", 11))
        self.pushButton.clicked.connect(self.convert_length)
        
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

    def retranslateUi(self, MainWindow_uzunluk):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_uzunluk.setWindowTitle(_translate("MainWindow_uzunluk", "UZUNLUK"))

    def convert_length(self):
        units = {
            "Petametre(Pm)": 1e15, "Terametre(Tm)": 1e12, "Gigametre(Gm)": 1e9, "Megametre(Mm)": 1e6,
            "Kilometre(Km)": 1e3, "Hektometre(Hm)": 1e2, "Dekametre(Dam)": 1e1, "Metre(m)": 1.0,
            "Desimetre(dm)": 1e-1, "Santimetre(cm)": 1e-2, "Milimetre(mm)": 1e-3, "Mikrometre(µm)": 1e-6,
            "Nanometre(nm)": 1e-9, "Pikometre(pm)": 1e-12, "Pika(pc)": 3.086e16, "Mil(mi)": 1609.344,
            "Yarda(yd)": 0.9144, "Feet(ft)": 0.3048, "İnç(in)": 0.0254, "Punto(pt)": 3.514598e-5
        }

        from_unit = self.comboBox.currentText()
        to_unit = self.comboBox_2.currentText()
        input_value = float(self.lineEdit_3.text())

        from_value = units[from_unit]
        to_value = units[to_unit]

        result = input_value * from_value / to_value
        self.lineEdit_4.setText(str(result))
    
    def swap_values(self):
        temp = self.lineEdit_3.text()
        self.lineEdit_3.setText(self.lineEdit_4.text())
        self.lineEdit_4.setText(temp)
        
    def swap_units(self):
        temp = self.comboBox.currentIndex()
        self.comboBox.setCurrentIndex(self.comboBox_2.currentIndex())
        self.comboBox_2.setCurrentIndex(temp)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_uzunluk = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_uzunluk()
    ui.setupUi(MainWindow_uzunluk)
    MainWindow_uzunluk.show()
    sys.exit(app.exec_())
