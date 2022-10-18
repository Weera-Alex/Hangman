import random
print("""H A N G M A N""")
score = 0
lost = 0
while True:

    a = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if a == "exit":
        break
    elif a == "results":
        print(f"""You won: {score} times
You lost: {lost} times""")
    elif a == "play":
        code = "python", "java", "swift", "javascript"
        word = random.choice(code)
        counter = 0
        hint = ""
        for x in word:
            hint += "-"
        list2 = list(hint)
        string = hint
        already_guess = []
        while counter <= 7:

            all_indexes = []
            print()
            print(string)
            if "-" not in string:
                score += 1
                print(f"You guessed the word {string}!")
                print("You survived!")
                break
            guess = input(f"Input a letter: ")
            already_guess.append(guess)
            if len(guess) != 1:
                print("Please, input a single letter.")
            elif guess.isupper() or not guess.isalpha():
                print("Please, enter a lowercase letter from the English alphabet.")
            elif guess in string or already_guess.count(guess) >= 2:
                print("You've already guessed this letter.")
            elif guess in word:
                word = list(word)
                for i in range(0, len(word)):
                    if word[i] == guess:
                        all_indexes.append(i)
                for x in all_indexes:
                    list2[x] = guess
                string = "".join(list2)
                del all_indexes
            else:
                print("That letter doesn't appear in the word.")
                counter += 1
        if counter == 8:
            lost += 1
            print("You lost!")