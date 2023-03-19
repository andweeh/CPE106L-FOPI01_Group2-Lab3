import random

from student import Student
# Student List
students = [
    Student("Light", 4),
    Student("Andre", 3),
    Student("Haru", 3),
    Student("Xander", 7)
]

# Shuffle the list of students
random.shuffle(students)

# Sort Method in ascending order
#<-- after shuffle list method
students.sort(key=lambda student: student.getName())
for student in students:
  print(student)

# Sort Method in descending order
#<-- after shuffle list method
# students.sort(reverse=True)
# for student in students:
#   print(student)
