word = 'laptop'
attempts = len('hangman')
counter = 0
while counter <=attempts:
    hint = 'A portable computer'
    guess = input("Enter your guess. Type 'hint' if you want hint: ")
    if guess == 'hint':
        print(hint)
    else:
        if guess == word:
            print("You got the word correct!")
            break
        else:
            print(f"You got the word wrong. Attempt: {'hangman'[counter]}")
            counter+=1