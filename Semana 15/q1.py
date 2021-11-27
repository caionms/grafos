from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.graph = {}        
        self.qtd_vertices = v   
        self.T = 0
        
    def add(self,u,v):
        if v not in self.graph[u]:
            self.graph[u].append(v)
        if u not in self.graph[v]:
            self.graph[v].append(u)

    def criaDic(self):
        valores = {}
        for key in self.graph.keys():
            valores[key] = []
            valores[key].append(False) #visited - 0
            valores[key].append(-1) #disc - 1
            valores[key].append(-1) #low - 2
        return valores

    def ImprimeResultado(self, resultado):
        for listaresult in resultado:
            aux = ''
            for i in range(len(listaresult)):
                aux += f'{listaresult[i]},'
            print(aux)
        print(f'{len(resultado)} connected components')
        print('')
            
    
    def Tarjan(self):
        #Marca todos os vértices como não visitados e inicializa seus pais e os visitados
        #e os pontos de articulação
        valores = self.criaDic()
        parent = []
        resultado = []
        #Chama a função auxiliar recursiva para achar os componentes na árvore de DFS com raiz no vértice i
        for key in self.graph.keys():
            if valores[key][1] == -1:
                resultado.append(self.Util(key, valores, parent))
        self.ImprimeResultado(resultado)
                
    def Util(self, u, valores, parent):
        #Marca o nó atual como visitado
        valores[u][0] = True
        #Inicializa o tempo de descoberta e o valor minimo
        valores[u][1] = self.T
        valores[u][2] = self.T
        self.T += 1
        parent.append(u)
        for v in self.graph[u]:			
            if valores[v][1] == -1 :
                self.Util(v, valores, parent)
                valores[u][2] = min(valores[u][2], valores[v][2])						
            elif valores[v][0] == True:
                valores[u][2] = min(valores[u][2], valores[v][1])
        w = -1
        aux = []
        if valores[u][2] == valores[u][1]:
            while w != u:
                w = parent.pop()             
                aux.append(w)
                valores[w][0] = False
            aux.sort()
        return(aux)

N = int(input())
for a in range(1,N+1):
    print(f'Case #{a}:')
    vertices = []
    V,E = map(int,input().split())
    graph = Graph(V)
    for i in range(65, V+65):
        graph.graph[chr(i).lower()] = []
    for i in range(E):
        A,B = map(str,input().split())
        graph.add(A,B)
    graph.Tarjan()
    
    
