#Entrada com a quantidade de casos testes
T = int(input())
#Loop passando pelos casos testes
for t in range(T):
    #Declarando o grafo
    graph = {}
    #Capturando o nó inicial do labirinto
    n = int(input())
    #Nós visitados
    visited = set()
    visited.add(n)
    #Capturando a quantidade de vértices e arestas
    v,a=map(int,input().split())
    #Looping criando os nós do labirinto
    for i in range(v):
        graph[i] = []
    #Looping pegando os vértices que são ligados pelas arestas
    for i in range(a):
        x,y=map(int,input().split())
        #Preenchendo o grafo
        if x in graph and y not in graph[x]:
            graph[x].append(y)
        if y in graph and x not in graph[y]:
            graph[y].append(x)
    
    #Depth First Search
    def dfs(visited, graph, arestas, start):
        #Quantidade de movimentos
        movimentos = 0
        #Variavel para guardar os proximos nós na sequencia
        proximosNos = graph[start]
        for a in range(arestas):
            for no in proximosNos:
                 #Se o no não foi visitada
                if no not in visited:
                   #Adiciona na lista de visitadas 
                    visited.add(no)
                    #Adiciona na lista de proximas nós todas os nós vizinhas a ele que não
                    #estejam na lista de proximas nós, nem na lista de visitados
                    in_first = set(proximosNos).union(visited)
                    in_second = set(graph[no])
                    in_second_but_not_in_first = in_second - in_first                             
                    proximosNos = proximosNos + list(in_second_but_not_in_first)
                    #Aumenta em 1 a quantidade de movimentos
                    movimentos += 1
        return movimentos
    
    #Chama a função para retornar a quantidade de movimentos e mult por 2
    #Pois é para contar ida e volta
    qtdMovimentos = dfs(visited, graph, a, n) * 2
    #Imprime a saída
    print(qtdMovimentos)
