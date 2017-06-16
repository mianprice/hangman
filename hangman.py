#Import list of random words
import random

WORDS = open('./words.txt').read().splitlines()
SAFE_LETTERS = list("abcdefghijklmnopqrstuvwxyz")
GAME_COUNT = 0

#Setup Variables and Initial Values
def reset():
    global wrong,word,word_array,solution,solution_array,guesses,guessed_array,l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,e,ee
    ee = False
    e = ""
    wrong = 0
    word = random.choice(WORDS).lower()
    word_array = list(word)
    solution = ""
    solution_array = ["_"]*len(word)
    guesses = ""
    guessed_array = []
    l1 = "_"*11
    l2 = "| /      |"
    l3 = "|/       "
    l4 = "|       "
    l5 = "|       "
    l6 = "|"
    l7 = "|\\"
    l8 = "| \\"
    l9 =  "="*20
    l10 = "|"*20
    l11 = "="*20

#Function that draws gallows, current solution state, and current guesses state
def hangman():
    global solution,guesses
    solution,guesses,solution_print,guesses_print = [""]*4
    for i in range(20):
        print "\n"
    print l1
    print l2
    print l3
    print l4
    print l5
    print l6
    print l7
    print l8
    print l9
    print l10
    print l11
    print "\n"
    print "Here's what you have so far:\n"
    for x in range(len(solution_array)):
        solution += solution_array[x]
        solution_print += solution_array[x] + " "
    print solution_print + "\n"
    for x in range(len(guessed_array)):
        guesses += guessed_array[x]
        guesses_print += guessed_array[x] + " "
    print "Guesses: " + guesses_print
    print "\n"


#Guess handling function: RECURSIVE
def guess():
    global e,ee
    hangman()
    if solution == word:
        if wrong < 5:
            print "\nYou won with %d guesses left!" % (6-wrong)
        else:
            print "\nYou won with 1 guess left!"
    else:
        if ee == True:
            print e
        n = str(raw_input("Guess a letter: "))
        if len(n) < 1:
            ee = True
            e = "Please enter a letter. Try again."
            guess()
        elif len(n) > 1:
            ee = True
            e = "Please enter only one letter. Try again."
            guess()
        elif n in guessed_array:
            ee = True
            e = "You already guessed that. Try again."
            guess()
        elif n not in SAFE_LETTERS:
            ee = True
            e = "The character you entered wasn't a letter. Try again."
            guess()
        else:
            ee = False
            e = ""
            guessed_array.append(n)
            update(n)

#Update after receiving valid guess
def update(n):
    global wrong,word_array,solution_array
    if n in word_array:
        for x in range(word_array.count(n)):
            solution_array[word_array.index(n)] = n
            word_array[word_array.index(n)] = "_"
    else:
        wrong += 1
        update_hangman()

#Update gallows illustratrion after completed guess
def update_hangman():
    global l3,l4,l5
    if wrong == 1:
        l3 += "0"
    elif wrong == 2:
        l4 += "/"
    elif wrong == 3:
        l4 += "|"
    elif wrong == 4:
        l4 += "\\"
    elif wrong == 5:
        l5 += "/"
    elif wrong == 6:
        l5 += " \\"
        hangman()
        print "\nYou lost..."

#Game Loop
t = str(raw_input("Do you want to play hangman? (y/n) "))
while t == "y":
    reset()
    while wrong < 6:
        guess()
        if solution == word:
            break
    print "The word was: " + word
    t = str(raw_input("Do you want to play again? (y/n) "))
