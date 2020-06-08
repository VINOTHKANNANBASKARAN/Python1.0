from student import student

s1= student("Vinoth",26,"ECE",9.0)
s2= student("MSD",26,"ECE",6.8)
s3= student("Magesh",26,"ECE",3)
s4= student("OOSI",26,"ECE",7.0)
s1.student_category()
s1.student_info()

#s5=student("Vinoth",26,"ECE",9.0)
s5=s1
if s1 == s5:
    print("same students")
else:
    print("differnt Students")

del s5;
s1.student_info()
s5.student_info()
