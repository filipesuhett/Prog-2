def spo2(mu, playlists):
    cont = 0
    
    for i in range(len(playlists)):
        for j in range(len(playlists[i][2])):
            if mu == playlists[i][2][j]:
                cont += 1
                
    return cont

def spo3(playlists, musicas, artistas):
    maior = ''
    te = -1
    x = list(musicas.keys())
    
    for l in range(len(musicas)):
        cont = 0
        for i in range(len(playlists)):
            for j in range(len(playlists[i][2])):
                if x[l] == playlists[i][2][j]:
                    cont += 1
        if cont > te:
            te = cont
            maior = x[l]
        
        l = artistas.get(musicas[maior][0])    
            
    print(f'Hit do Ano: {musicas[maior][1]} ({l})')