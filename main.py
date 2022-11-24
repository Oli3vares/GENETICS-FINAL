import csv
import math
import random
import time

NUMBERS_RANGE = 1000
TOURNAMENT_PROB = 0.5
SIZE = 2


def check_valid(ind):
    non_terminal = 0
    terminal = 0
    i = 0
    while i < len(ind):
        if ind[i] in operator_two.keys():
            non_terminal += 1
        elif ind[i] == '?':
            i += 1
            while ind[i] != '?':
                i += 1
            terminal += 1
        elif ind[i] == 'x':
            terminal += 1
        i += 1
    # print(terminal, non_terminal)
    if terminal - 1 != non_terminal:
        print(terminal, non_terminal)
        return False
    return True


def read_str(ind, list, num_children):
    new_operator_list = []
    children = 0
    father = 0
    new_children = 0
    elem_read = 0
    if num_children == 0:
        if list[father].value in operator_two.keys():
            new_children = 2
        else:
            new_children = 1
        new_operator_list.append(list[father])
        elem_read = 1
    while children < num_children:
        # se inserta el primer elemento como hijo del nodo x
        if list[father].value in operator_two.keys():
            # print("Str", ind[elem_read:], ind)
            output_elem = read_elem(ind[elem_read:])
            insert_node(list[father], output_elem[0])
            if output_elem[1] != 0:
                new_operator_list.append(list[father].left)
                new_children += output_elem[1]
            elem_read += len(output_elem[0])
            children += 1
            # se inserta el segundo elemento como hijo del nodo x
            # print("Str", ind[elem_read:], ind)
            output_elem = read_elem(ind[elem_read:])
            insert_node(list[father], output_elem[0])
            if output_elem[1] != 0:
                new_operator_list.append(list[father].right)
                new_children += output_elem[1]
            elem_read += len(output_elem[0])
            children += 1
            father += 1
            # si alguno de los elementos es un operador, se incluye en la nueva lista
        elif list[father].value in operator_one.keys():
            # print("Str", ind[elem_read:], ind)
            output_elem = read_elem(ind[elem_read:])
            insert_node(list[father], output_elem[0])
            if output_elem[1] != 0:
                new_operator_list.append(list[father].left)
                new_children += output_elem[1]
            elem_read += len(output_elem[0])
            children += 1
            father += 1
    if len(new_operator_list) != 0:
        read_str(ind[elem_read:], new_operator_list, new_children)
    return


def read_elem(string):
    read = 0
    if string[0] == '?':
        read = 1
        while string[read] != '?':
            read += 1
        gen_children = 0
        read += 1
        return string[:read], gen_children

    elif string[0] in operator_two.keys():
        gen_children = 2
    elif string[0] in operator_one.keys():
        gen_children = 1
    else:
        gen_children = 0
    return string[0], gen_children


def calculate_function(root, x_value):
    if root.value in operator_two.keys():
        # print(root.value)
        return operator_two[root.value](root.left, root.right, x_value)
    elif root.value in operator_one.keys():
        # print(root.value)
        return operator_one[root.value](root.left, x_value)
    else:
        if root.value != 'x':
            number = root.value[1:]
            value1 = int(number[:-1])
        else:
            value1 = float(x_value)
        return value1


def get_values(arg1, x_value, arg2=None):
    if arg1.value in operator_two.keys():
        value1 = operator_two[arg1.value](arg1.left, arg1.right, x_value)
    elif arg1.value in operator_one.keys():
        value1 = operator_one[arg1.value](arg1.left, x_value)
    else:
        if arg1.value != 'x':
            number = arg1.value[1:]
            value1 = int(number[:-1])
        else:
            value1 = float(x_value)
    if arg2 is not None:
        if arg2.value in operator_two.keys():
            value2 = operator_two[arg2.value](arg2.left, arg2.right, x_value)
        elif arg2.value in operator_one.keys():
            value2 = operator_one[arg2.value](arg2.left, x_value)
        else:
            if arg2.value != 'x':
                number = arg2.value[1:]
                value2 = int(number[:-1])
            else:
                value2 = float(x_value)
        # print(value1, value2)
        return value1, value2
    # print("Value",value1, arg1.value)
    return value1


def multiplication(arg1, arg2, x_value):
    values = get_values(arg1, x_value, arg2)
    # print("Arg1x", arg1)
    # print("Arg2x", arg2)
    # print("Multiplication:", value1, value2)7
    if not "False" in values:
        return values[0] * values[1]
    return "False"


def addition(arg1, arg2, x_value):
    values = get_values(arg1, x_value, arg2)
    # print("Arg1a", arg1)
    # print("Arg2a", arg2)
    # print("Addition:", value1, value2)
    if not "False" in values:
        return values[0] + values[1]
    return "False"


def substraction(arg1, arg2, x_value):
    values = get_values(arg1, x_value, arg2)
    # print("Arg1m", arg1)
    # print("Arg2m", arg2)
    # print("Substraction:", value1, value2)
    if not "False" in values:
        return values[0] - values[1]
    return "False"


def division(arg1, arg2, x_value):
    values = get_values(arg1, x_value, arg2)
    # print("Division:", value1, value2)
    # print("Arg1d", arg1)
    # print("Arg2d", arg2)
    if not "False" in values:
        if values[1] != 0:
            return values[0] / values[1]
        print("Division by zero")
    return "False"


def square_root(arg1, x_value):
    value = get_values(arg1, x_value)
    # print("Arg1s", arg1)
    if value != "False":
        if value >= 0:
            return math.sqrt(value)
        print("Negative sqrt")
    return "False"


def append_level(root, level, list_tree):
    if list_tree is None:
        list_tree = []
    if root is not None:
        orden = str(level) + ":" + root.value
        list_tree.append(orden)
        # print(level, root.value)
        level += 1
        append_level(root.left, level, list_tree)
        append_level(root.right, level, list_tree)

    return (list_tree)


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
    return (str_tree)


def generate_initial_population(size, max_depth, method):
    population_strings = []
    population_trees = []
    for i in range(0, size):
        population_strings.append(generate_individual(max_depth))
    for i in population_strings:
        new_root = Node(i[0])
        new_tree = Tree(new_root, i)
        population_trees.append(new_tree)
        read_str(i, [new_root], 0)
    return population_trees


def generate_individual(max_depth):
    actual_depth = 2
    new_depth_children = 0
    first_operator = random.choice(all_operators)
    if first_operator in operator_two.keys():
        new_children = 2
    else:
        new_children = 1
    new_ind = first_operator
    while actual_depth < max_depth:
        new_depth_children = 0
        for i in range(0, new_children):
            new_operator = random.choice(all_operators)
            if new_operator in operator_two.keys():
                new_depth_children += 2
            else:
                new_depth_children += 1
            new_ind += new_operator
        actual_depth += 1
        new_children = new_depth_children
    for i in range(0, new_depth_children):
        new_ind += gen_terminal()
    if check_valid(new_ind):
        return new_ind
    else:
        print("invalid")


def gen_terminal():
    if random.randint(0, 1):
        number = random.randint(1, NUMBERS_RANGE)
        element = "?" + str(number) + "?"
    else:
        element = "x"
    return element


def calculate_error(individual_root):
    cumulative_error = 0
    file = open('unknown_function_mid.csv', newline='')
    reader = csv.reader(file)

    for row in reader:
        if row[0] != "x":
            ind_result = calculate_function(individual_root, int(row[0]))
            if ind_result == "False":
                print("Individual not valid")
                return "Not valid"
            cumulative_error += abs(ind_result - int(row[1]))

    return cumulative_error


def choose_fighters(population):
    chosen_fighters = 0
    fighters = []
    numbers = []
    num_fighters = SIZE * TOURNAMENT_PROB
    print(num_fighters)
    while chosen_fighters < num_fighters:
        chosen = "a"
        # print(numbers)
        while chosen != "Chosen":
            index = random.randint(0, SIZE - 1)
            if index not in numbers:
                chosen = "Chosen"
                numbers.append(index)
        chosen_fighters += 1
    for indexes in numbers:
        fighters.append(population[indexes])
    return fighters


def get_error(fighter):
    return fighter[1]


def choose_parents(population):
    parent1 = min(choose_fighters(population), key=get_error)
    chosen = "A"
    print("Chosen")
    while chosen != "Chosen":
        parent2 = min(choose_fighters(population), key=get_error)
        if parent2[0].str != parent1[0].str:
            chosen = "Chosen"
    return parent1[0], parent2[0]


def crossing(parent1, parent2):
    children1_root = Node(parent1.str[0])
    children1 = Tree(children1_root, parent1.str)
    read_str(parent1.str, [children1_root], 0)
    children2_root = Node(parent2.str[0])
    children2 = Tree(children2_root, parent2.str)
    read_str(parent2.str, [children2_root], 0)
    print(children1)
    path1 = choose_path(
        children1)  # returns the path to the root of the subtree which is going to be modified, and the string of that subtree
    print(children2)
    path2 = choose_path(children2)
    modify_children(children1, path1[0][1:], path2[1])  # returns a tree with the modified children
    modify_children(children2, path2[0][1:], path1[1])
    # print("Parents\n", parent1, parent2)
    # print("Children\n",children1, children2)
    print(children1, children2)
    return children1, children2


def choose_path(child):
    path = ["BEG"]
    list_subtree = None
    str_subtree = None
    if child.root.right is not None:
        print("a")
        if random.randint(0, 1):
            print("a1", child.root.left.value)
            path.append("L")
            n_root = child.root.left
        else:
            print("a2", child.root.right.value)
            path.append("R")
            n_root = child.root.right
    else:
        print("b", child.root.left)
        path.append("L")
        print(child)
        n_root = child.root.left
    while path[-1] != "S":
        print("Entered")
        deviation = choose_deviation(n_root)
        n_root = deviation[0]
        path.append(deviation[1])
    list_subtree = append_level(n_root, 0, None)
    str_subtree = return_tree(list_subtree)
    print(path, str_subtree)
    return path, str_subtree


def choose_deviation(root):
    if root.right is not None:
        if random.randint(0, 2) == 0:
            root_dev = root.left
            new_path = "L"
        elif random.randint(0, 2) == 1:
            root_dev = root.right
            new_path = "R"
        else:
            return root, "S"
        return root_dev, new_path
    elif root.left is not None:
        if random.randint(0, 1):
            new_path = "L"
            root_dev = root.left
            return root_dev, new_path
        else:
            return root, "S"
    return root, "S"


def modify_children(children, path, string):
    root = children.root
    for i in path[:-1]:
        if i == "L":
            root = root.left
        else:
            root = root.right
    root.value = string[0]
    replace_str(string, [root], 0)
    return


def replace_str(ind, list, num_children):
    new_operator_list = []
    children = 0
    father = 0
    new_children = 0
    elem_read = 0
    if num_children == 0:
        if list[father].value in operator_two.keys():
            new_children = 2
            new_operator_list.append(list[father])
        elif list[father].value in operator_one.keys():
            new_children = 1
            new_operator_list.append(list[father])
        else:
            new_children = 0
        elem_read = 1
        list[father].left = None
        list[father].right = None
    while children < num_children:
        # se inserta el primer elemento como hijo del nodo x
        if list[father].value in operator_two.keys():
            # print("Str", ind[elem_read:], ind)
            output_elem = read_elem(ind[elem_read:])
            replace_node(list[father], output_elem[0], 0)
            if output_elem[1] != 0:
                new_operator_list.append(list[father].left)
                new_children += output_elem[1]
            elem_read += len(output_elem[0])
            children += 1
            # se inserta el segundo elemento como hijo del nodo x
            # print("Str", ind[elem_read:], ind)
            output_elem = read_elem(ind[elem_read:])
            replace_node(list[father], output_elem[0], 1)
            if output_elem[1] != 0:
                new_operator_list.append(list[father].right)
                new_children += output_elem[1]
            elem_read += len(output_elem[0])
            children += 1
            father += 1
            # si alguno de los elementos es un operador, se incluye en la nueva lista
        elif list[father].value in operator_one.keys():
            # print("Str", ind[elem_read:], ind)
            output_elem = read_elem(ind[elem_read:])
            replace_node(list[father], output_elem[0], 0)
            if output_elem[1] != 0:
                new_operator_list.append(list[father].left)
                new_children += output_elem[1]
            elem_read += len(output_elem[0])
            children += 1
            father += 1
    if len(new_operator_list) != 0:
        replace_str(ind[elem_read:], new_operator_list, new_children)
    return


def pairing(population):
    new_population = []
    for i in range(0, int(len(population) / 2)):
        parents = choose_parents(population)
        children = crossing(parents[0], parents[1])
        new_population.append(children[0])
        new_population.append(children[1])
    return new_population


def mutate(population):
    new_population = []
    for i in population:
        mutated_tree = mutation_non_terminal_simple(i)
        new_population.append(mutated_tree)
    return new_population


def mutation_terminal_simple(tree):
    print("Not mutated", tree)
    node = tree.root
    terminal_chosen = False
    while not terminal_chosen:
        if node.left is None:
            print(node.value)
            terminal_chosen = True
        elif node.right is None:
            node = node.left
        else:
            if random.randint(0, 1):
                node = node.left
            else:
                node = node.right
    if random.randint(0, 1):
        node.value = "x"
    else:
        number = random.randint(1, NUMBERS_RANGE)
        node.value = "?" + str(number) + "?"
    print("Mutated", tree)
    return tree


def mutation_non_terminal_simple(tree):
    print("Not mutated", tree)
    non_terminal_chosen = False
    while not non_terminal_chosen:
        node = tree.root
        terminal_chosen = False
        while not terminal_chosen:
            if node.left is None:
                terminal_chosen = True
            elif node.right is None:
                if random.randint(0, 1):
                    print("Value to mutate v1", node.value)
                    terminal_chosen = True
                    non_terminal_chosen = True
                else:
                    node = node.left
            else:
                if random.randint(0, 2) == 0:
                    node = node.left
                elif random.randint(0, 2) == 1:
                    node = node.right
                else:
                    print("Value to mutate", node.value)
                    terminal_chosen = True
                    non_terminal_chosen = True
    if node.value in operator_two.keys():
        new_op = random.choice(all_operators)
        if new_op in operator_one.keys():
            node.right = None
        node.value = new_op
    else:
        pass
        # print("Can´t mutate (og non_terminal sqrt, no other one child operator)")

    print("Mutated", tree)
    return tree


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.value) + "\n"
        if self.left != None:
            ret += self.left.__repr__(level + 1)
        if self.right != None:
            ret += self.right.__repr__(level + 1)
        return ret


class Tree:
    def __init__(self, node, str):
        self.root = node
        self.str = str

    def __str__(self):
        return (str(self.root))


def create_node(value):
    return Node(value)


def insert_node(root, node):
    if root.left is None:
        root.left = create_node(node)
    else:
        root.right = create_node(node)


def replace_node(root, node, pos):
    if pos == 0:
        root.left = create_node(node)
        root.left.left = None
        root.left.right = None
    else:
        root.right = create_node(node)
        root.right.left = None
        root.right.right = None


operator_two = {"+": addition, "-": substraction, "*": multiplication, "/": division}
operator_one = {"s": square_root}
all_operators = ["+", "-", "*", "/", "s"]

population = generate_initial_population(SIZE, 4, "a")
j = 0
incorrect = 0
while j < len(population):
    # print(population[j].str)
    result = calculate_error(population[j].root)
    if result == "Not valid":
        population.remove(population[j])
        new_ind = generate_individual(4)
        new_root = Node(new_ind[0])
        new_tree = Tree(new_root, new_ind)
        # print("new ind")
        population.append(new_tree)
        read_str(new_ind, [new_root], 0)
        incorrect += 1
    else:
        population[j] = [population[j], result]
        j += 1
        # print(result)
print(len(population))
new_pop = pairing(population)
mutated_pop = mutate(new_pop)