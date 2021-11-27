aux = 2**25

def dijkstra(O, D, N):
    global aux
    nv = 0 
    dist = [aux]*(N+1)
    corr = [False]*(N+1)
    dist[O] = 0
    for i in range(1,N+1):
        sd = aux
        if corr[D]:
            break
        for j in range(1,N+1):
            if dist[j] < sd and not corr[j]:
                sd = dist[j]
                nv = j
        if sd == aux:
            break
        corr[nv] = True
        for j in range(1,N+1):
            if sd + matrix[nv][j] < dist[j]:
                dist[j] = sd + matrix[nv][j]
    return dist[D]
        
while True:    
    N,E = map(int,input().split())
    if N == E == 0:
        break
    matrix = []
    for i in range(N+1):          
        a =[aux]*(N+1)
        matrix.append(a)
    for i in range(E):
        X,Y,H = map(int,input().split())
        matrix[X][Y] = H
        if matrix[Y][X] != aux:
            matrix[X][Y] = matrix[Y][X] = 0
    K = int(input())
    for i in range(K):
        O,D = map(int,input().split())
        result = dijkstra(O,D,N)
        if result == aux:
            print ('Nao e possivel entregar a carta')
        else:
            print (result)
    print('')
    
