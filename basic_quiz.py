# defining a class
class Question:
    def __init__(self, prompt, answer):
        self.prompt=prompt
        self.answer=answer
# questions array
question_prompts = [
    "What colors are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colors are Bannanas?\n(a)Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colors are straberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

#question prompt array
questions=[
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2],"b")
]


# function definition
def run_test(questions):
    score = 0
    for question in questions:
        answer= input(question.prompt)
        if answer== question.answer:
            score +=1
    print("You got "+str(score)+'/'+ str(len(questions))+ "Correct")


# function call
run_test(questions)
