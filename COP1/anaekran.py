from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow_ilkekran(object):
    def setupUi(self, MainWindow_ilkekran):
        MainWindow_ilkekran.setObjectName("MainWindow_ilkekran")
        MainWindow_ilkekran.resize(690, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow_ilkekran)
        self.centralwidget.setObjectName("centralwidget")
        
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 690, 714))
        self.background_label.setObjectName("background_label")
        self.movie = QtGui.QMovie("logolar/16.gif")  # Gif dosyanızın yolunu buraya ekleyin
        self.background_label.setMovie(self.movie)
        self.movie.start()

        self.pushButton_SICAKLIK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_SICAKLIK.setGeometry(QtCore.QRect(280, 140, 120, 120))
        self.pushButton_SICAKLIK.setObjectName("pushButton_SICAKLIK")
        self.pushButton_SICAKLIK.setStyleSheet("background-image: url(logolar/sicaklik.png);background-color: white;")
        self.pushButton_ZAMAN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ZAMAN.setGeometry(QtCore.QRect(60, 140, 120, 120))
        self.pushButton_ZAMAN.setObjectName("pushButton_ZAMAN")
        self.pushButton_ZAMAN.setStyleSheet("background-image: url(logolar/zaman.png);background-color: white;")
        self.pushButton_AGIRLIK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AGIRLIK.setGeometry(QtCore.QRect(500, 140, 120, 120))
        self.pushButton_AGIRLIK.setObjectName("pushButton_AGIRLIK")
        self.pushButton_AGIRLIK.setStyleSheet("background-image: url(logolar/agirlik.png);background-color: white;")
        self.pushButton_UZUNLUK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_UZUNLUK.setGeometry(QtCore.QRect(60, 280, 120, 120))
        self.pushButton_UZUNLUK.setObjectName("pushButton_UZUNLUK")
        self.pushButton_UZUNLUK.setStyleSheet("background-image: url(logolar/uzunluk.png);background-color: white;")
        self.pushButton_ALAN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ALAN.setGeometry(QtCore.QRect(280, 280, 120, 120))
        self.pushButton_ALAN.setObjectName("pushButton_ALAN")
        self.pushButton_ALAN.setStyleSheet("background-image: url(logolar/alan.png);background-color: white;")
        self.pushButton_ENERJI = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ENERJI.setGeometry(QtCore.QRect(500, 280, 120, 120))
        self.pushButton_ENERJI.setObjectName("pushButton_ENERJI")
        self.pushButton_ENERJI.setStyleSheet("background-image: url(logolar/enerji.png);background-color: white;")
        self.pushButton_DIRENC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DIRENC.setGeometry(QtCore.QRect(60, 420, 120, 120))
        self.pushButton_DIRENC.setObjectName("pushButton_DIRENC")
        self.pushButton_DIRENC.setStyleSheet("background-image: url(logolar/direnc.png); background-color: white;")
        self.pushButton_AKIM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AKIM.setGeometry(QtCore.QRect(280, 420, 120, 120))
        self.pushButton_AKIM.setObjectName("pushButton_AKIM")
        self.pushButton_AKIM.setStyleSheet("background-image: url(logolar/akim.png);background-color: white;")
        self.pushButton_FREKANS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_FREKANS.setGeometry(QtCore.QRect(500, 420, 120, 120))
        self.pushButton_FREKANS.setObjectName("pushButton_FREKANS")
        self.pushButton_FREKANS.setStyleSheet("background-image: url(logolar/frekansdalga.png);background-color: white;")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_GERIDON = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GERIDON.setGeometry(QtCore.QRect(280, 560, 120, 120))
        self.pushButton_GERIDON.setObjectName("pushButton_GERIDON")
        self.pushButton_GERIDON.setStyleSheet("background-image: url(logolar/as.png);background-color: white;")
        
        MainWindow_ilkekran.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_ilkekran)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_ilkekran.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_ilkekran)
        self.statusbar.setObjectName("statusbar")
        MainWindow_ilkekran.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_ilkekran)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_ilkekran)

        # Ana ekranın arka plan rengini değiştirme
        MainWindow_ilkekran.setStyleSheet("background-color: rgba(0,0,0,0);")  # RGB formatı
        
    def retranslateUi(self, MainWindow_ilkekran):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_ilkekran.setWindowTitle(_translate("MainWindow_ilkekran", "BİRİM ÇEVİRİCİ"))
        self.pushButton_SICAKLIK.setText("")
        self.pushButton_ZAMAN.setText("")
        self.pushButton_AGIRLIK.setText("")
        self.pushButton_UZUNLUK.setText("")
        self.pushButton_ALAN.setText("")
        self.pushButton_ENERJI.setText("")
        self.pushButton_DIRENC.setText("")
        self.pushButton_AKIM.setText("")
        self.pushButton_FREKANS.setText("")
        self.label.setText("")
        self.pushButton_GERIDON.setText("")
        

        # Yeni QLabel ekleme
        self.label_SICAKLIK = QtWidgets.QLabel(self.centralwidget)
        self.label_SICAKLIK.setGeometry(QtCore.QRect(215, 45, 280, 60))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_SICAKLIK.setFont(font)
        self.label_SICAKLIK.setStyleSheet("color: white;")
        self.label_SICAKLIK.setObjectName("label_SICAKLIK")
        self.label_SICAKLIK.setText(_translate("MainWindow_ilkekran", "BİRİMLER"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_ilkekran = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_ilkekran()
    ui.setupUi(MainWindow_ilkekran)
    MainWindow_ilkekran.show()
    sys.exit(app.exec_())