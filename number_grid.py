number_grid =[
    [1,2,3,4],
    [5,6,7,8,9,10],
    [0]
]

for row in number_grid:
    for item in row:
        print(item)

'''
multi line comment
'''
##Remove vowel in the givenn phrase

phrase = input("Enter the phrase:")
translator =""
for letter in phrase:
    if letter in "AEIOUaeiou":
        translator = translator+'v'
    else:
        translator = translator+letter

print(translator)