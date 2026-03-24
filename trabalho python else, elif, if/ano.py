anoB = int(input("Qual é o ano que voce ira verificar se é um ano bissexto?:"))

if (anoB % 4 == 0 and anoB % 100 != 0) or (anoB % 400 == 0):
    print("ano bissexto")
else:
    print("esse ano nao é bissexto")