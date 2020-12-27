import random
class Student():

    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

student1 = Student("Miray","Topal")
list1 = [student1.name, student1.surname]

i=0
while(i<3):
    name1 = input("Enter your name:")
    surname1 = input("Enter your surname:")
    list2 = [name1, surname1]
    if list1 == list2:
        print("Welcome", name1, surname1)
        break
    else:
        i += 1
    print("Try again later...")

lesson=int(input("Choose at least 3 lessons:"))
if(5>=lesson>=3):
    print("You choosed",lesson,"lesson")
else:
    print("You failed in class")

courseList=("pyt","c","c++","matlab","java")
course1=[]
i=0
while(i<lesson):
    randomcourse=random.randrange(0,lesson)
    randomcourse1=courseList[randomcourse]
    course1.append(randomcourse1)
    i+=1
print(course1)

exam=input("Choose an exam:")
x=0
while(x<len(course1)):
    if(exam == course1[x]):
        print("You choosed",course1[x],"exam")
        break
    else:
        print ("You did't take the lesson")
    x+=1

    def resultCalculate(self):
        result=random.randint(0,100)
        print(result)
        if 80 <= result:
            print("AA")
        elif 70 <= result < 90:
            print("BB")
        elif 50 <= result < 70:
            print("CC")
        elif 30 <= result < 50:
            print("DD")
        else:
            print("FF")

student=Student()
student.resultCalculate()

