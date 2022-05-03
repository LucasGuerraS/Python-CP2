num = float(input("Digite o primeiro número: "))
op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)- Multiplicação \n(4)- Divisão: ")
if op == "1":
     num2 = float(input("Digite o segundo número: "))
     res = num + num2
elif op == "2":
     num2 = float(input("Digite o segundo número: "))
     res = num - num2
elif op == "3":
     num2 = float(input("Digite o segundo número: "))
     res = num * num2
elif op == "4":
     num2 = float(input("Digite o segundo número: "))
     res = num / num2

cont = "1"
while cont == "1":
    print("O que deseja fazer com o número: ", res)
    op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)- Multiplicação \n(4)- Divisão: ")
    if op == "1":
     num2 = float(input("Digite o segundo número: "))
     res = res + num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
    elif op == "2":
     num2 = float(input("Digite o segundo número: "))
     res = res - num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
    elif op == "3":
     num2 = float(input("Digite o segundo número: "))
     res = res * num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
    elif op == "4":
     num2 = float(input("Digite o segundo número: "))
     res = res / num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
print("O resultado ", res)