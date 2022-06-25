altura = int(input('Digite a altura do triângulo:'))
while altura <= 0:
    print('Altura inválida!')
    altura = int(input('Digite a altura do triângulo:'))
base = int(input('Digite a base do triângulo:'))
while base <= 0:
    print('Base inválida!')
    base = int(input('Digite a base do triângulo!:'))
area = (base * altura) / 2
print('A área do triângulo é igual a:', area)
