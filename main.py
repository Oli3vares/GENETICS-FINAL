import csv
import math


def read_str(ind, list, num_children):
    new_operator_list = []
    children = 0
    father = 0
    new_children = 0
    while children < num_children:
        #se inserta el primer elemento como hijo del nodo x
        if list[father].value in operator_two.keys():
            tree.insert_node(list[father], ind[children])
            if ind[children] in operator_two.keys():
                new_operator_list.append(list[father].left)
                new_children += 2
            elif ind[children] in operator_one.keys():
                new_operator_list.append(list[father].left)
                new_children += 1
            children += 1
            #se inserta el segundo elemento como hijo del nodo x
            tree.insert_node(list[father], ind[children])
            if ind[children] in operator_two.keys():
                new_operator_list.append(list[father].right)
                new_children += 2
            elif ind[children] in operator_one.keys():
                new_operator_list.append(list[father].right)
                new_children += 1
            children += 1
            father += 1
            #si alguno de los elementos es un operador, se incluye en la nueva lista
        elif list[father].value in operator_one.keys():
            tree.insert_node(list[father], ind[children])
            if ind[children] in operator_two.keys():
                new_operator_list.append(list[father].left)
                new_children += 2
            elif ind[children] in operator_one.keys():
                new_operator_list.append(list[father].left)
                new_children += 1
            children += 1
            father += 1
    if len(new_operator_list) != 0:
        #print("New depth")
        read_str(ind[children:], new_operator_list, new_children)
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

def get_value(arg1, x_value):
    if arg1.value in operator_two.keys():
        value1 = operator_two[arg1.value](arg1.left, arg1.right, x_value)
    elif arg1.value in operator_one.keys():
        return operator_one[arg1.value](arg1.left, x_value)
    else:
        if arg1.value != 'x':
            value1 = int(arg1.value)
        else:
            value1 = x_value
    return value1
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

def square_root(arg1, x_value):
    value = get_value(arg1, x_value)
    return math.sqrt(value)
     
        
def append_level(root, level=0, list_tree=[]):
    if root is not None:
        orden = str(level) + ":" + root.value 
        list_tree.append(orden)
        #print(level, root.value)
        level += 1
        append_level(root.left, level)
        append_level(root.right, level)
        
    return(list_tree)


def return_tree(list_tree):
    l_tree = []
    str_tree = ""
    list_level = []
    list_value = []
    
    for i in range(len(list_tree)):
        node = list_tree[i].split(', ')
        l_level = [item.split(':', 1)[0] for item in node]
        l_value = [item.split(':', 1)[1] for item in node]
        level = [int(x) for x in l_level]
        value = "".join(l_value)
        list_level.append(level[0])
        list_value.append(value)
    x = 0
    while x in list_level:
        cont = 0
        for i in list_level:
            if i == x:
                l_tree.append(list_value[cont])
                
            cont += 1
        x += 1

    str_tree = "".join(l_tree)
    return(str_tree)
    
        
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
file = open('function4.csv',newline='')
reader = csv.reader(file)

for row in reader:
    if row != []: #Sacamos del CSV los valores necesarios
        list_values.append(row)

#print(list_values)

ind2 = list_values[1][0]
root = Node(ind2[0])
tree = Tree(root, ind2)

if ind2[0] in operator_two:
    operator_list = [root]
    #print(operator_list)
    read_str(ind2[1:], operator_list, 2)
elif ind2[0] in operator_one:
    operator_list = [root]
    read_str(ind2[1:], operator_list, 1)

results = []
for i in list_values[2:]:
    new_y = calculate_function(root, float(i[0]))
    if float(i[1]) != new_y:
        print("Mal")

        
l_tree = append_level(tree.root)
str_tree = return_tree(l_tree)
print(str_tree)

