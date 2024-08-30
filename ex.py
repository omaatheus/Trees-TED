#Busca em Profundidade

def createNode(data): #Função que recebe um valor
    return  { #retorna um objeto que contém:
        "data": data, #data contém o valor do nó
        "left": None, # os lados por padrão são vazios
        "right": None # idem
        }

def insertNodeOnNode(fatherNode, childNode, side): #Função que recebe o Nó Pai, Nó filho e o lado.
    if side == "left": #se o lado for esquerdo...
        fatherNode["left"] = childNode # atribui o nó filho ao lado esquerdo do nó pai
    elif side == "right": #se o lado for direito...
        fatherNode["right"] = childNode # atribui o nó filho ao lado direito do nó pai
    else: # Se não...
        print("Invalid side") # Imprime "Lado Inválido."

def findNode(node, searchedNode): #Função que recebe o nó atual e o nó que estamos procurando 
    if node == None: #Se o nó for nulo
        return None #retorne nada.
    
    if node ["data"] ==  searchedNode: #Se o nó atual for igual ao nó que estamos procurando
        print('Node found') #Retornamos que o nó não foi encontrado

    if node ["left"] != None: #Se o nó esquerdo for diferente de nulo
            findNode(node['left'], searchedNode) #Chama a função recursivamente para o nó esquerdo.

    if node ["right"] != None: #Se o nó direito for diferente de nulo
            findNode(node['right'], searchedNode) #Chama a função recursivamente para o no direito

    #Assumimos que, com a recursividade o nó atual é o lado que ele é procurado e então procuramos o nó que queremos, 
    #assim formando um loop até achar o que queremos.
    
    return None #Redundância, a função já teria que retornar Nulo caso não achasse nada.

#Busca em Largura
def bfs(node, searchedNode): #Função que recebe o nó atual e o nó que queremos procurar
     if node == None: #Se o nó for nulo
          return None #retorne nada.
     
     fila = [] #Criamos uma array vazia e definimos nome dela como fila
     fila.append(node) #Fila acessa o método append que atribui o nó através desse metódo.
     while len(fila) > 0: #Enquanto a quantidade de caracteres de fila for maior que 0
        current = fila.pop(0) #Variável recebe o método pop para remover e retornar o primeiro elemento da fila que é atribuido a variavel.
        if current['data'] == searchedNode: #Se o valor do nó atual for igual ao valor procurado
            print('Node found')#Imprime "Nó encontrado."

            print(current['data']) #Imprime o valor do nó

            if current ['left'] != None: #Se o nó tiver um filho a esquerda
                fila.append(current['left']) #Ele é adicionado a fila
    
            if current ['right'] != None: #Se o nó tiver um filho na direita
                fila.append(current['right']) #Ele é adicionado a fila