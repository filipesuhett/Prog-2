def Troca(l1, l2):
    lb = []
    la = []
    clear = []
    i = 0
    cont = 0
    
    if l1 == l2:
        print(0)
    else:
        while i < len(l1):
            while cont < len(l2):    
                if not l2[cont] == l1[i]:
                    if lb.count(l1[i]) == 0:
                        lb.append(l1[i])
                    if la.count(l2[cont]) == 0:
                        la.append(l2[cont])
                else:
                    if clear.count(l1[i]) == 0:
                        clear.append(l1[i])
                cont += 1
            cont = 0
            i += 1
        cont = 0
        if len(clear) > 0:    
            while len(clear) > cont:
                la.remove(clear[cont])
                lb.remove(clear[cont])
                cont += 1
        if len(la) > len(lb):
            print(len(lb))
        else:
            print(len(la))