### ----- ÁRVORE DE BUSCA BINÁRIA  ----- ###

# Estrutura do nó
class Node:
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

def insert(root, value):
  if root is None:
    return Node(value)
  else:
    if value < root.value:
      root.left = insert(root.left, value)
    elif value > root.value:
      root.right = insert(root.right, value)
  return root 
  

# PERCURSOS EM PROFUNDIDADE (DFS)
def preOrdem(root):
  if root:
    print(root.value, end=" ")
    preOrdem(root.left)
    preOrdem(root.right)

def inOrdem(root):
  if root:
    inOrdem(root.left)
    print(root.value, end=" ")
    inOrdem(root.right)

def posOrdem(root):
  if root:
    posOrdem(root.left)
    posOrdem(root.right)
    print(root.value, end=" ")
    

# PERCURSOS EM LARGURA (BFS)  
import queue
q = queue.Queue()

def levelOrder(root):
  if root is None: return None
  q.put(root)
  while not q.empty():
    current = q.queue[0]
    print(current.value, end=" ")
    if current.left is not None: q.put(current.left)
    if current.right is not None: q.put(current.right)
    q.get() 

# Função para imprimir mais "bonitinho"
def printTree(root, level=0):
  if root is not None:
    printTree(root.right, level+1)
    print(' ' *4*level + '->' +str(root.value))
    printTree(root.left, level+1)

# Outras funções    
def findMin(root):
  if root is None:
    return None
  while root.left != None:
    root = root.left
  return root.value
  
def findMax(root):
  if root is None:
    return None
  while root.right != None:
    root = root.right
  return root.value

def findHeight(root):
  if root is None:
    return -1
  leftH = findHeight(root.left)
  rightH = findHeight(root.right)
  return max(leftH, rightH) + 1

def findRemoved(root, value):
  if root is None: return None #verificação se nulo
  elif value < root.value:
    root.left = findRemoved(root.left, value)
  elif value > root.value:
    root.right = findRemoved(root.right, value)
  else:
      # Caso 1: condição de nó unico (sem filhos, folha)
      if root.left and root.right is None:
        root = None
      # Caso 2: condição de nó com um filho
      # remoção pela esquerda
      elif root.left is None:
        temp = root # variavel temporaria para armazenar o valore que sera substituido
        root = root.right
        temp = None  
      # remoção pela esquerda
      elif root.right is None:
        temp = root # variavel temporaria para armazenar o valore que sera substituido
        root = root.left
        temp = None  
      # Caso 3: Condição de nó com dois filhos
      else:
        minNode = findMin(root.right)
        root.value = minNode.value
        root.right = findRemoved(root.right, minNode.value)
  return root
# ------ Main --------
root = None
root = insert(root, 55)
root = insert(root, 10)
root = insert(root, 15)
root = insert(root, 5)
root = insert(root, 6)
root = insert(root, 44)
root = insert(root, 28)
root = insert(root, 59)
root = insert(root, 0)
# preOrdem(root)
printTree(root)
print("Min: ",findMin(root))
print("Max: ",findMax(root))
print("Altura: ",findHeight(root))
levelOrder(root)

print("\n","\n")

findRemoved(root, 51)
printTree(root)