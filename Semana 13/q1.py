from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.graph = defaultdict(list) 
        self.qtd_vertices = v   
        self.T = 0
        
    def add(self,u,v):
        self.graph[u].append(v)

    def Tarjan(self):
        #Marca todos os vértices como não visiados e inicializa seus pais e os visitados
        #e os pontos de articulação
        visited = [False] * (self.qtd_vertices)
        disc = [-1] * (self.qtd_vertices)
        low = [-1] * (self.qtd_vertices)
        parent =[]
        #Chama a função auxiliar recursiva para achar os componentes na árvore de DFS com raiz no vértice i
        for i in range(self.qtd_vertices):
            if disc[i] == -1:
                if self.Util(i, low, disc, visited, parent):
                    print('1')
                else:
                    print('0')
                    return
                
    def Util(self, u, low, disc, visited, parent):
        #Marca o nó atual como visitado
        visited[u]= True
        #Inicializa o tempo de descoberta e o valor minimo
        disc[u] = self.T
        low[u] = self.T
        self.T += 1
        parent.append(u)
        for v in self.graph[u]:			
            if disc[v] == -1 :
                self.Util(v, low, disc, visited, parent)
                low[u] = min(low[u], low[v])						
            elif visited[v] == True:
                low[u] = min(low[u], disc[v])
        w = -1
        stackresult = []
        if low[u] == disc[u]:
            while w != u:
                w = parent.pop()
                stackresult.append(w)
                visited[w] = False
            if len(stackresult) == self.qtd_vertices:
                return True
            else:
                return False

while True:
    N,M = map(int,input().split())
    if N == M == 0:
        break
    graph = Graph(N)
    for i in range(M):
        V,W,P = map(int,input().split())
        if P == 1:
            graph.add(V-1,W-1)
        else:
            graph.add(V-1,W-1)
            graph.add(W-1,V-1)
    graph.Tarjan()
        
