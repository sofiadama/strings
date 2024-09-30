N = int(input('Testes: '))

for i in range(N):
    leds = 0
    valor = input('Valor: ')

    for num in valor:
        num = int(num)
        if num == 0 or num == 6 or num == 9:
           leds += 6
        elif num == 1:
           leds += 2
        elif num == 2 or num == 3 or num == 5:
           leds += 5
        elif num == 4:
           leds += 4
        elif num == 7:
           leds += 3
        elif num == 8:
           leds += 7

    print(leds,'leds')
