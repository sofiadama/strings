sentido = {0:'N',1:'O',2:'S',3:'L',-1:'L',-2:'S',-3:'O'}

N = int(input('Número de comandos: '))
C = list(map(str,input('Comandos: ').upper()[:N]))

graus = 0
for comando in C:
    if graus < -3 or graus > 3:
        graus = 0
    elif comando == 'D':
        graus -= 1
    elif comando == 'E':
        graus += 1
    print(sentido[graus])
