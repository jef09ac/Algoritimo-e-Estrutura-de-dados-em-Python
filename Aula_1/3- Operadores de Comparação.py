n1 = n2 = 0

#A entrada de dados é um tipo de string e devemos transforma-lo para tipo inteiro

print('Digite o primeiro número:')
n1 = int(input())
n2 = int(input('Digite o segundo número: '))

if n1 == n2:
    print('Os números são iguais', '\n')
elif n1 > n2:
    print('O primeiro número é maior que o segundo', '\n')
else:
    print('O segundo número é maior que o primeiro', '\n')