class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def insertNode(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insertNode(root.left, value)
        elif value > root.value:
            root.right = insertNode(root.right, value)
    return root

          
#->percursos de profundidade<-
def preOrdem(root):
    if root:
        print(root.value, end = " ")
        preOrdem(root.left)
        preOrdem(root.right)

def inOrdem(root):
    if root:
        inOrdem(root.left)
        print(root.value, end = " ")
        inOrdem(root.right)

def posOrdem(root):
    if root:
        posOrdem(root.left)
        posOrdem(root.right)
        print(root.value, end = " ")


#->printando a arvore de ladinho<-
def printTree(root, level = 0):
    if root is not None:
        printTree(root.right, level+1)
        print(' ' * 4*level + '->' + str(root.value))
        printTree(root.left, level+1)


#->achar o menor valor da arvore<-
def findMin(root):
    if root is None:
        return None
    while root.left != None:
        root = root.left
    return root


#->achar o maior valor da arvore<-
def findMax(root):
    if root is None:
        return None
    while root.right != None:
        root = root.right
    return root


#->achar a altura total da arvore<-
def findHeight(root):
  if root is None:
      return 1
  leftH = findHeight(root.left)
  rightH = findHeight(root.right)
  return max(leftH, rightH) + 1

#->remover 1 node da arvore<-
def deleteNode(root, value):
    if root is None: return root
    
    #se o valor a ser deletado for menor que root então ele está à esquerda de root
    elif (value < root.value):
        root.left = deleteNode(root.left, value)
    
    #se o valor a ser deletado for maior que root entao ele fica à direita de root
    elif(value > root.value):
        root.right = deleteNode(root.right, value)

    #se o valor a ser deletado é igual a root entao esse valor SERÁ deletado
    else:

        #código do prof
        #Caso1: Nó sem filhos(folha)
        if root.left and root.right is None:
            root = None
            return root
        
        #caso2: Nó com 1 filho
        elif root.left is None:
            temp = root
            root = root.right
            temp = None
            return root
        elif root.right is None:
            temp = root
            root = root.left
            temp = None
            return root
        else:

            # if root.left is None: #TENTATIVA 1 -FUNCIONA- funciona pro caso 1 e 2 de uma vez só
            #     temp = root.right
            #     root = None
            #     return temp
            # elif root.right is None:
            #     temp = root.left
            #     root = None
            #     return temp

            #Caso3: Nó com 2 filhos
            #pegamos o sucessor em ordem crescente que é o menor nó na subarvore direita
            temp = findMin(root.right)

            #daí pegamos o sucessor em ordem crescente e passamos para o valor de root
            root.value = temp.value

            #e deletamos o sucessor em ordem
            root.right = deleteNode(root.right, temp.value)
    return root

#->percurso em level(BFS)<-
import queue
q = queue.Queue()
def levelOrder(root):
    if root is None: return None
    q.put(root)
    while not q.empty():
        current = q.queue[0]
        print(current.value, end = " ")
        if current.left is not None: q.put(current.left)
        if current.right is not None: q.put(current.right)
        q.get()


#->!implementando a arvore!<-
root = None
root = insertNode(root, 10)
root = insertNode(root, 15)
root = insertNode(root, 20)
root = insertNode(root, 23)
root = insertNode(root, 25)
root = insertNode(root, 28)
root = insertNode(root, 32)
root = insertNode(root, 40)
root = insertNode(root, 55)
root = insertNode(root, 82)
root = insertNode(root, 87)
root = insertNode(root, 90)
root = insertNode(root, 100)

print("agora trabalhando com exclusão de nós!")
print("vamos deletar o 40!")
deleteNode(root, 40)
print("printando a arvore em sí:")
printTree(root)