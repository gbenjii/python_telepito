import time
import sys
verzio_lista = "1 2"
print("Hello ez a Benji telepítő!")
time.sleep(2)
while True:
    bemenet = input("Folytatni kívánja a letöltést? igen vagy nem?: ")
    if bemenet == "igen":
        print("Egy pillanat múlva folyatatódik a telepítés!")
        break
    elif bemenet == "nem":
        print("A telepítés nem sikerült az ablak 3 másodpercmúlva bezáródik!")
        time.sleep(3)
        sys.exit()
    else:
        print("Csak pontosan igen vagy nem írható írható! Próbáld újra.")

time.sleep(1)
print ("Kérlek válassz egy verziót ezek közül: ")
time.sleep(1)
print(verzio_lista)
while True:
    bemenet = input("Kérem, írja be hogy melyik verziót szeretné letölteni: ")
    if bemenet.lower() == "1":
        print("Ön az első verziót válaszottta hamarosan megkezdődik a letöltés!")
        time.sleep(2)
        print("Az első verzó letöltés alatt")
    elif bemenet.lower() == "2":
        print("Ön a második verziót válaszottta hamarosan megkezdődik a letöltés!")
        print("A második verzó letöltés alatt")
    else:
        print("Csak 1 vagy 2 értéket lehet megadni! Próbáld újra.")
