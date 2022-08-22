def sal(x):
    f = []
    s = []
    cont = 0

    for i in range(x):
        f.append(input('Nome? '))
        s.append(int(input('Salário? ')))
    while cont < x:
        if sum(s)/x < s[cont]:
            print(f[cont], end=" ")
        cont += 1