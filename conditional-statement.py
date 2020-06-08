is_male = True
name = "Vinoth"
print("Hi ",name)
print(len(name)>0)
if not(is_male) and len(name)>0:
    if name.count("V"):
     print("Gender is Male")
elif name.count("V"):
    print("name start wiht V but not male")
else:
    print("Gender is female")

##Even or odd number
def even_number_check(num):
    if num==0:
        print("0 is eithher Even or Odd")
    elif num % 2 == 0 :
        print("Number is Even Number")

    else:
        print(str(num) + " number is Odd")
num = int(input("Enter the number to test: "))
even_number_check(num)
##Max of 3 numbers

def max_function(a,b,c):
    if a>b and a>c:
        print(str(a)+ " greater")
    elif b>a and b>c:
        print(str(b)+" is greater")
    else:
        print(str(c)+" greater")

max_function(256,250,78)
