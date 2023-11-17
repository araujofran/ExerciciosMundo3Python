
dados={}
dados['nome']=str(input('Nome do jogador: '))
partidas= int (input('Quantas partidas ele jogou? '))
dados['partidas']=partidas
c=0
gols=[]
dados['gols']= gols
somagols=0

while c <=dados['partidas']-1:
    g= int (input(f'Quantos gols na partida {c}? '))
    gols.append(g)
    somagols+=g
    c+=1
dados['total']=somagols
del dados['partidas']
print()
print(35*'==')
print(dados)
print(35*'==')
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}. ')
print()
print(35*'==')
print (f'O jogador {dados["nome"]} jogou {partidas} partidas e {somagols} gols. ')
print()

    
    