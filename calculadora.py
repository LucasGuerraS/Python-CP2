acum = 0
nma = 0
nmn = 0
escolha = "1"
num = float(input("Digite um número: "))
acum += num
op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)- Multiplicação \n(4)- Divisão: ")
if op == "1":
      num2 = float(input("Digite o número que deseja somar: "))
      if num > num2:
            nma = num
            nmn = num2
      elif num < num2:
            nma = num2
            nmn = num
      res = num + num2
      acum += num2
      print("O resultado ", res)
      escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
      while escolha == "1":
           print("O que deseja fazer com o número: ", res)
           op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)-  Multiplicação \n(4)- Divisão: ")
           if op == "1":
               num2 = float(input("Digite o número que deseja somar: "))
               res = res + num2
               acum += num2
               if num2 > nma:
                    nma = num2
               elif num2 < nmn:
                    nmn = num2
               print("O resultado ", res)
               escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "2":
                num2 = float(input("Digite o número que deseja subtrair: "))
                res = res - num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "3":
                num2 = float(input("Digite o número que deseja multiplicar: "))
                res = res * num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "4":
                num2 = float(input("Digite o número que deseja dividir: "))
                res = res / num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
elif op == "2":
      num2 = float(input("Digite o número que deseja subtrair: "))
      if num > num2:
            nma = num
            nmn = num2
      else:
            nma = num2
            nmn = num
      acum += num2
      res = num - num2
      print("O resultado ", res)
      escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
      while escolha == "1":
           print("O que deseja fazer com o número: ", res)
           op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)-  Multiplicação \n(4)- Divisão: ")
           if op == "1":
               num2 = float(input("Digite o número que deseja somar: "))
               res = res + num2
               acum += num2
               if num2 > nma:
                    nma = num2
               elif num2 < nmn:
                    nmn = num2
               print("O resultado ", res)
               escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "2":
                num2 = float(input("Digite o número que deseja subtrair: "))
                res = res - num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "3":
                num2 = float(input("Digite o número que deseja multiplicar: "))
                res = res * num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "4":
                num2 = float(input("Digite o número que deseja dividir: "))
                res = res / num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
      
elif op == "3":
      num2 = float(input("Digite o número que deseja multiplicar: "))
      if num > num2:
            nma = num
            nmn = num2
      else:
            nma = num2
            nmn = num
      res = num * num2
      acum += num2
      print("O resultado ", res)
      escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
      while escolha == "1":
           print("O que deseja fazer com o número: ", res)
           op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)-  Multiplicação \n(4)- Divisão: ")
           if op == "1":
               num2 = float(input("Digite o número que deseja somar: "))
               res = res + num2
               acum += num2
               if num2 > nma:
                    nma = num2
               elif num2 < nmn:
                    nmn = num2
               print("O resultado ", res)
               escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "2":
                num2 = float(input("Digite o número que deseja subtrair: "))
                res = res - num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "3":
                num2 = float(input("Digite o número que deseja multiplicar: "))
                res = res * num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "4":
                num2 = float(input("Digite o número que deseja dividir: "))
                res = res / num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")

  
elif op == "4":
      num2 = float(input("Digite o número que deseja dividir: "))
      if num > num2:
            nma = num
            nmn = num2
      else:
            nma = num2
            nmn = num
      res = num / num2
      acum += num2
      print("O resultado ", res)
      escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
      while escolha == "1":
           print("O que deseja fazer com o número: ", res)
           op = input("Digite a operação \n(1)- Adição \n(2)- Subtração \n(3)-  Multiplicação \n(4)- Divisão: ")
           if op == "1":
               num2 = float(input("Digite o número que deseja somar: "))
               res = res + num2
               acum += num2
               if num2 > nma:
                    nma = num2
               elif num2 < nmn:
                    nmn = num2
               print("O resultado ", res)
               escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "2":
                num2 = float(input("Digite o número que deseja subtrair: "))
                res = res - num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "3":
                num2 = float(input("Digite o número que deseja multiplicar: "))
                res = res * num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
           elif op == "4":
                num2 = float(input("Digite o número que deseja dividir: "))
                res = res / num2
                acum += num2
                if num2 > nma:
                    nma = num2
                elif num2 < nmn:
                    nmn = num2
                print("O resultado ", res)
                escolha = input("deseja continuar? \n(1)- Sim \n(2)- Não")
print("Resultado final: ", res)
print("O valor acumulado foi: ", acum)
print(f"Maior valor {nma} e Menor valor {nmn}")