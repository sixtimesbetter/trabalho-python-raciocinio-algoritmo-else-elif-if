usuario = input("qual seu usuario?:")

senha = input ("qual sua senha?:")

if usuario == "admin" and senha == "1234":
    print("acesso permitido")

elif usuario == "convidado" and senha == "":
    print ("acesso restrito")

else:
    print("acesso bloqueado")