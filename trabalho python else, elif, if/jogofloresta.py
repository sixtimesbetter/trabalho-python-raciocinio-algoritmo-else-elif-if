cam = input("voce tem dois caminhos (esquerda/direita):")

if cam == "esquerda":
    acao1 = input("voce podera (atravessar/voltar):")

    if acao1 == "atravessar":
        print("voce chegou a uma vila segura")
    else:
        print("voce continua perdido na floresta")

elif cam == "direita":
    acao2 = input("voce podera (subir/voltar)")

    if acao2 == "subir":
        print("voce encontrou um tesouro")
    else:
        print("voce continua perdido na floresta")

        
     