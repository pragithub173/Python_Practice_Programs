def translator(phrase):
    word=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            # this will covert the letter to lower case and check
            if letter.isupper() :
             word=word+"G"
            else :
             word = word + "g"
        else:
            word=word +letter
    return word

phrase = input("Enter a phrase: ")

print(translator(phrase))