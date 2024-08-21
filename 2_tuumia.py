yksi_tuuma = 2.54

tuuma = float(input("Kirjoita tumaa: "))

while tuuma >= 0:
    muuntaa = tuuma * yksi_tuuma
    print(f"{tuuma} on {muuntaa} cm")
    tuuma = float(input("Kirjoita tumaa: "))

    #print(f"{tuuma} on {muuntaa} cm")