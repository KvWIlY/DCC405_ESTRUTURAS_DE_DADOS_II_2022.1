import re

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)
def unival_count(root):
    if root == None:
        return True, 0
    if root.left == None and root.right == None:
        return True, 1
    
    l_val, left_val = unival_count(root.left)
    r_val, right_val = unival_count(root.right)
    if l_val and r_val:
        if (root.left == None and root.right.val == root.val) or (root.right == None and root.left.val == root.val) or (root.left.val == root.val and root.right.val == root.val):
            return True, left_val + right_val + 1
    return False, left_val + right_val

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, node_val):
        self.root = self.__create__(node_val)
    def __create__(self, node_val):
        pattern = re.compile(r'null')
        if len(node_val) != 0:
            n = node_val.pop(0)
            if  pattern.findall(n):
                return None
            root = Node(n)
            root.left = self.__create__(node_val)
            root.right = self.__create__(node_val)
            return root
        else:
            return None
    def Print(self):
        print_tree(self.root)
    def find_unival(self):
        return unival_count(self.root)
    

if __name__ == '__main__':
    string = input()
    string = string[1:-1].split(',')
    print("Tree - \n\n")
    tree = Tree(string)
    tree.Print()
    print("\n\nNumber of unival subtrees - {}".format(tree.find_unival()[1]))