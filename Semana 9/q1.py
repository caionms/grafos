#É possível distribuir?
dist = False
#Estrutura do grafo
graph = {}
#Quantidade de camisas
camisas = [0]*6

#Função para permitir o uso de lista
def str_to_int_camisa(camisa):
    if camisa == "XS":
        return 0
    elif camisa == "S":
        return 1
    elif camisa == "M":
        return 2
    elif camisa == "L":
        return 3
    elif camisa == "XL":
        return 4
    else:
        return 5

#Método de busca 
def busca(graph, i, M):
    #Se tiver chegado na última camisa, retorna pessoa
    if i == M:
        global dist
        dist = True
        return 
    #Se for possível distribuir, retorna
    if dist:
        return
    #Se a quantidade da camisa 1 da pessoa for maior que zero
    if camisas[str_to_int_camisa(graph[i][0])] > 0:
        camisas[str_to_int_camisa(graph[i][0])] -= 1
        busca(graph, i+1, M)
        camisas[str_to_int_camisa(graph[i][0])] += 1
    #Se a quantidade da camisa 2 da pessoa for maior que zero
    if camisas[str_to_int_camisa(graph[i][1])] > 0:
        camisas[str_to_int_camisa(graph[i][1])] -= 1
        busca(graph, i+1, M)
        camisas[str_to_int_camisa(graph[i][1])] += 1

#Número de casos
X = int(input())
for i in range(X):
    dist = False
    #Pega a quantidade de vértices e arestas
    N, M = map(int,input().split())
    #Preenchendo a lista da camisa
    for i in range(6):
        camisas[i] = N/6
    for i in range(M):
        #Pega os nós conectados e o peso da conexão
        entrada = input().split()
        #Adiciona essa aresta no grafo
        graph[i] = []
        graph[i].append(entrada[0]) #Tamanho 1
        graph[i].append(entrada[1]) #Tamanho 2
    #Chama o método de busca
    busca(graph, 0, M)
    #Se for possível distribuir
    if(dist):
        print('YES')
    else:
        print('NO')

   


