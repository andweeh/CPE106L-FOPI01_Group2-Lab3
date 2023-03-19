import random

class Student(object):
   

    def __init__(self, name, number):
     
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    #Make a method that compares two objects
    @classmethod
    def isEqual(cls,score1,score2):
        if score1 == score2:
            print("The scores are for both students are equal")
        else:
            print("The scores are not equal")
    @classmethod
    def isLessThan(cls,score1,score2):
        if score1 < score2:
            print(str(score1) + " is less than " + str(score2))
        else:
            print(str(score1) + " is not less than " + str(score2))
    @classmethod
    def greaterOrEqual(cls,score1,score2):
        if score1 >= score2:
            print(str(score1) + " is greater than or equal than " + str(score2))
        else:
            print(str(score1) + " is not greater " + str(score2))

    def getName(self):
  
        return self.name
  
    def setScore(self, i, score):
       
        self.scores[i - 1] = score

    def getScore(self, i):
      
        return self.scores[i - 1]
   
    def getAverage(self):

        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
       
        return max(self.scores)
 
    def __str__(self):
      
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

def main():
    
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


if __name__ == "__main__":
    main()