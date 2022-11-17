import csv
import random
list_values = []

def calculate_value(value):
    return value/(2*(value-3)+9)

for i in range (100):
    number = random.random()*random.randint(0, 100000)
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
writer.writerow(["/x+*92-x3"])
for i in results:
    data = []
    data.append(i[0])
    data.append(i[1])
    writer.writerow(data)
file.close()


