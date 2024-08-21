import random

ehto = True
pc_numero = random.randint(1, 10)
while ehto:
    ihminen_numero = int(input("Kirjoita numero 1-10 välillä: "))
    if pc_numero > ihminen_numero:
        print("Liian pieni arvaus")
    elif pc_numero < ihminen_numero:
        print("Liian suuri arvaus")
    elif ihminen_numero == pc_numero:
        ehto = False
        print("Oikein")
        break
