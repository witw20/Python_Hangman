import random

print("H A N G M A N\n")

win = 0

lose = 0

while True:

    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    if menu.strip() == "exit":

        break

    elif menu.strip() == "results":

        print(f"You won: {win} times")

        print(f"You lost: {lose} times")

    elif menu.strip() == "play":

        print()

        word_list = ["python", "java", "swift", "javascript"]

        answer = random.choice(word_list)

        attempt = 8

        hint = list("-" * len(answer))

        guess_list = list()



        while attempt > 0 and "".join(hint) != answer:

            print("".join(hint))

            guess = input("Input a letter: ")



            if len(guess) != 1:

                print("Please, input a single letter.")

            elif not (guess.islower() and guess.isalpha()):

                print("Please, enter a lowercase letter from the English alphabet.")

            elif guess in guess_list or guess in hint:

                print("You've already guessed this letter.")

            elif guess not in answer:

                print("That letter doesn't appear in the word.")

                guess_list.append(guess)

                attempt -= 1

            else:

                for i in range(len(answer)):

                    if answer[i] == guess:

                        hint[i] = guess

            print()



        if "".join(hint) == answer:

            win += 1

            print(f"You guessed the word {answer}!\nYou survived!")

        else:

            lose += 1

            print("You lost!")

    else: continue

