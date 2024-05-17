from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import sys

class Ui_MainWindow_hakkinda(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(0,0,0);")  # Set background color as RGB(0,0,0)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 550, 400))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollContentWidget = QtWidgets.QWidget()
        self.scrollContentWidget.setGeometry(QtCore.QRect(0, 0, 700, 950))

        self.label = QtWidgets.QLabel(self.scrollContentWidget)
        self.label.setGeometry(QtCore.QRect(10, -30, 550, 980))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setText("\n                           Birim Çevirici Arayüz Uygulaması\n\n"
                           "  Birim Çevirici uygulaması, çeşitli birimleri dönüştürmek ve\n  karşılaştırmak için tasarlanmış kullanıcı dostu bir mobil\n  uygulamadır. Bu uygulama, pratik ve hızlı bir şekilde çeşitli ölçü\n  birimleri arasında geçiş yapmanıza olanak tanır. İşte bu\n  uygulamanın sunabileceği bazı özellikler:\n\n "
                           "  1. Kapsamlı Birim Seçenekleri: Uygulama, zaman, sıcaklık,\n  ağırlık, uzunluk, alan, enerji, direnç, akım ve frekans gibi\n  geniş bir birim yelpazesini kapsar. Kullanıcılar, ihtiyaçlarına\n  göre farklı ölçü birimleri arasında dönüşümler yapabilirler.\n\n"
                           "  2. Kullanıcı Dostu Arayüz: Uygulamanın arayüzü basit,\n  sezgisel ve kullanıcı dostudur. Birim seçimi ve dönüşüm\n  işlemleri kolayca gerçekleştirilebilir, böylece kullanıcılar hızlı\n  bir şekilde istedikleri sonuca ulaşabilirler.\n\n"
                           "  3. Hızlı Dönüşüm: Uygulama, anında dönüşüm sonuçları\n  sunar. Kullanıcılar, birimler arasında dönüşüm yapmak için\n  sadece giriş alanına değer girerler ve sonucu anında görürler.\n  Bu, pratik ve etkili bir kullanıcı deneyimi sağlar.\n\n"
                           "  4. Çevrimdışı Kullanım: Uygulama, internet bağlantısı\n  olmadan da kullanılabilir. Bu özellik, kullanıcıların her\n  zaman ve her yerde birim dönüşümleri yapmalarını sağlar.\n\n"
                           "  Bu birim çevirici uygulaması, günlük hayatta ve profesyonel\n  çalışmalarda çeşitli ölçü birimleriyle yapılan dönüşümleri\n  kolaylaştırır. Kullanıcılar, uygulama sayesinde pratik ve hızlı\n  bir şekilde birimler arasında geçiş yapabilir ve doğru\n  sonuçları elde edebilirler.\n\n\n\n"
                           "                              Projede Emeği Geçenler \n\n"
                           "  Ahmet Bilal Zengin            zzamcamjoe@gmail.com \n\n"
                           "  Eren Altınışık               2003220059.erenaltinisik@gmail.com\n\n"
                           "  Ömer Faruk Akbulak    2003220018.omerfarukakbulak@gmail.com")

        self.scrollArea.setWidget(self.scrollContentWidget)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 405, 61, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-image: url(logolar/return.png);")

        self.pushButton_github = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_github.setGeometry(QtCore.QRect(220, 405, 61, 61))
        self.pushButton_github.setObjectName("pushButton_github")
        self.pushButton_github.setStyleSheet("background-image: url(logolar/github.png);background-color: white; border-radius: 50%;")
        self.pushButton_github.clicked.connect(self.openGitHubPage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HAKKINDA"))
        self.pushButton.setText("")
        self.pushButton_github.setText("")

    def openGitHubPage(self):
        github_url = "https://github.com/EREN0059/BirimCeviriciArayuzu"  # Replace with your GitHub URL
        webbrowser.open(github_url)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_hakkinda()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
