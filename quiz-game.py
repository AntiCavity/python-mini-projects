print("Welcome to my history quiz!")

playing = input("Would you like to take this quiz(Y/N)? ")

if playing.lower() != "y":
    quit()


correct = 0
answer1 = input("What year was America Discovered? ")

if answer1 == "1492":
    print("Correct!")    
    correct = correct + 1
else:
    print("Incorrect!")

answer2 = input("Who was the creator of the Carolingian Empire? ")

if answer2.lower() == "charlemagne":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect!")

answer3 = input("Who won the Battle of Hastings in 1066? ")

if answer3.lower() == "william the conqueror":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect!")

answer4 = input("What year did the Ottomans conquer Constantinople? ")

if answer4 == "1453":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect!")

answer5 = input("Who had the biggest empire in history? ")

if answer5.lower() == "the mongols":
    print("Correct!")
    correct = correct + 1
else:
    print("Incorrect!")

print("You got " + str(correct) + " questions correct!")