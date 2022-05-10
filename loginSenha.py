username = "LucasGuerraS"
senha = "P@ssw0rd778"
continua = True

while continua == True:
    cont = 0
    while cont <= 3:
         x = input("Digite seu usuário: ")
         y = input("Digite sua senha: ")
         if x == username and y == senha:
             print("Login efetuado com sucesso!")
             continua = False
             break
         else:
            print("Usuário ou senha inválidos!")
            cont += 1
            if cont == 3:
                print("Redefina o usuário e a senha por favor!")
                username = input("Digite seu novo usuário: ")
                senha = input("Digite sua nova senha: ")
                
