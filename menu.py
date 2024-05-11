import json

import PyQt5
from PyQt5.QtGui import QPixmap

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
window.resize(200,100)
window.show()



settings = {}
def read_data():
    global settings
    try:
        with open("settings.json", "r", encoding="utf-8") as file:
            settings = json.load(file)
    except:
        settings ={
                "skin": "img.png",
                "money": 0,
                "player_skin": "img.png"
            }
def write_data():
    global settings
    with open("settings.json", "w", encoding="utf-8") as file:
        json.dump(settings, file, indent=4)



def buy_skin1():
    read_data()
    if settings['money'] >= 7:
        settings['money'] -= 7
        settings['skin'] = "img_png"
        write_data()
    else:
        print("Грошей не хватає")
    write_data()

def buy_skin2():
    read_data()
    if settings['money'] >= 8:
        settings['money'] -= 8
        settings['skin'] = "img1_png"
        write_data()
    else:
        print("Грошей не хватає")

def buy_skin3():
    read_data()
    if settings['money'] >= 10:
        settings['money'] -= 10
        settings['player_skin'] = "img2_png"
        write_data()
    else:
        print("Грошей не хватає")

def buy_skin4():
    read_data()
    if settings['money'] >= 12:
        settings['money'] -= 12
        settings['player_skin'] = "img3_png"
        write_data()
    else:
        print("Грошей не хватає")













Play = QPushButton("Грати")
shop = QPushButton("МАГАЗИН")
nadpys = QLabel("Тут нічого немає")
skin1 = QLabel('НАдпис')
skin1_image = QPixmap("img.png")
skin1_image = skin1_image.scaledToHeight(200)
skin1.setPixmap(skin1_image)









choose_skin1 = QPushButton("Купити скін:коштує !7!")
choose_skin2 = QPushButton("Купити скін:коштує !9!")
choose_skin3 = QPushButton("Купити скін:коштує !10!")
choose_skin4 = QPushButton("Купити скін:коштує !11!")



choose_skin1.clicked.connect(buy_skin1)




#Задній фон

#back_g = QLabel("Задній_фон")
#back_image = QPixmap("back_Lo.png")
#back_image = back_image.scaledToHeight(500)
#back_g.setPixmap(back_image)







skin2 = QLabel('НАдпис')
skin2_image = QPixmap("img_1.png")
skin2_image = skin2_image.scaledToHeight(180)
skin2_image = skin2_image.scaledToWidth(135)
skin2.setPixmap(skin2_image)

skin3 = QLabel('НАдпис')
skin3_image = QPixmap("img_2.png")
skin3_image = skin3_image.scaledToHeight(200)
skin3.setPixmap(skin3_image)

skin4 = QLabel('НАдпис')
skin4_image = QPixmap("img_3.png")
skin4_image = skin4_image.scaledToHeight(300)
skin4_image = skin4_image.scaledToWidth(200)
skin4.setPixmap(skin4_image)


H1 = QHBoxLayout()
H1.addWidget(Play)
H1.addWidget(shop)

kaka1 = QHBoxLayout()

#kaka1.addWidget(back_g)
Wkaka1 = QVBoxLayout()
Wkaka2 = QVBoxLayout()
kaka1.addLayout(Wkaka1)
kaka1.addLayout(Wkaka2)









Wkaka1.addWidget(skin1)
Wkaka1.addWidget(choose_skin1)
Wkaka1.addWidget(skin2)
Wkaka1.addWidget(choose_skin2)



Wkaka2.addWidget(skin3)
Wkaka2.addWidget(choose_skin3)
Wkaka2.addWidget(skin4)
Wkaka2.addWidget(choose_skin4)




def magazin():
    Shop.show()





Play.clicked.connect(my_mega_game)
shop.clicked.connect(magazin)
Shop.setLayout(kaka1)
window.setLayout(H1)
app.exec()

