teste = 0
while True:
    teste += 1;
    #Declarando o grafo
    graph = {}
    #Capturando a entrada
    c,e,l,p = map(int,input().split())
    #Condição de fim
    if c==e==l==p==0:
        break
    #Nós visitados
    visited = set()
    visited.add(l)
    #Looping criando as cidades
    for i in range(c):
        graph[i+1] = []
    #Looping pegando os pedágios
    for i in range(e):
        x,y=map(int,input().split())
        #Preenchendo o grafo
        if x <= c or y <= c:
            if x in graph and y not in graph[x]:
                graph[x].append(y)
            if y in graph and x not in graph[y]:
                graph[y].append(x)
    
    #Depth First Search
    def dfs(visited, graph, pedagio, start):
        proximasCidades = graph[start]
        #Loop na quantidade de pedagios
        for p in range(pedagio):
            #Faz um loop passando em todas as cidades da lista
            for cidade in proximasCidades:
                #Se a cidade não foi visitada
                if cidade not in visited:
                   #Adiciona na lista de visitadas 
                    visited.add(cidade)
                    #Adiciona na lista de proximas cidades todas as cidades vizinhas a ela que não
                    #estejam na lista de proximas cidades, nem na lista de visitadas
                    in_first = set(proximasCidades).union(visited)
                    in_second = set(graph[cidade])
                    in_second_but_not_in_first = in_second - in_first                             
                    proximasCidades = proximasCidades + list(in_second_but_not_in_first)
        #Remove a cidade inicial da lista de visitados
        visited.remove(start)
        return list(visited)

    #Chama a função para retornar a lista de cidades possíveis
    cidades = dfs(visited, graph, p, l)
    #Imprime a primeira linha da saída
    print(f'Teste {teste}')
    
    #Ordena as cidades em ordem crexcente
    cidades.sort()

    #Imprime a saída
    resultado = ''
    if(len(cidades) > 0):
        for r in range(len(cidades)):
            resultado = resultado + str(cidades[r]) + ' '
    print(resultado + '\n')
