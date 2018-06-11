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

current_month = 6
current_day = 11
name_2 = raw_input("What's your name? ")
birth_month = int(raw_input("Enter the number of your birth month. "))
birth_day = int(raw_input("What day of the month were you born? "))
if birth_month > current_month:
    months = int(birth_month - current_month)
    print "Your birthday is in " + str(months) + "and " + str(days) "!"
if birth_day > current_day:
    days = int(birth_day - current_day)


if birth_month < current_month:
    print str(birth_month + current_month)