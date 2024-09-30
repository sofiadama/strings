qtd_leds = {'0': 6,'1': 2,'2': 5,'3': 5,'4': 4,'5': 5,'6': 6,'7': 3,'8': 7,'9': 6}

N = int(input('Testes: '))

for i in range(N):
    leds = 0
    valor = list(input('Valor: '))
    for digito in valor:
        leds += qtd_leds[digito]
    print(leds,'leds')
