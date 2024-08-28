# GPA Rank
# by J. Warneke, 8/27/2024
# Input student name and GPA to determine whether they meet the requirements for the honor roll (3.25+) or deans list (3.5+).

# Setup initial values
l_name = ""
f_name = ""
GPA = 0.0
rank = "None"

while True:
    # Accept input
    l_name = input("Enter the student's last name, or enter 'ZZZ' to quit:")

    if l_name == "ZZZ":
        break

    f_name = input("Enter the student's first name:")
    GPA = float(input("Enter the student's GPA, in the format '4.00':"))

    # Check GPA against requirements to determine rank
    if GPA >= 3.5:
        rank = "Dean's List"
    elif GPA >= 3.25:
        rank = "Honor Roll"
    else:
        rank = "None"

    if not rank == "None":
        print("Congratulations! %s achieved %s!" % (f_name,rank))
    else:
        print("%s's GPA does not qualify for honor roll or dean's list." % f_name)

print("Quitting the program...")