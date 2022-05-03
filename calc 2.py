num = float(input("Digite o primeiro número: "))
acum = 0
nma = 0
nmn = 0
acum += num
op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)- Multiplicação \n(4)- Divisão: ")
if op == "1":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num > num2:
           nma = num
           nmn = num2
     elif num < num2:
            nma = num2
            nmn = num
     elif num == num2:
          nma = num
          nmn = num
     res = num + num2
elif op == "2":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num > num2:
           nma = num
           nmn = num2
     elif num < num2:
            nma = num2
            nmn = num
     elif num == num2:
          nma = num
          nmn = num
     res = num - num2
elif op == "3":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num > num2:
           nma = num
           nmn = num2
     elif num < num2:
            nma = num2
            nmn = num
     elif num == num2:
          nma = num
          nmn = num
     res = num * num2
elif op == "4":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num > num2:
           nma = num
           nmn = num2
     elif num < num2:
            nma = num2
            nmn = num
     elif num == num2:
          nma = num
          nmn = num
     res = num / num2

cont = "1"
while cont == "1":
    print("O que deseja fazer com o número: ", res)
    op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)- Multiplicação \n(4)- Divisão: ")
    if op == "1":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num2 > nma:
          nma = num2
     elif num2 < nmn:
          nmn = num2
     res = res + num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
    elif op == "2":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num2 > nma:
          nma = num2
     elif num2 < nmn:
          nmn = num2
     res = res - num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
    elif op == "3":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num2 > nma:
          nma = num2
     elif num2 < nmn:
          nmn = num2
     res = res * num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
    elif op == "4":
     num2 = float(input("Digite o segundo número: "))
     acum += num2
     if num2 > nma:
          nma = num2
     elif num2 < nmn:
          nmn = num2
     res = res / num2
     cont = input("Deseja continuar? \n(1)- Sim \n(2)- Não")
print("O resultado ", res)
print("O maior número é: ", nma)
print("O menor número é: ", nmn)
print("A soma dos números é: ", acum)