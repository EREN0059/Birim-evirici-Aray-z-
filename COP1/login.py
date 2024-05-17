import os
from PyQt5.QtWidgets import *
from anaekran import *
from zamanpencere import *
from agirlikpencere import *
from sicaklikpencere import *
from uzunlukpencere import *
from alanpencere import *
from frekanspencere import *
from enerjipencere import *
from akimpencere import *
from direncpencere import *
from giris import *
from hak import *

class Girispage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gir = Ui_MainWindow_CIKIS()
        self.gir.setupUi(self)
        self.gir.pushButton_giris.clicked.connect(self.birimcevirici)
        self.gir.pushButton_3.clicked.connect(self.cikis)
        self.gir.pushButton_HAKKINDA.clicked.connect(self.hakkinda)

    def hakkinda(self):
        self.close()
        self.hakkindaac = hakkindapage()
        self.hakkindaac.show()    

    def cikis(self):
        self.close()

    def birimcevirici(self):
        self.close()
        self.birim_cevirici = LoginPage()
        self.birim_cevirici.show()


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.loginanaekran = Ui_MainWindow_ilkekran()
        self.loginanaekran.setupUi(self)
        self.loginanaekran.pushButton_ZAMAN.clicked.connect(self.zamansayfasi)
        self.loginanaekran.pushButton_AGIRLIK.clicked.connect(self.agirliksayfasi)
        self.loginanaekran.pushButton_SICAKLIK.clicked.connect(self.sicakliksayfasi)
        self.loginanaekran.pushButton_UZUNLUK.clicked.connect(self.uzunluksayfasi)
        self.loginanaekran.pushButton_ALAN.clicked.connect(self.alansayfasi)
        self.loginanaekran.pushButton_FREKANS.clicked.connect(self.frekanssayfasi)
        self.loginanaekran.pushButton_ENERJI.clicked.connect(self.enerjisayfasi)
        self.loginanaekran.pushButton_AKIM.clicked.connect(self.akimsayfasi)
        self.loginanaekran.pushButton_DIRENC.clicked.connect(self.direncsayfasi)

        self.loginanaekran.pushButton_GERIDON.clicked.connect(self.geridon)

    def geridon(self):
        self.close()
        self.geridon = Girispage()
        self.geridon.show()

    def zamansayfasi(self):
        self.close()
        self.zamanac = zamanpage()
        self.zamanac.show()

    def agirliksayfasi(self):
        self.close()
        self.agirlikac = agirlikpage()
        self.agirlikac.show()

    def sicakliksayfasi(self):
        self.close()
        self.sicaklikac = sicaklikpage()
        self.sicaklikac.show()

    def uzunluksayfasi(self):
        self.close()
        self.uzunlukac = uzunlukpage()
        self.uzunlukac.show()

    def alansayfasi(self):
        self.close()
        self.alanac = alanpage()
        self.alanac.show()

    def frekanssayfasi(self):
        self.close()
        self.frekansac = frekanspage()
        self.frekansac.show()

    def enerjisayfasi(self):
        self.close()
        self.enerjicac = enerjipage()
        self.enerjicac.show()

    def akimsayfasi(self):
        self.close()
        self.akimac = akimpage()
        self.akimac.show()

    def direncsayfasi(self):
        self.close()
        self.direncac = direncpage()
        self.direncac.show()
        

class hakkindapage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hakkindagir = Ui_MainWindow_hakkinda()
        self.hakkindagir.setupUi(self)
        self.hakkindagir.pushButton.clicked.connect(self.cikis)
    
    def cikis(self):
        self.close()
        self.girisac = Girispage()
        self.girisac.show()

class frekanspage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.frekansgir = Ui_MainWindow_frekans()
        self.frekansgir.setupUi(self)        
        self.frekansgir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()    

class direncpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.direncgir = Ui_MainWindow_direnc()
        self.direncgir.setupUi(self)        
        self.direncgir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show() 

class sicaklikpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sicaklikgir = Ui_MainWindows_sicaklik()
        self.sicaklikgir.setupUi(self)        
        self.sicaklikgir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()      

class zamanpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.zamangir = Ui_MainWindow_zaman()
        self.zamangir.setupUi(self)        
        self.zamangir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()      

class agirlikpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.agirlikgir = Ui_MainWindow_agirlik()
        self.agirlikgir.setupUi(self)        
        self.agirlikgir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()  

class direncpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.direncgir = Ui_MainWindow_direnc()
        self.direncgir.setupUi(self)        
        self.direncgir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show() 

class uzunlukpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uzunlukgir = Ui_MainWindow_uzunluk()
        self.uzunlukgir.setupUi(self)        
        self.uzunlukgir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()      

class alanpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.alangir = Ui_MainWindow_alan()
        self.alangir.setupUi(self)        
        self.alangir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()

class enerjipage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.enerjigir = Ui_MainWindow_enerji()
        self.enerjigir.setupUi(self)        
        self.enerjigir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()        

class akimpage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.akimgir = Ui_MainWindow_akim()
        self.akimgir.setupUi(self)        
        self.akimgir.pushButton1.clicked.connect(self.cikis)

    def cikis(self):
        self.close()
        self.girisac = LoginPage()
        self.girisac.show()                                                        


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow_CIKIS = QMainWindow()
    ui = Ui_MainWindow_CIKIS()
    ui.setupUi(MainWindow_CIKIS)
    MainWindow_CIKIS.show()
    sys.exit(app.exec_())
