N = int(input('Testes: '))

C = 0
R = 0
S = 0
total_cobaias = 0

for i in range(N):
    QTD,letra = list(input('Quantidade: ').upper().split())
    QTD = int(QTD)
    
    if letra == 'C':
        C += QTD
    elif letra == 'R':
        R += QTD
    elif letra == 'S':
        S += QTD
    total_cobaias += QTD

percentual_coelhos = (C*100)/total_cobaias
percentual_ratos = (R*100)/total_cobaias
percentual_sapos = (S*100)/total_cobaias

print('Total:',total_cobaias,'cobaias')
print('Total de coelhos:',C)
print('Total de ratos:',R)
print('Total de sapos:',S)
print(f'Percentual de coelhos: {percentual_coelhos:.2f}%')
print(f'Percentual de ratos: {percentual_ratos:.2f}%')
print(f'Percentual de sapos: {percentual_sapos:.2f}%')