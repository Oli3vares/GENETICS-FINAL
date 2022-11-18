import csv
def read_str(ind, list, num_children):
    new_operator_list = []
    children = 0
    i = 0
    new_children = 0
    while children < num_children:
        #se inserta el primer elemento como hijo del nodo x
        if list[0] in operator_two:
            tree.insert_node(list[i], ind[children])
            if ind[children] in operator_two:
                new_operator_list.append(list[i].left)
                new_children += 2
            elif ind[children] in operator_one:
                new_operator_list.append(list[i].left)
                new_children += 1
            children += 1
            #se inserta el segundo elemento como hijo del nodo x
            tree.insert_node(list[i], ind[children])
            if ind[children] in operator_two:
                new_operator_list.append(list[i].left)
                new_children += 2
            elif ind[children] in operator_one:
                new_operator_list.append(list[i].left)
                new_children += 1
            children += 1
            i += 1
            #si alguno de los elementos es un operador, se incluye en la nueva lista
        elif list[0] in operator_one:
            tree.insert_node(list[i], ind[children])
            if ind[children] in operator_two:
                new_operator_list.append(list[i].left)
                new_children += 2
            elif ind[children] in operator_one:
                new_operator_list.append(list[i].left)
                new_children += 1
            children += 1
            i += 1
    if len(new_operator_list) != 0:
        #print("New depth")
        read_str(ind[2*len(list):], new_operator_list, new_children)
    else:
        return

def calculate_function(root, x_value):
    if root.value in operator_two.keys():
        return operator_two[root.value](root.left, root.right, x_value)
    elif root.value in operator_one.keys():
        return operator_one[root.value](root.left, x_value)
    else:
        if type(root.value) == int:
            return root.value
        else:
            return x_value


def get_values(arg1, arg2, x_value):
    if arg1.value in operator_two.keys():
        value1 = operator_two[arg1.value](arg1.left, arg1.right, x_value)
    elif arg1.value in operator_one.keys():
        return operator_one[arg1.value](arg1.left, x_value)
    else:
        if arg1.value != 'x':
            value1 = int(arg1.value)
        else:
            value1 = x_value
    if arg2.value in operator_two.keys():
        value2 = operator_two[arg2.value](arg2.left, arg2.right, x_value)
    elif arg2.value in operator_one.keys():
        value2 = operator_one[arg2.value](arg2.left, x_value)
    else:
        if arg2.value != 'x':
            value2 = int(arg2.value)
        else:
            value2 = x_value
    return value1, value2
def multiplication(arg1, arg2, x_value):
    values = get_values(arg1, arg2, x_value)
    #print("Multiplication:", value1, value2)
    return values[0]*values[1]

def addition(arg1, arg2, x_value):
    values = get_values(arg1, arg2, x_value)
    #print("Addition:", value1, value2)
    return values[0]+values[1]

def substraction(arg1, arg2, x_value):
    values = get_values(arg1, arg2, x_value)
    #print("Substraction:", value1, value2)
    return values[0]-values[1]

def division(arg1, arg2, x_value):
    values = get_values(arg1, arg2, x_value)
    #print("Division:", value1, value2)
    return values[0]/values[1]

def square_root():
    pass

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

operator_two = {"+": addition, "-": substraction, "*": multiplication, "/": division}
operator_one = {"s": square_root}


list_values = []
file = open('function1.csv',newline='')
reader = csv.reader(file)

for row in reader:
    if row != []: #Sacamos del CSV los valores necesarios
        list_values.append(row)

print(list_values)

ind2 = list_values[1][0]
root = Node(ind2[0])
tree = Tree(root, ind2)

if ind2[0] in operator_two:
    operator_list = [root]
    read_str(ind2[1:], operator_list)

results = []
for i in list_values[2:]:
    new_y = calculate_function(root, float(i[0]))
    if float(i[1]) != new_y:
        print("Mal")
