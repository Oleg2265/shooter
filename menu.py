import PyQt5
from main import *
from Every_enemy import *
from Character import *
from PyQt5 import *
from PyQt5.QtWidgets import *


app = QApplication([])
Shop = QWidget()
Shop.resize(500,500)
Shop.hide()


window = QWidget()
window.resize(700,500)
window.show()

Play = QPushButton("Грати")
shop = QPushButton("МАГАЗИН")
nadpys = QLabel("Тут нічого немає")
H1 = QHBoxLayout()
H1.addWidget(Play)
H1.addWidget(shop)

kaka1 = QHBoxLayout()
kaka1.addWidget(nadpys)



def magazin():
    Shop.show()





Play.clicked.connect(my_mega_game)
shop.clicked.connect(magazin)
Shop.setLayout(kaka1)
window.setLayout(H1)
app.exec()

