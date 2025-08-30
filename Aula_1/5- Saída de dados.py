#utilizando a função print
print(' ') #Utilizado para pular uma linha
nome = input('Digite seu nome: ')
frase = 'Olá ' + nome + '!' + ' Bem vindo a aula de Python!'
print(frase)
print(nome + ', Tenha um bom dia!')

#Para não ocorrer quebra de linha entre um print e outro, usa-se o comando end=
sobrenome = input('Digite o seu sobrenome: ')
print('Meu nome completo é ' + nome + ' ' + sobrenome, end=' ')