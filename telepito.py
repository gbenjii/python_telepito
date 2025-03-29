import time
import sys
import requests
import os
from bs4 import BeautifulSoup
import re
verzio_lista = "1 2"
print("Hello ez a Benji telepítő!")
time.sleep(1)
while True:
    bemenet = input("Folytatni kívánja a letöltést? igen vagy nem?: ")
    if bemenet == "igen":
        print("Egy pillanat múlva folyatatódik a telepítés!")
        break
    elif bemenet == "nem":
        print("A telepítés nem sikerült az ablak 3 másodperc múlva bezáródik!")
        time.sleep(3)
        sys.exit()
    else:
        print("Csak pontosan igen vagy nem írható írható! Próbáld újra.")
time.sleep(1)
while True:
    print("Elérhető verziók:")
    print(verzio_lista)
    time.sleep(1)
    bemenet = input("Kérem, írja be hogy melyik verziót szeretné letölteni: ")
    if bemenet.lower() == "1":
        print("Ön az első verziót válaszottta hamarosan megkezdődik a letöltés!")
        time.sleep(2)
        print("Az első verzó letöltés alatt")
        time.sleep(5)
        print("A letöltés kész!")
        time.sleep(2)
        sys.exit()
    elif bemenet.lower() == "2":
        print("Ön a második verziót válaszottta hamarosan megkezdődik a letöltés!")
        print("A második verzó letöltés alatt")
        time.sleep(5)
        print("A letöltés kész!")
        time.sleep(2)
        sys.exit()
    else:
        print("Csak 1 vagy 2 értéket lehet megadni! Próbáld újra.")
