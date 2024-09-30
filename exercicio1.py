def direcao_soldado(grau):
    if grau == 0:
        return 'N'
    elif grau == 1 or grau == -3:
        return 'O'
    elif grau == -1 or grau == 3:
        return 'L'
    else:
        return 'S'
        
N = int(input('Comandos: '))
C = list(map(str,input().upper()[:N]))
#usei "[:N]" para que C aceite até o valor de N 

grau = 0
for comando in C:
    if comando == 'D':
        grau -= 1
    elif comando == 'E':
        grau += 1
    if grau < -3 or grau > 3:
        grau = 0
        
sentido = direcao_soldado(grau)
print(sentido)
    