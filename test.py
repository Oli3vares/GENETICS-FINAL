import csv
import random
list_values = []

def calculate_value(value):

    return (7+2*value)/(3-(6*value+4*(5/value)))

for i in range (100):
    number = random.random()*random.randint(-50000, 100000)
    if number != 3:
        list_values.append(number)

print(list_values)
results = []
for i in list_values:
    result = calculate_value(i)
    results.append([i, result])
print(results)
file = open('function4.csv', 'a')
writer = csv.writer(file)
data = ["X_VALUE", "Y_VALUE"]
writer.writerow(data)
writer.writerow(["/+-7*3+2x**6x4/5x"])
for i in results:
    data = []
    data.append(i[0])
    data.append(i[1])
    writer.writerow(data)

print(list_values)
file.close()


