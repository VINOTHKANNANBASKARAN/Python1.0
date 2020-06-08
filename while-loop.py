#Use while loop to print table of the number inputed by the user

num = float(input('Enter the number for which the table is required'))
i=0
num = int(round(num))
while i<10:

    i += 1
    if i==5:
        continue
        print('continue statement hit')
    print(str(num)+" x "+ str(i) +" = "+str(num*i))


##Guess the password

secretKey = "vinoth"
password=""
limit = 3
try_count=0
status_message="You WIN !!"
while password!=secretKey:
    if (try_count==3):
        status_message = ("You Loose")
        break;
    password = input("Enter the Password")
    try_count += 1;


print(status_message)
