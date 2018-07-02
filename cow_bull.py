# Create a program that will play the 'cows and bulls' game with the user. The game works
# like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every
# digit that the user guessed correctly in the correct place, they have a 'cow'. For
# every digit the user guessed correctly in the wrong place is a 'bull.' Every time the
# user makes a guess, tell them how many 'cows' and 'bulls' they have. Once the user
# guesses the correct number, the game is over. Keep track of the number of guesses the
# user makes throughout the game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like
# this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull

# Until the user guesses the number.


import random
numb = str(random.randint(1000,9999)) #random 4 digit number
print numb
cows = 0
bulls = 0
gus = 0

print "Welcome to Cows and Bulls!"
print "I will generate a random 4-digit number. For every correct number in the right place, you get a cow. For every correct number in the wrong place, you get a bull."

cobu = 5

while cobu == 5:
    cows = 0
    bulls = 0
    uni = (raw_input("Enter a 4-digit number."))
    for numby in range(0, 4):
        if uni == numb:
            cows = cows + 1
            uni = "&"
            numb = "*"
    for um in uni:
        con = 0
        for bum in numb:
            bulls = bulls + 1
            numb = "*"
            break

        con = con + 1
    gus = gus + 1
    print "You have " + str(cows) + " cows and " + str(bulls) + " bulls."
    if cows == 4:
        cobu = cobu - 3
        print "You won! Congratulations!"
        print "You used " + str(gus) + " guesses."
    else:
        print "Try again!"