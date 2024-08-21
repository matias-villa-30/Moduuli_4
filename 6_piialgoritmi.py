import random

n = 0
index = 0
pistetta = int(input("Kirjoita monta pistetta: "))

while index < pistetta:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    punto = x**2 + y**2 < 1

    if punto == True:

        n += 1
    index += 1



pi_estimado = 4 * (n/pistetta)
print(pi_estimado)