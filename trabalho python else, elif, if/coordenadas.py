coordenadaX = float(input("qual sua coordenada X?:"))

coordenadaY = float(input("qual sua coordenada Y?:"))

if coordenadaX < 0 or coordenadaX > 10 or coordenadaY < 0 or coordenadaY > 10:
    print("fora do quadrado")

elif coordenadaX == 0 or coordenadaX == 10 or coordenadaY == 0 or coordenadaY == 10:
    print("na fronteira")

else:
    print("dentro do quadrado")
