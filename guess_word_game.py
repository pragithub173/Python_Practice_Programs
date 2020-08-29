secret_word= "bangalore"
user_input=""
user_count=0
user_limit=3
out_of_guess= False

while user_input!= secret_word and not out_of_guess:
    if user_count<user_limit:
            user_count=user_count +1
            user_input = input("Enter the word: ")
    else :
        out_of_guess=True

if out_of_guess:
        print("Limit exceeded. You looses")
else:
    print("You win")