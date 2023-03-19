import random

from student import Student

# Student List
students = [
    Student("Light", 4),
    Student("Andre", 4),
    Student("Haru", 4),
    Student("Xander", 4)
]

# Shuffle the list of students
random.shuffle(students)

# Sort the list of students
students.sort(key=lambda student: student.getName())
for student in students:
  print(student)


