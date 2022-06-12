meses =('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novenbro','dezembro')
ano = list()
venda_mes = list()
total = 0
#preenchimento da matriz
for mes in range(12):
    for semana in range(4):
        venda_mes.append(float(input(f'vendas da {semana+1}ª semana do mes de {meses[mes]}:')))
    ano.append(venda_mes.copy())
    total += sum(venda_mes)
    venda_mes.clear()
#apresentação dos dados infomados
print(f'\n{"vendas no ano".center(67)}')
print(f'{"mes".center(10)} {"1ª semana".center(10)} {"2ª semana".center(10)} {"3ª semana".center(10)} {"4ª semana".center(10)} {"total no mes".center(12)}')

for mes in range(12):
    print(f'{meses[mes].center(10)}', end ='')
    for semana in range(4):
        print(f'{ano[mes][semana]:.2f}'.rjust(8).center(10), end ='')
    print(f'{sum(ano[mes]):.2f}'.rjust(10).center(12))
print(f'\ntotal anual: R${total:.2f}')
