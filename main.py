import csv
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
        #print("New depth")
        read_str(ind[2*len(list):], new_operator_list)
    else:
        return

def calculate_function(root, x_value):
    "No sé si hay que tener en cuenta la jerarquía de las operaciones (creo que no hace falta)"
    if root.value in operator:
        return operator[root.value](root.left, root.right, x_value)
    else:
        if type(root.value) == int:
            return root.value
        else:
            return x_value

def multiplication(arg1, arg2, x_value):
    if arg1.value in operator.keys():
        value1 = operator[arg1.value](arg1.left, arg1.right, x_value)
    else:
        if arg1.value != 'x':
            value1 = int(arg1.value)
        else:
            value1 = x_value
    if arg2.value in operator.keys():
        value2 = operator[arg2.value](arg2.left, arg2.right, x_value)
    else:
        if arg2.value != 'x':
            value2 = int(arg2.value)
        else:
            value2 = x_value
    #print("Multiplication:", value1, value2)
    return value1*value2

def addition(arg1, arg2, x_value):
    if arg1.value in operator.keys():
        value1 = operator[arg1.value](arg1.left, arg1.right, x_value)
    else:
        if arg1.value != 'x':
            value1 = int(arg1.value)
        else:
            value1 = x_value
    if arg2.value in operator.keys():
        value2 = operator[arg2.value](arg2.left, arg2.right, x_value)
    else:
        if arg2.value != 'x':
            value2 = int(arg2.value)
        else:
            value2 = x_value
    #print("Addition:", value1, value2)
    return value1+value2

def substraction(arg1, arg2, x_value):
    if arg1.value in operator.keys():
        value1 = operator[arg1.value](arg1.left, arg1.right, x_value)
    else:
        if arg1.value != 'x':
            value1 = int(arg1.value)
        else:
            value1 = x_value
    if arg2.value in operator.keys():
        value2 = operator[arg2.value](arg2.left, arg2.right, x_value)
    else:
        if arg2.value != 'x':
            value2 = int(arg2.value)
        else:
            value2 = x_value
    #print("Substraction:", value1, value2)
    return value1-value2

def division(arg1, arg2, x_value):
    if arg1.value in operator.keys():
        value1 = operator[arg1.value](arg1.left, arg1.right, x_value)
    else:
        if arg1.value != 'x':
            value1 = int(arg1.value)
        else:
            value1 = x_value
    if arg2.value in operator.keys():
        value2 = operator[arg2.value](arg2.left, arg2.right, x_value)
    else:
        if arg2.value != 'x':
            value2 = int(arg2.value)
        else:
            value2 = x_value
    #print("Division:", value1, value2)
    return value1/value2

class Node:
    def __init__(self, value):
        self.value = value
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

operator = {"+": addition, "-": substraction, "*": multiplication, "/": division}

list_values = []
file = open('function4.csv',newline='')
reader = csv.reader(file)

for row in reader:
    if row != []: #Sacamos del CSV los valores necesarios
        list_values.append(row)

print(list_values)

ind2 = list_values[1][0]
root = Node(ind2[0])
tree = Tree(root, ind2)

if ind2[0] in operator:
    operator_list = [root]
    read_str(ind2[1:], operator_list)

results = []
for i in list_values[2:]:
    new_y = calculate_function(root, float(i[0]))
    if float(i[1]) != new_y:
        print("Mal")
