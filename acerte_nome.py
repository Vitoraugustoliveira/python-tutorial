""" Read name from keyboard input and verify if name is corrected"""

def validator(message, name):
    second_time = False
    while True:
        message2 = message + "\n" if not second_time else message+" again\n"
        name_input = input(message2)
        if name_input == name:
            break
        second_time = True
    return name_input

NAME = "Jhon"
"""SECOND_TIME = False
while True:
    message = "Enter with your name\n" if not SECOND_TIME else "Enter with your name again\n"
    name_input = input(message)
    if name_input == NAME:
        break
    SECOND_TIME = True
 """

name_input = validator("Enter with your name", NAME)
print(name_input)

COUNTRY = "USA"
""" SECOND_TIME = False
while True:
    message = "Enter with your country name\n" if not SECOND_TIME else "Enter with your country name again\n"
    name_input = input(message)
    if name_input == COUNTRY:
        break
    SECOND_TIME = True """

name_input = validator("Enter with your country name", COUNTRY)


print(name_input)