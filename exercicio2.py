N = int(input('Testes: '))

for i in range(N):
    n1,letra,n2 = input()
    n1 = int(n1)
    n2 = int(n2)

    if n1 == n2:
        r = n1 * n2
    elif letra.isupper():
        r = n2 - n1
    elif letra.islower():
        r = n1 + n2

    print(r)
