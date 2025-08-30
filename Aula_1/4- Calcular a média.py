nota_1 = nota_2 = nota_3 = nota_4 = 0.0
media = 0.0

#Entrada de dados é do tipo string e devemos transforma-lo para tipo float
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
nota_4 = float(input('Digite a quarta nota: '))

#Calcular a média aritmética das notas
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

if media >= 7:
    print('O aluno foi aprovado')
elif media < 7 and media >= 4:
    print('O aluno esta de exame final')
else:
    print('O aluno foi reprovado')

print('A média do aluno é:', media)