# Imported modules
import random

#Variables
name = input("What is your name?")
question = input("What is your question?")
answer = ("")

# Statment
print(name + " asks: " + question + "?")

# Options for the Magic 8 Ball game
answer1 = "Yes - definitely"
answer2 = "It is decidedly so"
answer3 = "Without a doubt"
answer4 = "Reply hazy, try again"
answer5 = "Ask again later"
answer6 = "Better not tell you now"
answer7 = "My sources say no"
answer8 = "Outlook not so good"
answer9 = "Very doubtful"

# Generator to get a random answer
randnumber = random.randint(1, 9)
match randnumber:
    case 1:
        print(answer1)
    case 2:
        print(answer2)
    case 3:
        print(answer3)
    case 4:
        print(answer4)
    case 5:
        print(answer5)
    case 6:
        print(answer6)
    case 7:
        print(answer7)
    case 8:
        print(answer8)      
    case 9:
        print(answer9)     