cod_produto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_estoque = [120, 130, 100, 55, 30, 80, 10, 40, 60, 110]
while True:
    indice = 0
    cod_cliente = int(input('Digite o codigo do cliente: '))
    if cod_cliente == 0:
        break
    print(f'\n Código do produto:',cod_produto,'\n','Total no estoque:',total_estoque ,'\n')
    cod_prod = int(input('Digite o codigo do produto: '))
    if cod_prod in cod_produto:
        indice = cod_produto.index(cod_prod)
        qtd = int(input('Digite a quantidade: ')) 
        if total_estoque[indice] - qtd >= 0:
            total_estoque[indice] -= qtd
            print('Obrigado e volte sempre.')
            i = 0
            while i < len(cod_produto):
                print(cod_produto[i],total_estoque[i])
                i += 1
        else:
            print('Não temos unidades suficiente do produto',cod_prod, 'no estoque! Apenas:',total_estoque[indice])
    else:
        print('Código inexistente')
