

lista = []

while True:
    numerot = input("Kirjoita numerot, ohjelma loppu kun se kirioita tila merkki: ")
    if numerot != "":

        lista.append(numerot)
    elif numerot == "":

        maximo = max(lista, key=int)
        minimo = min(lista, key=int)
        print(f"Maksimi numero oli: {maximo}\nMinimi numero oli: {minimo} ")
        break

