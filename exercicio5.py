def verificar_divisibilidade_por_3(m):
    if sum(m) % 3 == 0:
        return 'sim'
    else:
        return 'não'

while True:
    n = int(input('Algarismos: '))
    m = list(map(int,input('Número: ')[:n]))

    resultado = verificar_divisibilidade_por_3(m)
    print(resultado)
    print()
    
    r = input('Continuar verificando? ')
    if r.lower() == 'não' or r.lower() == 'nao':
        break
