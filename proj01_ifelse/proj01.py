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
name = raw_input("What's your name? ")
name = name[0:1].upper() + name[1:].lower()
grade = int(raw_input("What grade are you in? "))
years = 13 - grade
print name + ", you will graduate from high school in " + str(years) + " years."
print "End of Program 1."

current_month = 6
current_day = 12
name_2 = raw_input("What's your name? ")
name_2 = name_2[0:1].upper() + name_2[1:].lower()
birth_month = int(raw_input("Enter the number of your birth month. "))
birth_day = int(raw_input("What day of the month were you born? "))
if birth_month > current_month:
    months = int(birth_month - current_month)
    if birth_day > current_day:
        days = int(birth_day - current_day)
    print name_2 + ", your birthday is in " + str(months) + " months and " + str(days) + " days!"
if birth_month < current_month:
    months_2 = int(birth_month + current_month)
    if birth_day < current_day:
        days_2 = int(30 - (current_day - birth_day))
    print name + ", your birthday is in " + str(months_2) + " months and " + str(days_2) + " days!"
    print "End of Program 2."
    
age = int(raw_input("How old are you? "))
if age > 16:
    print "You can see R rated movies. Great."
elif age < 8:
    print "You should be allowed to see PG movies."
elif age < 14:
    print "You should be allowed to see PG-13 movies."



talk = 1
if talk == 1:
    name_3 = raw_input("Hi friend! What's your name? ")
    if len(name_3) > 10:
        print "That's a long name."
    print "My name's Macintosh."
    state = (raw_input("Where are you from? "))
    if state == "alabama" or state == "Alabama":
        print "Neat."
    elif state == "alaska" or state == "Alaska":
        print "The lights there are so beautiful! I've been a couple of times myself."
    elif state == "arizona" or state == "Arizona":
        print "Neat."
    elif state == "arkansas" or state == "Arkansas":
        print "Nice."
    elif state == "florida" or state == "Florida":
        print "the Sunshine State with the beautiful beaches and great seafood? I went there and I loved it!"
    elif state == "Texas" or state == "texas":
        print "That's where I'm from."
    elif state == "colorado" or state == "Colorado":
        ur = raw_input("Oh. No offense, but isn't that where the crackheads are? ")
        if ur == "yes" or ur == "Yes":
            print "Ha! Thought so."
        else:
            print "Oh."
    elif state == "california" or state == "California":
        city = raw_input("Where in California? ")
        if city == "Las Vegas" or city == "las vegas" or city == "Las vegas" or city == "las Vegas" or city == "Vegas":
            print "With the famed Vegas Strip, and the casinos and stuff? I've never been there myself."
    else:
        print "Nice."
    ui = raw_input("Do you want to play a game? ")
    if ui == "no" or ui == "No":
        raw_input("Why not? I haven't talked to anyone in a long time.")
        print "Oh. Ok. Bye I guess."
        talk = talk - 1
    if ui == "yes" or ui == "Yes":
        print "Yay! I'm good at most games as long as they're only virtual."
    ui2 = raw_input("Which game do you want to play? (1, 2, or 3.) ")
    if ui2 == "1":
        print "Great! Let's get started."
        ui_3 = raw_input("Game 1 is rock, paper, scissors. Do you still want to play? ")
        if ui_3 == "no" or ui_3 == "No":
            print "Oh. Ok. Bye I guess."
            talk = talk - 1
        if ui_3 == "yes" or ui_3 == "Yes":
