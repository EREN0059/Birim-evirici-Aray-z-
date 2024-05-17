from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_GIRIS(object):
    def setupUi(self, MainWindow_GIRIS):
        MainWindow_GIRIS.setObjectName("MainWindow_GIRIS")
        MainWindow_GIRIS.resize(463, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow_GIRIS)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_GIRISS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GIRISS.setGeometry(QtCore.QRect(150, 30, 161, 161))
        self.pushButton_GIRISS.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Users\Eren\OneDrive\Masaüstü\COP\sand-clock-icon-hourglass-simple-flat-vector-38155817.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_GIRISS.setIcon(icon)
        self.pushButton_GIRISS.setIconSize(QtCore.QSize(200, 200))
        self.pushButton_GIRISS.setObjectName("pushButton_GIRISS")
        self.pushButton_CIKIS = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CIKIS.setGeometry(QtCore.QRect(20, 240, 111, 111))
        self.pushButton_CIKIS.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../png-transparent-emergency-exit-output-device-computer-icons-business-end-angle-image-file-formats-company.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_CIKIS.setIcon(icon1)
        self.pushButton_CIKIS.setIconSize(QtCore.QSize(105, 105))
        self.pushButton_CIKIS.setObjectName("pushButton_CIKIS")
        self.pushButton_HAKKINDA = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_HAKKINDA.setGeometry(QtCore.QRect(340, 240, 111, 111))
        self.pushButton_HAKKINDA.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../png-transparent-computer-icons-information-about-icon-game-text-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_HAKKINDA.setIcon(icon2)
        self.pushButton_HAKKINDA.setIconSize(QtCore.QSize(105, 105))
        self.pushButton_HAKKINDA.setCheckable(False)
        self.pushButton_HAKKINDA.setObjectName("pushButton_HAKKINDA")
        MainWindow_GIRIS.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_GIRIS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 26))
        self.menubar.setObjectName("menubar")
        MainWindow_GIRIS.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_GIRIS)
        self.statusbar.setObjectName("statusbar")
        MainWindow_GIRIS.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_GIRIS)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_GIRIS)

    def retranslateUi(self, MainWindow_GIRIS):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_GIRIS.setWindowTitle(_translate("MainWindow_GIRIS", "BİRİM DÖNÜŞTÜRÜCÜ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_GIRIS = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_GIRIS()
    ui.setupUi(MainWindow_GIRIS)
    MainWindow_GIRIS.show()
    sys.exit(app.exec_())
