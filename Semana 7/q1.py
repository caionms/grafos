from collections import defaultdict

#Função para achar o conjunto do elemento i
def find(parent, i):
    #Caso o pai seja ele mesmo
    if parent[i-1] == i:
        #Retorna ele
        return i
    #Caso não chama o método de novo passando o pai dele
    return find(parent, parent[i-1])

#Função para fazer a união por rank dos conjuntos de x e y 
def union(parent, rank, x, y):
    #Acha a raiz do conjunto de x
    xroot = find(parent, x)
    #Acha a raiz do conjunto de y
    yroot = find(parent, y)
 
    #Anexa a árvore de menor classificação sob a raiz da
    #de maior classificação
    if rank[xroot-1] < rank[yroot-1]:
        parent[xroot-1] = yroot
    elif rank[xroot-1] > rank[yroot-1]:
        parent[yroot-1] = xroot
    #Se as classificações forem iguais, então torna uma raiz e
    #incrementa o rank em 1
    else:
        parent[yroot-1] = xroot
        rank[xroot-1] += 1

#Função principal para a construção da árvore através do alg.
#de Kruskal
def KruskalMST(graph, qtdArestas):
    #Guarda a árvore
    result = []  
    #Index das arestas guardadas e da árvore resultante
    i, e = 0, 0
 
    #Cria um novo grafo ordenado em ordem descrescente de peso
    newGraph = sorted(graph,key=lambda item: item[2])

    #Guarda os pais dos nós
    parent = []
    #Guarda os ranks de cada subconjunto
    rank = []
 
    #Cria um subconjunto para cada nó comapenas 1 elemento e
    #define seu rank como 0
    for node in range(qtdArestas):
        parent.append(node+1)
        rank.append(0)
 
    #Faz um loop pela quantidade de arestas - 1
    while e < qtdArestas - 1:
 
        #Pega a aresta de menor peso
        u, v, w = newGraph[i]
        #Aumenta em 1 o index de arestas guardadas
        i = i + 1
        #Busca o pai de u
        x = find(parent, u)
        #Busca o pai de v
        y = find(parent, v)
 
        #Se essa aresta não gera um ciclo
        if x != y:
            #Aumenta o index da árvore
            e = e + 1
            #Adiciona ela na árvore
            result.append([u, v, w])
            #Faz a união do conjunto das duas arestas
            union(parent, rank, x, y)
        #Se não, discarta essa aresta
    #Variável para guardar o custo da árvore
    minimumCost = 0
    #Percorre as arestas na árvore
    for u, v, weight in result:
        #Incrementa em 1 para cada aresta
        minimumCost += weight
    #Imprime o resultado do custo
    print(minimumCost)

#Estrutura do grafo
graph = []
#Pega a quantidade de vértices e arestas
R, C = map(int,input().split())
for i in range(C):
    #Pega os nós conectados e o peso da conexão
    V, W, P = map(int,input().split())
    #Adiciona essa aresta no grafo
    graph.append([V, W, P])
#Chama o método baseado no algoritmo de Kruskal
KruskalMST(graph, R)
    
