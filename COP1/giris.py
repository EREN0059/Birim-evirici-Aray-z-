from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow_CIKIS(object):
    def setupUi(self, MainWindow_CIKIS):
        MainWindow_CIKIS.setObjectName("MainWindow_CIKIS")
        MainWindow_CIKIS.resize(462, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow_CIKIS)
        self.centralwidget.setObjectName("centralwidget")

        # QLabel ekleyerek arka plana GIF ekleme
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 462, 418))
        self.background_label.setObjectName("background_label")
        self.movie = QtGui.QMovie("logolar/15.gif")  # Gif dosyanızın yolunu buraya ekleyin
        self.background_label.setMovie(self.movie)
        self.movie.start()

        self.pushButton_giris = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_giris.setGeometry(QtCore.QRect(70, 35, 320, 180))
        self.pushButton_giris.setObjectName("pushButton_giris")
        self.pushButton_giris.setStyleSheet("background-image: url(logolar/giris5.png);background-color: white;")
        self.pushButton_HAKKINDA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_HAKKINDA.setGeometry(QtCore.QRect(40, 280, 101, 101))
        self.pushButton_HAKKINDA.setObjectName("pushButton_HAKKINDA")
        self.pushButton_HAKKINDA.setStyleSheet("background-image: url(logolar/about.png);background-color: white; border-radius: 50%;")
        self.pushButton_3 = RandomMoveButton(self.centralwidget)  # RandomMoveButton sınıfından bir nesne oluşturuyoruz
        self.pushButton_3.setGeometry(QtCore.QRect(320, 280, 101, 101))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-image: url(logolar/cikis.png);background-color: white; border-radius: 50%;")       
        MainWindow_CIKIS.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow_CIKIS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_CIKIS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_CIKIS)
        self.statusbar.setObjectName("statusbar")
        MainWindow_CIKIS.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_CIKIS)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_CIKIS)

    def retranslateUi(self, MainWindow_CIKIS):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_CIKIS.setWindowTitle(_translate("MainWindow_CIKIS", "BİRİM ÇEVİRİCİ"))
        self.pushButton_giris.setText(_translate("MainWindow_CIKIS", ""))
        self.pushButton_HAKKINDA.setText(_translate("MainWindow_CIKIS", ""))
        self.pushButton_3.setText(_translate("MainWindow_CIKIS", ""))

        MainWindow_CIKIS.setStyleSheet("background-color: rgba(0, 0, 0, 0);")  # Arka plan rengini sıfıra ayarlıyoruz

class RandomMoveButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(RandomMoveButton, self).__init__(parent)
        self.setGeometry(parent.rect())  # Ana pencerenin boyutlarına uygun olarak yerleştirilir
        self.moveRandomly()  # Buton oluşturulduğunda hemen rastgele bir konuma yerleştirilir

    def enterEvent(self, event):
        self.moveRandomly()  # Fare butonun üzerine geldiğinde rastgele bir konuma hareket ettirilir

    def moveRandomly(self):
        parent_rect = self.parent().rect()
        button_rect = self.rect()
        max_x = parent_rect.width() - button_rect.width()
        max_y = parent_rect.height() - button_rect.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.move(new_x, new_y)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_CIKIS = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_CIKIS()
    ui.setupUi(MainWindow_CIKIS)
    MainWindow_CIKIS.show()
    sys.exit(app.exec_())
