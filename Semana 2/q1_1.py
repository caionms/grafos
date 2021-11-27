#Classe do nó da binary tree
class Node:
    def __init__(self, value): #Função para inicializar o nó
        self.left = None
        self.right = None
        self.value = value

    def insert(root, value): #Método para inserir um novo no iterativamente
        #Cria o novo nó a ser inserido
        r = Node(value)
        #Ponteiro usado para chegar da raiz a posição do novo nó
        x = root
        #Ponteiro para controle no percurso
        y = None
        #Loop para chegar na posição do novo nó
        while x!= None:
            y = x
            if value < x.value:
                x = x.left
            else:
                x = x.right
        #Caso a árvore esteja vazia
        if y == None:
            y = r
        #Caso o valor da folha seja maior que o nó, esse ficará na esquerda dela
        elif value < y.value:
            y.left = r
        #Caso o valor da folha seja menor que o nó, esse ficará na direita dela
        else:
            y.right = r
        #Retorna a posição de onde o novo nó foi inserido
        return y

    def preorder(self, root): #Função para fazer a impressão pre
        res = []
        if root:
            res.append(root.value)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def inorder(self, root): #Função para fazer a impressão in
        res = []
        if root:
            res = res + self.inorder(root.left)
            res.append(root.value)
            res = res + self.inorder(root.right)
        return res

    def postorder(self, root): #Função para fazer a impressão post
        res = []
        if root:
            res = res + self.postorder(root.left)
            res = res + self.postorder(root.right)
            res.append(root.value)
        return res

#Quantidade de casos teste
c = int(input())
#Roda os casos testes
for i in range(c):
    #Pega a quantidade de nós de cada caso teste
    n = int(input())
    #Pega os valores dos nós
    valores = [int(valor) for valor in input().split(' ')]
    #Coloca o valor da raiz como o primeiro input
    root = Node(valores[0])
    #Faz um loop para adicionar cada valor nó na árvore
    for valor in valores[1:]:
        #Adiciona o nó atual na árvore
        root.insert(valor)

    print(f"Case {i+1}:")
    #Preenche as variáveis com as listas de valores
    valorespre = root.preorder(root)
    valoresin = root.inorder(root)
    valorespost = root.postorder(root)

    #Formata as listas para String
    valorespre = " ".join([str(v) for v in valorespre])
    valoresin = " ".join([str(v) for v in valoresin])
    valorespost = " ".join([str(v) for v in valorespost])

    #Imprime os valores no padrão da questão
    print(f"Pre.: {valorespre}")
    print(f"In..: {valoresin}")
    print(f"Post: {valorespost}")
    print("")
