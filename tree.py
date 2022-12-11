# Uma Arvore Basica
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
         
# Função que soma todos os valores da arvore
def find_sum(root):
    if (root == None):
        return 0
    return (root.data + find_sum(root.left) + find_sum(root.right))

# contador Unival
def count_unival_subtree(root):
    count, _ = cont_aux(root)
    return count

# Retorna o número de subárvores univais e se ela própria é uma subárvore unival.
def cont_aux(root):
    if (root is None):
        return 0, True
    
    # como a função cont_aux vai retornar um interio e um bool,criemos ariaveis para as mesmas.
    left_count, B_left_unival = cont_aux(root.left)
    right_count, B_right_unival = cont_aux(root.right)
    #calculando o total
    total_count = left_count + right_count

    if (B_left_unival and B_right_unival):
        if (root.left is not None and root.data != root.left.data):
            return total_count, False
        if (root.right is not None and root.data != root.right.data):
            return total_count, False
        return total_count + 1, True
    return total_count, False


if __name__ == '__main__':
    #criando a arvore para a 1° questão

    # root = Node(2)
    # root.left = Node(3)
    # root.right = Node(4)
    # root.left.left = Node(5)
    # root.left.right = Node(6)

    # print("Soma de todos as Chaves da Árvore: ", find_sum(root))
    
    #criando a arvore para a 2° questão
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(1)
    root.right.right = Node(0)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)

    print("Total de Subtrees: ",count_unival_subtree(root))
 
