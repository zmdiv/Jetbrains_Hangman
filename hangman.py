import random


def start_play():
    print("H A N G M A N")
    to_start = input('Type "play" to play the game, "exit" to quit: ')
    return to_start


def play():
    word_list = ['python', 'java', 'kotlin', 'javascript']
    choice = random.choice(word_list)
    basket = set(choice)
    counter = 8
    exposed = ''.join(("-" * len(choice)))
    called_letters = []
    while counter > 0:
        inp_index = 0
        print("")
        print(exposed)
        inp = input('Input a letter: ')

        if len(str(inp)) == 1 and inp != ' ':
            if inp.isalpha() and inp.islower():
                if inp not in choice and inp not in called_letters:
                    print("That letter doesn't appear in the word")
                    counter -= 1

                if inp in basket:
                    for idx, value in enumerate(choice):
                        if value == inp:
                            exposed = exposed[:idx] + inp + exposed[idx + 1:]

                if inp in called_letters:
                    print("You've already guessed this letter")

                called_letters.append(inp)

                if counter == 0:
                    print("You lost!")
                    break

                if exposed == choice:
                    print("")
                    print(choice)
                    print("You guessed the word!")
                    print("You survived!")
                    break
            else:
                print('Please enter a lowercase English letter')
        else:
            print('You should input a single letter')


if start_play() == 'play':
    play()
elif start_play() == 'quit':
    pass
