a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in a:
    print(i)

for i in range(5):
    print(i)
for i in range(len(a)):
    print(a[i])

for letter in "VinothKannan":
    print(letter)

# Print 5 tables

for i in range(1, 10):
    print(str(5) + " x " + str(i) + " = " + str(5 * i))

##Find out active and inactive users
week_dictionary = {
    "day": [
        {
            "user": "Monday",
            "isActive": True,
            "message": "Beautiful Monday"
        },
        {
            "user": "Tuesday",
            "isActive": False,
            "message": "Learning Tuesday"
        },
        {
            "user": "Wednesday",
            "isActive": True,
            "message": "Studious Wednesday"
        },
        {
            "user": "Thursday",
            "isActive": False,
            "message": "Tiresome Thursday"
        },
        {
            "user": "friday",
            "isActive": True,
            "message": "Futuristic Friday"
        },
        {
            "user": "saturday",
            "isActive": True,
            "message": "soothing saturday"
        }
    ]

}


for  day in week_dictionary.copy().items():
    for i in day:
        print(i)

    break;