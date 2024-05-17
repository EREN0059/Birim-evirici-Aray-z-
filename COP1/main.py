from PyQt5.QtWidgets import QApplication
from login import Girispage

app = QApplication([])
pencere = Girispage()
pencere.show()
app.exec_()

