class student:

    def __init__(self,name,age,course,gpa):
        self.name = name;
        self.age=age;
        self.course=course
        self.gpa=gpa

    def student_info(self):
        print("Hi, I am "+self.name+" and i am enrolled in "+self.course)

    def student_category(self):
        gpa = self.gpa
        if gpa>8.5:
            print('ExtraOrdinary Student')
        elif gpa>6 and gpa<8.5:
            print("Student with Distinction")
        elif gpa>5 and gpa<6:
            print("Average Student")
        else:
            print('Flopper')
