import csv
import random
import math
list_values = []

def calculate_value(value):

    calculation = (7+2*value)/(3+(6*value+4*(5/value)))
    print(calculation)
    return math.sqrt(calculation)

for i in range (100):
    number = random.random()*random.randint(0, 5000)
    if number != 3:
        list_values.append(number)

print(list_values)
results = []
for i in list_values:
    result = calculate_value(i)
    results.append([i, result])
print(results)
file = open('function1.csv', 'a')
writer = csv.writer(file)
data = ["X_VALUE", "Y_VALUE"]
writer.writerow(data)
writer.writerow(["s/++7*3+2x**6x4/5x"])
for i in results:
    data = []
    data.append(i[0])
    data.append(i[1])
    writer.writerow(data)

print(list_values)
file.close()


