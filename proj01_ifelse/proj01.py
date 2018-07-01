# Name:
# Date:

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.


# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday


# If you complete extensions, describe your extensions here!

#name = raw_input("What's your name? ")
#name = name[0:1].upper() + name[1:].lower()
#grade = int(raw_input("What grade are you in? "))
#years = 13 - grade
#print name + ", you will graduate from high school in " + str(years) + " years."
#print "End of Program 1."

#current_month = 6
#current_day = 12
#name_2 = raw_input("What's your name? ")
#name_2 = name_2[0:1].upper() + name_2[1:].lower()
#birth_month = int(raw_input("Enter the number of your birth month. "))
#birth_day = int(raw_input("What day of the month were you born? "))
#if birth_month > current_month:
    #months = int(birth_month - current_month)
    #if birth_day > current_day:
        #days = int(birth_day - current_day)
    #print name_2 + ", your birthday is in " + str(months) + " months and " + str(days) + " days!"
#if birth_month < current_month:
    #months_2 = int(birth_month + current_month)
    #if birth_day < current_day:
        #days_2 = int(30 - (current_day - birth_day))
    #print name + ", your birthday is in " + str(months_2) + " months and " + str(days_2) + " days!"
    #print "End of Program 2."

    #age = int(raw_input("How old are you? "))
    #if age > 16:
        #print "You can see R rated movies. Great."
    #elif age < 8:
        #print "You should be allowed to see PG movies."
    #elif age < 14:
        #print "You should be allowed to see PG-13 movies."

import time
import random
smalley = 18
liek = 7
talk = 1
while talk == 1:
    name_3 = raw_input("Hi! What's your name? ")
    name_3 = name_3[0:1].upper() + name_3[1:].lower()
    if len(name_3) > 10 and len(name_3) < 50:
        time.sleep(1.2)
        print "That's a long name."
        time.sleep(1.4)
    elif len(name_3) > 50:
        time.sleep(2.5)
        print "I don't think that's even a name."
        time.sleep(1.8)
    print "My name's Macintosh."
    time.sleep(1)
    state = (raw_input("What state are you from? "))
    time.sleep(0.45)
    if state == "alabama" or state == "Alabama":
        time.sleep(0.45)
        print "Neat."
    elif state == "alaska" or state == "Alaska":
        time.sleep(0.45)
        print "The lights there are so beautiful! I've been a couple of times myself."
        time.sleep(0.5)
    elif state == "arizona" or state == "Arizona":
        time.sleep(0.45)
        print "Neat."
        time.sleep(0.5)
    elif state == "arkansas" or state == "Arkansas":
        time.sleep(0.45)
        print "Nice."
        time.sleep(0.5)
    elif state == "florida" or state == "Florida":
        time.sleep(0.45)
        print "The Sunshine State with the beautiful beaches and great seafood? I went there and I loved it!"
        time.sleep(0.5)
    elif state == "Texas" or state == "texas":
        time.sleep(0.45)
        print "That's where I'm from."
        time.sleep(0.5)
    elif state == "colorado" or state == "Colorado":
        time.sleep(0.8)
        ur = raw_input("Oh. No offense, but isn't that where the crackheads are? ")
        if ur == "yes" or ur == "Yes":
            time.sleep(0.38)
            print "Ha! Thought so."
            time.sleep(0.5)
        else:
            time.sleep(1)
            print "Oh."
            time.sleep(0.6)
    elif state == "california" or state == "California":
        time.sleep(0.45)
        city = raw_input("Where in California? ")
        if city == "Las Vegas" or city == "las vegas" or city == "Vegas":
            time.sleep(0.4)
            print "With the famed Vegas Strip, and the casinos and stuff? I've never been there myself."
            time.sleep(0.5)
    else:
        time.sleep(0.45)
        print "Nice."
        time.sleep(0.45)
    while liek == 7:
        ui = raw_input("Do you want to play a game? ")
        if ui == "no" or ui == "No":
            raw_input("Why not? I haven't talked to anyone in a long time.")
            print "Oh. Ok. Bye I guess."
            talk = talk - 1
        if ui == "yes" or ui == "Yes":
            time.sleep(0.2)
            print "Yay! I'm good at most games as long as they're only virtual."
        ui2 = int(raw_input("Which game do you want to play? (1, 2, or 3.) "))
        if ui2 == 1:
            time.sleep(0.45)
            print "Great! Let's get started."
            ui_3 = raw_input("Game 1 is rock, paper, scissors. Do you still want to play? ")
            if ui_3 == "no" or ui_3 == "No":
                time.sleep(1)
                print "Oh. Ok."
            else:
                time.sleep(0.45)
                print "Great!"
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
                        liek = liek + 1
        if ui2 == 2:
            print "Great! Let's get started."
            ui_4 = raw_input("Game 2 is Guess my number. Do you still want to play?")
            if ui_4 == "no" or ui_4 == "No":
                print "Oh."
            else:
                print "Great! Let's begin."
                game = 1
                counter = 0
                num = int(random.randint(1, 9))
                while game == 1 and counter < 10:
                    ug = int(raw_input("Enter a number, or type 0 to end. "))
                    counter = counter + 1
                    if ug == 0:
                        game = game - 1
                    elif ug > num:
                        print "You guessed too high!"
                    elif ug < num:
                        print "You guessed too low!"
                    elif ug == num:
                        ui = raw_input(("Great, you won in ") + str(counter) + (" guess(es)! Do you want to play again? "))
                        if ui == "No" or ui == "no":
                            print "Oh. Okay then."
                            game = game - 1
                            liek = liek + 1
                        else:
                            game = 1
                            num = int(random.randint(1, 9))
                            counter = 0
                    else:
                        counter = counter + 0
                        print "A number, not a word or letters."
        if ui2 == 3:
            while smalley == 18:
                print "This game is called I Will Predict Your Birthday. I'm really good at it. Let's begin."
                bmon = int(raw_input("Tell me the number of your birth month."))
                bmon2 = int(bmon + 18)
                time.sleep(1.1)
                print "Add 18 to that. This gives you " + str(bmon2) + "."
                bmon3 = int(bmon2 * 25)
                time.sleep(1.1)
                print "Multiply that by 25. Now you have " + str(bmon3) + "."
                bmon4 = int(bmon3 - 333)
                time.sleep(1.1)
                print "Subtract 333 from that. That leaves you with " + str(bmon4) + "."
                bmon5 = int(bmon4 * 8)
                time.sleep(1.1)
                print "Multiply the number by 8. Now, it's " + str(bmon5) + "."
                bmon6 = int(bmon5 - 554)
                time.sleep(1.1)
                print "Subtract 554 from that. You're left with " + str(bmon6) + "."
                bmon7 = int(bmon6 / 2)
                time.sleep(1.1)
                print "Divide " + str(bmon6) + " by 2. Now you have " + str(bmon7) + "."
                time.sleep(1.1)
                bdate = int(raw_input("Tell me what day of the month you were born."))
                bdamon = int(bmon7 + bdate)
                time.sleep(1)
                print "Add your day of birth to " + str(bmon7) + ". You now have " + str(bdamon) + "."
                bdamon2 = int(bdamon * 5)
                time.sleep(1)
                print "Multiply " + str(bdamon) + " by 5. You have " + str(bdamon2) + "."
                bdamon3 = int(bdamon2 + 692)
                time.sleep(1)
                print "Subtract 692 and you're left with " + str(bdamon3) + "."
                bdamon4 = int(bdamon3 * 20)
                time.sleep(1)
                print "Now multiply " + str(bdamon3) + " by 20 and you get " + str(bdamon4) + "."
                time.sleep(1)
                l2d = int(raw_input("Give me the last two numbers of your birth year."))
                bdale = int(bdamon4 + l2d)
                time.sleep(1)
                print "Then add " + str(l2d) + " to " + str(bdamon4) + " and you get " + str(bdale) + "."
                bdale_ultimate = int(bdale - 32940)
                time.sleep(1)
                print "And finally, subtract 32,940 from " + str(bdale) + " to get " + str(bdale_ultimate) + "."
                time.sleep(1)
                if l2d < 10:
                    print "Your birthdate is " + str(bmon) + "/" + str(bdate) + "/0" + str(l2d) + "."
                else:
                    print "Your birthdate is " + str(bmon) + "/" + str(bdate) + "/" + str(l2d) + "."
                play = raw_input("Do you want to play again?")
                if play == "no" or play == "No":
                    smalley = smalley + 1
                else:
                    smalley = 18
        if ui2 != 1 or ui2 != 2 or ui2 != 3:
            print "That's not an option. Let's go with game 3."