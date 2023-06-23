print("""you enter a dark room with teo doors.
Do you go through door 1 or door 2 or door 3?""")

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cake")
    print("what do you do?")
    print("1 - take the cake")
    print("2- scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. good job")
    elif bear == "2":
        print("THe bear eats your legs off. good job")
    else:
        print(f"well, doing {bear} is probably better")
        print("bear runs away")

elif door == "2":
    print("you stare into the endless abyss at cthulhu's retina")
    print("1- blueberries")
    print("2- yellow jacket clothespin")
    print("3- understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by the mind of a jedi")
        print("good job")
    else:
        print("the insanity rots your eyes into a pool of muck")
        print("Good Job")

elif door == "3":
    print("You find your self in another room with lots bees.")
    print("1- make friend swith the bees and take over")
    print("2 - run and hide")
    print("3= touch yourself")

    bees = input("> ")

    if bees == "1":
        print(" welldone you befirended the bees and now you are their master")
    elif bees == "2":
        print("Twat")
    else:
        print("you dutty bugger")
        
else:
    print("you stumble around and fall on a knife and die....good job")