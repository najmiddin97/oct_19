import csv

with open('data.csv', newline='') as csvfile:
    file_data = csv.reader(csvfile)
    data = []
    for row in file_data:
        data.append(row)

print(data)
for row in data:
    name, last_name, city = row
    print(f'Familya: {last_name}, ism: {name}, shaxar: {city}')
