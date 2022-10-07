import json

file = open('students.json', 'r')
data = json.load(file)
file.close()

print(data)
for student in data['Students']:
        print(f"{student['FirstName']} {student['LastName']} {student['Age']}")



total_age = 0
count = 0
for student in data['Students']:
    total_age += int(student['Age'])
    count += 1

print('===================================')
print(f'Average age is {total_age / count}')



ages = []
for student in data['Students']:
    ages.append(int(student['Age']))

print(sum(ages) / len(ages))