print("calculadora simples")
print("\n (+) (-) (*) (/) (=)")

n = int(input("Número: "))
op = input("Operação: ")
result = n
maior = n
menor = n
while op != "=":
    n = int(input("Número: "))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    if op == "+":
        result += n
    elif op == "-":
        result -= n
    elif op == "*":
        result *= n
    elif op == "/":
        result /= n
    op = input("Operação: ")
print(f'Resultado: {result}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')

