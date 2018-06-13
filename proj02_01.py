# Name:
# Date:

# proj02: sum

# Write a program that prompts the user to enter numbers, one per line,
# ending with a line containing 0, and keep a running sum of the numbers.
# Only print out the sum after all the numbers are entered
# (at least in your final version). Each time you read in a number,
# you can immediately use it for your sum,
# and then be done with the number just entered.

#Example:
# Enter a number to sum, or 0 to indicate you are finished: 4
# Enter a number to sum, or 0 to indicate you are finished: 5
# Enter a number to sum, or 0 to indicate you are finished: 2
# Enter a number to sum, or 0 to indicate you are finished: 10
# Enter a number to sum, or 0 to indicate you are finished: 0
#The sum of your numbers is: 21
sum = 0
loop = 1
while loop != 0:
    num = int(raw_input("Enter a number to add, or enter 0 to finish. "))
    sum = num + sum
    if num == 0:
        loop = loop - 1
        print "The sum of the numbers is " + str(sum) +  " ."

print " "
game = 2
print "Rock, Paper, Scissors"
loop = 0
while game == 2:
    u_1 = raw_input("Player 1, enter either rock, paper, or scissors.")
    u_2 = raw_input("Player 2, enter either rock, paper, or scissors.")
    if u_1 == "rock" or u_1 == "Rock":
        if u_2 == "paper" or u_2 == "Paper":
            print "Player 2 wins!"
    elif u_1 == "Rock" or u_1 == "rock":
        if u_2 == "scissors" or u_2 == "Scissors":
            print "Player 1 wins!"
    elif u_1 == "rock" or u_1 == "Rock":
        if u_2 == "Rock" or u_2 == "rock":
            print "Tie!"
    elif u_1 == "paper" or u_1 == "Paper":
        if u_2 == "rock" or u_2 == "Rock":
            print "Player 1 wins!"
    elif u_1 == "paper" or u_1 == "Paper":
        if u_2 == "paper" or u_2 == "Paper":
            print "Tie!"
    elif u_1 == "paper" or u_1 == "Paper":
        if u_2 == "scissors" or u_2 == "Scissors":
            print "Player 2 wins!"
    elif u_1 == "scissors" or u_1 == "Scissors":
        if u_2 == "rock" or u_2 == "Rock":
            print "Player 2 wins!"
    elif u_1 == "scissors" or u_1 == "Scissors":
        if u_2 == "paper" or u_2 == "Paper":
            print "Player 1 wins!"
    elif u_1 == "scissors" or u_1 == "Scissors":
        if u_2 == "scissors" or u_2 == "Scissors":
            print "Tie!"
    redo = raw_input("Would you like to play again?")
    if redo == "yes" or redo == "Yes":
        game = 2
    else:
        game = game - 1