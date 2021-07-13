from hangman_pics import hangman
import random

def guess_word():
    word = random.choice(words)
    print("Guess the fruit")
    return word

def is_present(letter):
    if letter.lower() in word.lower():
        return letter.lower()
    else:
        return False

def fill_blank(letter):
    global display_dash,word
    display_dash = list(display_dash)
    for i,l in enumerate(word):
        if letter == l:
            display_dash[i]=letter
    print("".join(display_dash))

def make_hangman():
    global chances
    chances += 1 
    print(hangman[chances])

def check_letter(user_choice): # when user enters single letter
    letter = is_present(user_choice)
    if letter:
        fill_blank(letter)
    else:
        make_hangman()

def check_word(user_choice): # when user enters full word
    if user_choice.lower() == word.lower():
        return True
    else:
        return False


#initial setup
chances = 0
is_win = False
words = ['apple', 'orange','kiwi','watermelon','banana','strawberry','plum']
word = guess_word()
display_dash = ('-'*len(word))
print(display_dash)
print(hangman[0])


#main loop

while chances <= 5 and not is_win:
    user_choice = input()
    if len(user_choice)==1:
        check_letter(user_choice)
    else:
        is_win = check_word(user_choice)
        break

    if '-' not in display_dash:
        is_win = True    


if is_win:
    print("Win")
else:
    print("Lost")