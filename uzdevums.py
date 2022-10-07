
import json

file = open('students.json', 'r')
data = json.load(file)
file.close()

print(data)
for student in data['Students']:
        print(f"{student['FirstName']} {student['LastName']} {student['Age']}")