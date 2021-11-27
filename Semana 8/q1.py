from collections import defaultdict
#Estrutura do grafo
class Grafo:
    def __init__(self,vertices):
        self.V= vertices #Qtd de vertices
        self.graph = defaultdict(list) #Dicionario do grafo
        self.Time = 0

    #Método para adicionar uma aresta
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    #Método de apoio para função que busca as pontes
    def bridgeUtil(self,u, visited, parent, low, disc):
        #Contador do número de pontes
        count = 0
        #Marca o nó atual como visitado
        visited[u]= True
        #Inicializa o tempo de descoberta e o valor minimo
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        #Percorre os vértices vizinhos do atual
        for v in self.graph[u]:
            #Se o nó não foi visitado, torna parente de u e faz um DFS nele
            if visited[v] == False :
                parent[v] = u
                count += self.bridgeUtil(v, visited, parent, low, disc)
                #Checa se a subarvore com raiz v tem conexão com um dos pais de u
                low[u] = min(low[u], low[v])
                #Se o vértice mais baixo alcançável da subárvore em v estiver abaixo
                #de u na árvore DFS, então u-v é uma ponte
                if low[v] > disc[u]:
                    #Aumenta em um a contagem de pontes
                    count += 1
                    #print ("%d %d" %(u,v))
            #Atualiza o menor valor de u para os pais
            elif v != parent[u]: 
                low[u] = min(low[u], disc[v])
        return count

    #Método para encontrar todas as pontes
    def bridge(self):
        #Contador de pontes
        count = 0
        #Marca todos os vértices como não visiados e inicializa seus pais e os visitados
        #e os pontos de articulação
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)

        #Chama a função auxiliar recursiva para achar as pontes na árvore de DFS com raiz no vértice i
        for i in range(self.V):
            if visited[i] == False:
                count += self.bridgeUtil(i, visited, parent, low, disc)
        return count
        
while(True):
    try:
        #Contador de pontes pro resultado
        count = 0
        #Pega a quantidade de nós e de arestas
        C, P = map(int,input().split())
        #Inicia o grafo com a quantidade de cidades
        graph = Grafo(C)
        #Percorre a quantidade de "pontes" e preenche o grafo
        for i in range(P):
            a, b = map(int,input().split())
            graph.addEdge(a-1,b-1)
        #Imprime a quantidade de pontes
        print(graph.bridge())
    except EOFError:
        break
