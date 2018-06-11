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
    if birth_day > current_day:
        days = int(birth_day - current_day)
    print name_2 + ", your birthday is in " + str(months) + " months and " + str(days) + " days!"
if birth_month < current_month:
    months_2 = int(birth_month + current_month)
    if birth_day < current_day:
        days_2 = int(30 - (current_day - birth_day))
    print name + ", your birthday is in " + str(months_2) + " months and " + str(days_2) + " days!"
