yritys = 1
while yritys <= 5:
    tunnus = input("Käyttäjä tunnus: ")
    salasana = input("Salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break

    else:
        print("Pääsy evätty.")
        yritys += 1
