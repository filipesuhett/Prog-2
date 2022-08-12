'''Regressiva: Faça uma função que crie e retorne uma lista com todos os números pares de 1 a 100, por ́em na ordem regressiva.'''

def regressiva():
    cont = 1
    l = []
    
    while cont <= 100:
        if cont%2 == 0:
            l.append(cont)
        cont += 1    

    print(l)
    return l

if __name__ == "__regressiva__":
    regressiva()