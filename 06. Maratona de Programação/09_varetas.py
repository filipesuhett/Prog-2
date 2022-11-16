def varetas(resu):
    cont = 0
    l = aux = []
    n = int(input('Quantos grupos de varetas serão? '))
    if n == 0:
        return 0
    while n > cont:
        tam = int(input('Qual o Tamanho delas? '))
        v = int(input('Quantas Varetas são? '))
        aux = [tam, v]
        l.append(aux)
        cont += 1
    resolve(l, resu)
    varetas(resu)

def resolve(l, resu):
    cont = 0
    reta = 0
    combi = 0
    while cont < len(l):
        if l[cont][1] > 3:
            x = l[cont][1]//4
            reta += x
            l[cont][1] -= x*4
        if 4 > l[cont][1] > 1:   
            combi += 1
        cont += 1
    y = combi // 2
    reta += y
    resu.append(reta)
    
def main():
    resu = []
    cont = 0
    varetas(resu)
    
    while len(resu) > cont:
        print(resu[cont])
        cont += 1
     
if __name__ == '__main__':
    main()