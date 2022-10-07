
file = open("names.txt", "w")
for i in range(100):
    file.write(f'\nName{i} Surname{i}')

file.close()