import random

from student import Student

student1 = Student("Marky", 4)
student2 = Student("Dee Dee",4)
for i in range(1,4):
     student1.setScore(i,random.randint(60,100))
     student2.setScore(i,random.randint(60,100))
student1HighScore = student1.getHighScore()
student2HighScore = student2.getHighScore()
print( student1.name+": "+str(student1HighScore) +"\n",student2.name+": "+str(student2HighScore))
Student.isEqual(student1HighScore,student2HighScore)
Student.isLessThan(student1HighScore,student2HighScore)
Student.greaterOrEqual(student1HighScore,student2HighScore)
