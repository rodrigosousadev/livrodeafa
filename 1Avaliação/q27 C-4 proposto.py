status = ''; ncanal = 0; npessoas = 0; tpesoas = 0
c4 = 0; c5 = 0; c7 = 0; c12 = 0 
status = input('A tv está ligada? (s/n):')
while status == 'n':
    print('A tv desligada no momento! Dirija-se a próxima casa.')
    status = input('A tv está ligada? (s/n):')
if status == 's':
    ncanal = int(input('Escolha o canal  (4,5,7,12) ou 0 para encerrar:'))
    while ncanal != 0:
        npessoas = int(input('Quantas pessoas estão assistindo?'))
        print('Casa adicionada a pesquisa vamos para a próxima.')
        status = input('A tv está ligada? (s/n):')
        if ncanal == 4:
            c4 = c4 + npessoas
        elif ncanal == 5:
            c5 = c5 + npessoas
        elif ncanal == 7:
            c7 = c7 + npessoas
        elif ncanal == 12:
            c12 = c12 + npessoas
        else:
            print('canal inválido!')
            ncanal = int(input('Escolha o canal (4,5,7,12) ou 0 para encerrar:'))
        tpesoas = tpesoas + npessoas
        ncanal = int(input('Escolha o canal (4,5,7,12) ou 0 para encerrar:'))
else:
    print('Informação inválida!')
    status = input('A tv está ligada? (s/n):')
print('A Audiêcia do canal 4 é de: %.2f ' %(c4/tpesoas),'%')
print('A Audiêcia do canal 5 é de: %.2f ' %(c5/tpesoas),'%')
print('A Audiêcia do canal 7 é de: %.2f ' %(c7/tpesoas),'%')
print('A Audiêcia do canal 12 é de: %.2f ' %(c12/tpesoas),'%')
