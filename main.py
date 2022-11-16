def read_str(ind, list):
    new_operator_list = []
    for i in range(0, 2*len(list), 2):
        #se inserta el primer elemento como hijo del nodo x
        tree.insert_node(list[int((i)/2)], ind[i])
        #se inserta el segundo elemento como hijo del nodo x
        tree.insert_node(list[int((i)/2)], ind[i+1])
        #si alguno de los elementos es un operador, se incluye en la nueva lista
        if ind[i] in operator:
            new_operator_list.append(list[int((i)/2)].left)
        if ind[i+1] in operator:
            new_operator_list.append(list[int((i)/2)].right)
    if len(new_operator_list) != 0:
        print("New depth")
        read_str(ind[2*len(list):], new_operator_list)
    else:
        return

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, node, str):
        self.root = node
        self.str = str

    def create_node(self, value):
        return Node(value)

    def insert_node(self, root, node):
        if root.left is None:
            root.left = self.create_node(node)
        else:
            root.right = self.create_node(node)

operator = ["+", "-", "*", "/"]
ind = "+a/b2"
root = Node(ind[0])
tree = Tree(root, ind)
if ind[0] in operator:
    operator_list = [root]
    read_str(ind[1:], operator_list)

print(root.data)
print(root.right.left.data)

