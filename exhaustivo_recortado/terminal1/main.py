import csv
import math
import random
import sys
import time



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
        #print(terminal, non_terminal)
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
            value1 = float(number[:-1])
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
            value1 = float(number[:-1])
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
                value2 = float(number[:-1])
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
        mult_value = values[0] * values[1]
        if type(mult_value) is complex:
            print("mult complex")
            return "False"
        else:
            return mult_value
    return "False"


def addition(arg1, arg2, x_value):
    values = get_values(arg1, x_value, arg2)
    # print("Arg1a", arg1)
    # print("Arg2a", arg2)
    # print("Addition:", value1, value2)
    if not "False" in values:
        add_value = values[0] + values[1]
        if type(add_value) is complex:
            print("add complex")
            return "False"
        else:
            return add_value
    return "False"


def substraction(arg1, arg2, x_value):
    values = get_values(arg1, x_value, arg2)
    # print("Arg1m", arg1)
    # print("Arg2m", arg2)
    # print("Substraction:", value1, value2)
    if not "False" in values:
        sub_value = values[0] - values[1]
        if type(sub_value) is complex:
            print("sub complex")
            return "False"
        else:
            return sub_value
    return "False"


def division(arg1, arg2, x_value):
    values = get_values(arg1, x_value, arg2)
    # print("Division:", value1, value2)
    # print("Arg1d", arg1)
    # print("Arg2d", arg2)
    if not "False" in values:
        if values[1] != 0:
            div_value = values[0] / values[1]
            if type(div_value) is complex:
                print("div complex")
                return "False"
            else:
                return div_value
        #print("Division by zero")
    return "False"


def square_root(arg1, x_value):
    value = get_values(arg1, x_value)
    # print("Arg1s", arg1)
    if value != "False":
        if type(value) is complex:
            print(value)
        if value >= 0:
            sqrt_value = math.sqrt(value)
            if type(sqrt_value) is complex:
                print("sqrt complex")
                return "False"
            else:
                return sqrt_value
        #print("Negative sqrt")
    return "False"


def power(arg1, arg2, x_value):
    # y = e^x
    values = get_values(arg1, x_value, arg2)
    if not "False" in values:
        try:
            pow_value = values[0] / values[1]
            if type(pow_value) is complex:
                print("pow complex")
                return "False"
            else:
                return pow_value
        except:
            print("Math range error")
            return "False"
    return "False"


def logarithm(arg1, x_value):
    value = get_values(arg1, x_value)
    if value != "False":
        if value > 0:
            log_value = math.log(value)
            if type(log_value) is complex:
                print("log complex")
                return "False"
            else:
                return log_value
        else:
            return "False"
    return "False"


def sine(arg1, x_value):
    value = get_values(arg1, x_value)
    # print("Arg1s", arg1)
    if value != "False":
        try:
            sine_value = math.sin(value)
            if type(sine_value) is complex:
                print("Sine complex")
                return "False"
            else:
                return sine_value
        except:
            return "False"

    return "False"


def cosine(arg1, x_value):
    value = get_values(arg1, x_value)
    # print("Arg1s", arg1)
    if value != "False":
        try:
            cosine_value = math.cos(value)
            if type(cosine_value) is complex:
                print("Cosine complex")
                return "False"
            else:
                return cosine_value
        except:
            return "False"
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
    if method == "full":
        population_strings = []
        population_trees = []
        for i in range(0, size):
            population_strings.append(generate_individual(max_depth))
        for i in population_strings:
            new_root = Node(i[0])
            new_tree = Tree(new_root, i)
            population_trees.append(new_tree)
            read_str(i, [new_root], 0)

    else:
        population_strings = []
        population_trees = []
        for i in range(0, size):
            population_strings.append(generate_ind_grow(max_depth))
        for i in population_strings:
            new_root = Node(i[0])
            new_tree = Tree(new_root, i)
            population_trees.append(new_tree)
            read_str(i, [new_root], 0)
    #print(population_strings[0])
    #print(population_trees[0])
    return population_trees

def generate_ind_grow(max_depth):
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
            new_operator = random.choice(all_elements)
            if new_operator in operator_two.keys():
                new_depth_children += 2
                new_ind += new_operator
            elif new_operator in operator_one.keys():
                new_depth_children += 1
                new_ind += new_operator
            else:
                new_ind += gen_terminal()

        actual_depth += 1
        new_children = new_depth_children
    for i in range(0, new_depth_children):
        new_ind += gen_terminal()
    if check_valid(new_ind):
        return new_ind
    else:
        print("invalid")


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
        if not FLOAT_RANGE:
            number = random.randint(0, NUMBERS_RANGE)
        else:
            number = random.random()
        element = "?" + str(number) + "?"
    else:
        element = "x"
    return element


def calculate_error(individual_root):
    cumulative_error = 0
    file = open('unknown_function_mid.csv', newline='')
    reader = csv.reader(file)
    data_points = 0
    for row in reader:
        if row[0] != "x":
            ind_result = calculate_function(individual_root, int(row[0]))
            if ind_result == "False":
                #print("Individual not valid")
                return "Not valid"
            try:
                cumulative_error += abs(ind_result - int(row[1]))
            except OverflowError:
                return "Not valid"
            if type(cumulative_error) is complex:
                print(cumulative_error, ind_result)
            data_points += 1
    cumulative_error = ((1/data_points)*cumulative_error)
    return cumulative_error


def choose_fighters(population):
    chosen_fighters = 0
    fighters = []
    numbers = []
    num_fighters = SIZE * TOURNAMENT_PROB
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
    #print("Chosen")
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
    #print(children1)
    path1 = choose_path(
        children1)  # returns the path to the root of the subtree which is going to be modified, and the string of that subtree
    #print(children2)
    path2 = choose_path(children2)
    modify_children(children1, path1[0][1:], path2[1])  # returns a tree with the modified children
    modify_children(children2, path2[0][1:], path1[1])
    list_subtree = append_level(children1.root, 0, None)
    children1.str = return_tree(list_subtree)
    list_subtree = append_level(children2.root, 0, None)
    children2.str = return_tree(list_subtree)
    # print("Parents\n", parent1, parent2)
    # print("Children\n",children1, children2)
    #print(children1, children2)
    return children1, children2


def choose_path(child):
    path = ["BEG"]
    list_subtree = None
    str_subtree = None
    if child.root.right is not None:
        #print("a")
        if random.randint(0, 1):
            #print("a1", child.root.left.value)
            path.append("L")
            n_root = child.root.left
        else:
            #print("a2", child.root.right.value)
            path.append("R")
            n_root = child.root.right
    else:
        #print("b", child.root.left)
        path.append("L")
        #print(child)
        n_root = child.root.left
    while path[-1] != "S":
        #print("Entered")
        deviation = choose_deviation(n_root)
        n_root = deviation[0]
        path.append(deviation[1])
    list_subtree = append_level(n_root, 0, None)
    str_subtree = return_tree(list_subtree)
    #print(path, str_subtree)
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
    if string[0] != "?":
        root.value = string[0]
    else:
        i = 1
        finished = False
        while not finished:
            if string[i] == "?":
                finished = True
            i += 1
        root.value = string[:i]
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
        elite_size = ELITE*SIZE
        if (elite_size)%2 == 1:
            elite_size -= 1
        if i < (elite_size):
            new_population.append(population[2*i][0])
            new_population.append(population[2*i+1][0])
        else:
            parents = choose_parents(population)
            children = crossing(parents[0], parents[1])
            new_population.append(children[0])
            new_population.append(children[1])
    return new_population


def mutate(population):
    new_population = []
    for i in population:
        rand = random.random()
        if rand <= MUTATION_PROB:
            if MUTATION_NUM == 1:
                mutated_tree = mutation_non_terminal_simple(i)
            elif MUTATION_NUM == 2:
                mutated_tree = mutation_terminal_simple(i)
            elif MUTATION_NUM == 3:
                mutated_tree = mutation_arbol(i)
            list_subtree = append_level(mutated_tree.root, 0, None)
            mutated_tree.str = return_tree(list_subtree)
            new_population.append(mutated_tree)
        else:
            new_population.append(i)
    return new_population


def mutation_terminal_simple(tree):
    #print("Not mutated", tree)
    node = tree.root
    terminal_chosen = False
    while not terminal_chosen:
        if node.left is None:
            #print(node.value)
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
        if not FLOAT_RANGE:
            number = random.randint(0, NUMBERS_RANGE)
        else:
            number = random.random()
        node.value = "?" + str(number) + "?"
    #print("Mutated", tree)
    return tree


def mutation_non_terminal_simple(tree):
    #print("Not mutated", tree)
    non_terminal_chosen = False
    while not non_terminal_chosen:
        node = tree.root
        terminal_chosen = False
        while not terminal_chosen:
            if node.left is None:
                terminal_chosen = True
            elif node.right is None:
                if random.randint(0, 1):
                    #print("Value to mutate v1", node.value)
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
                    #print("Value to mutate", node.value)
                    terminal_chosen = True
                    non_terminal_chosen = True
    chosen = False
    if node.value in operator_two.keys():
        while not chosen:
            #print("new_op",random.choice(list(operator_two.keys())))
            new_op = random.choice(list(operator_two.keys()))
            if new_op != node.value:
                chosen = True
                
    if node.value in operator_one.keys():
        while not chosen:
            new_op = random.choice(list(operator_one.keys()))
            if new_op != node.value:
                chosen = True
                
    else:
        pass
        # print("Can´t mutate (og non_terminal sqrt, no other one child operator)")
    #print("NO", new_op)
    node.value = new_op
    #print("Mutated", tree)
    return tree

def mutation_arbol(tree):
    #print("Not mutated", tree)
    # print("Not mutated", tree)
    non_subtree_chosen = False
    node = tree.root
    while not non_subtree_chosen:
            #print(node.value)
            next_action = random.randint(0, 2)
            if next_action == 0 and node != tree.root:
                if node.left != None:
                    node = node.left
                else: #Es terminal
                    node = tree.root

            elif next_action == 1 and node != tree.root and node.value not in operator_one:
                if node.right != None:
                    node = node.right
                else: #Es terminal
                    node = tree.root

            elif next_action == 2 and node != tree.root:
                    #print("Whey ", node.value)
                    node.left = None
                    if node.value not in operator_one:
                        node.right = None
                    #insertar nuevo arbol

                    new_ind = generate_individual(DEPTH)
                    node.value = new_ind[0]
                    new_tree = Tree(node, new_ind)
                    # print("new ind")
                    read_str(new_ind, [node], 0)


                    non_subtree_chosen = True

            else:
                if random.randint(0, 1) == 0 or node.value in operator_one:
                    node = node.left
                else:
                    node = node.right
    #print("Mutated", tree)
    return tree

def save_data_experiment(error = None):
    if error != None:
        file = open('all_experiments.csv', 'a')
        writer = csv.writer(file)
        data = [error, DEPTH, MUTATION_NUM, GENERATION_TYPE, SIZE, MUTATION_PROB, TOURNAMENT_PROB, ELITE, NUMBERS_RANGE, all_operators]
        writer.writerow(data)
        file.close()
    else:
        file = open('errors/error' + str(EXPERIMENT_NUMBER) + '.csv', 'a')
        writer = csv.writer(file)
        data = [DEPTH, MUTATION_NUM, GENERATION_TYPE, SIZE, MUTATION_PROB, TOURNAMENT_PROB, ELITE, NUMBERS_RANGE,
                all_operators]
        writer.writerow(data)

def save_data_cycles(population):
    error_best = get_error(population[0])
    top5percent = int(0.05 * SIZE)
    error_top5percent = 0
    error_total = 0
    operator_two = {"+": addition, "-": substraction, "*": multiplication, "/": division, "p": power}
    operator_one = {"r": square_root, "s": sine, "c": cosine, "l": logarithm}
    add_times = 0
    sub_times = 0
    mul_times = 0
    div_times = 0
    pow_times = 0
    sqr_times = 0
    sin_times = 0
    cos_times = 0
    log_times = 0
    for i in range(0, top5percent):
        list_tree = append_level(population[0][0].root, 0, None)
        str_tree = return_tree(list_tree)
        error_top5percent += get_error(population[i])
        add_times += str_tree.count("+")
        sub_times += str_tree.count("-")
        mul_times += str_tree.count("*")
        div_times += str_tree.count("/")
        pow_times += str_tree.count("p")
        sqr_times += str_tree.count("r")
        sin_times += str_tree.count("s")
        cos_times += str_tree.count("c")
        log_times += str_tree.count("l")

    error_top5percent = error_top5percent/top5percent
    add_times = add_times/top5percent
    sub_times = sub_times/top5percent
    mul_times = mul_times/top5percent
    div_times = div_times/top5percent
    pow_times = pow_times/top5percent
    sqr_times = sqr_times/top5percent
    sin_times = sin_times/top5percent
    cos_times = cos_times/top5percent
    log_times = log_times/top5percent

    for i in range(0, SIZE):
        error_total += get_error(population[i])
    error_total = error_total/SIZE

    list_tree = append_level(population[0][0].root, 0, None)
    str_tree_best = return_tree(list_tree)

    file = open('errors/error' + str(EXPERIMENT_NUMBER) + '.csv', 'a')
    writer = csv.writer(file)
    data = [error_best,error_top5percent,error_total,add_times,sub_times,mul_times,div_times,pow_times,sqr_times,sin_times,cos_times,log_times,str_tree_best]
    writer.writerow(data)
    file.close()






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




if __name__ == "__main__":
    EXPERIMENT_NUMBER = int(sys.argv[1])
    DEPTH = int(sys.argv[2])
    MUTATION_NUM = int(sys.argv[3])
    GENERATION_TYPE = sys.argv[4]
    SIZE = int(sys.argv[5])
    MUTATION_PROB = float(sys.argv[6])
    TOURNAMENT_PROB = float(sys.argv[7])
    ELITE = float(sys.argv[8])
    NUMBERS_RANGE = sys.argv[9]
    if NUMBERS_RANGE == "float":
        FLOAT_RANGE = True
    else:
        NUMBERS_RANGE = int(NUMBERS_RANGE)
        FLOAT_RANGE = False

    OPERATORS_LIST = list(sys.argv[10])

    operator_two = {}
    operator_one = {}
    all_operators = []
    all_elements = ["1", "2"]
    if "+" in OPERATORS_LIST:
        operator_two["+"] = addition
        all_operators.append("+")
        all_elements.append("+")

    if "-" in OPERATORS_LIST:
        operator_two["-"] = substraction
        all_operators.append("-")
        all_elements.append("-")

    if "*" in OPERATORS_LIST:
        operator_two["*"] = multiplication
        all_operators.append("*")
        all_elements.append("*")

    if "/" in OPERATORS_LIST:
        operator_two["/"] = division
        all_operators.append("/")
        all_elements.append("/")

    if "p" in OPERATORS_LIST:
        operator_two["p"] = addition
        all_operators.append("p")
        all_elements.append("p")

    if "r" in OPERATORS_LIST:
        operator_one["r"] = square_root
        all_operators.append("r")
        all_elements.append("r")

    if "s" in OPERATORS_LIST:
        operator_one["s"] = sine
        all_operators.append("s")
        all_elements.append("s")

    if "c" in OPERATORS_LIST:
        operator_one["c"] = cosine
        all_operators.append("c")
        all_elements.append("c")

    if "l" in OPERATORS_LIST:
        operator_one["l"] = logarithm
        all_operators.append("l")
        all_elements.append("l")

    save_data_experiment()
    population = generate_initial_population(SIZE, DEPTH, "full")

    new_ind = "/x?10?"
    new_root = Node(new_ind[0])
    new_tree = Tree(new_root, new_ind)
    replace_str(new_ind, [new_root], 0)
    #print(calculate_error(new_tree.root))

    j = 0
    incorrect = 0
    while j < len(population):
        #print(population[j].str)
        result = calculate_error(population[j].root)
        if result == "Not valid":
            population.remove(population[j])
            new_ind = generate_individual(DEPTH)
            new_root = Node(new_ind[0])
            new_tree = Tree(new_root, new_ind)
            # print("new ind")
            population.append(new_tree)
            read_str(new_ind, [new_root], 0)
            incorrect += 1
        else:
            population[j] = [population[j], result]
            j += 1
            #print(result)

    cycles = 1
    best_value = 99999999999
    while cycles <= 30:
        j = 0
        incorrect = 0
        population.sort(key=get_error)
        population = pairing(population)
        population = mutate(population)
        while j < len(population):
            # print(population[j].str)
            #print(j, population[j].str, population[j])
            result = calculate_error(population[j].root)
            if result == "Not valid":
                population.remove(population[j])
                new_ind = generate_individual(DEPTH)
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
        # print(population)
        new_ind = min(population, key=get_error)
        if new_ind[1] < best_value:
            best_value = new_ind[1]
        population.sort(key=get_error)


        cycles += 1
        save_data_cycles(population)
        print("Best value", new_ind[1], incorrect)

    save_data_experiment(best_value)
