#from random import uniform
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setenbro','outubro','novembro','dezembro']
ano = []
v_mes = []
total = 0
for mes in range(0, 12):
    for semana in range(0, 4):
        #v_mes.append(uniform(0,1000))
        v_mes.append(float(input(f'vendas da {semana+1}ª semana do mes de {meses[mes]}:')))
    ano.append(v_mes.copy())
    total += sum(v_mes)
    v_mes.clear()
print(f'\n{"VENDAS NO ANO".center(67)}','\n','=' * 68)
print(f'{"Mês".center(10)} {"1ª semana".center(10)} {"2ª semana".center(10)} {"3ª semana".center(10)} {"4ª semana".center(10)} {"Total no mês".center(10)}')
for mes in range(12):    
    print(f'{meses[mes].center(10)}', end ='|')
    for semana in range(4):
        print(f'{ano[mes][semana]:.2f}'.rjust(5).center(10), end ='|')
    print(f'{sum(ano[mes]):.2f}'.rjust(5).center(12)) 
print('=' * 68,f'\nTotal anual: R${total:.2f}\n')
