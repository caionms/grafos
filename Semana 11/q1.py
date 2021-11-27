#Depth First Search
def dfs(start, visited, graph, N, count):
    #Fila
    queue = []
    visited[start] = True
    queue.append(start)
    while len(queue) != 0:
        a = queue.pop(0) 
        for j in range(len(graph[a])):
            if not visited[graph[a][j]]:
                visited[graph[a][j]] = True
                queue.append(graph[a][j])

T = int(input())
for a in range(1,T+1):
    graph = {}
    entrada = input()
    if ' ' not in str(entrada):
        M = int(input()) #Número de vértices
        N = int(entrada) #Número de arestas
    else:
        N,M = map(int,entrada.split())
    visited = [False]*(N+1)
    for i in range(N+1):
        graph[i] = []
    for i in range(M):
        X, Y = map(int,input().split())
        if (X) in graph and (Y) not in graph[X]:
            graph[X].append(Y)
        if (Y) in graph and (X) not in graph[Y]:
            graph[Y].append(X)
    count = 0
    dfs(1, visited, graph, N, count)
    for i in range(1,N+1):
        if visited[i] == False:
            dfs(i, visited, graph, N, count)
            count += 1
    if count == 0:
        print(f'Caso #{a}: a promessa foi cumprida')
    else:
        print(f'Caso #{a}: ainda falta(m) {count} estrada(s)')
    
