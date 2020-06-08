from Question import Question

question_prompts = ["\nwhat color is the sky?\na)blue\nb)orange\nc)Yellow",
"\nwhat color is the sea?\na)blue\nb)orange\nc)Yellow",
"\nwhat color is the tree?\na)blue\nb)green\nc)Yellow",
                    ]

questions = [
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"a"),
    Question(question_prompts[2],"b")
]

def run_test():
    score = 0;
    for question in questions:
        answer = input(question.question);
        if answer == question.answer:
            score += 1 ;
    print("Your Score is "+ str(score) +" on "+str(len(questions)))

run_test();