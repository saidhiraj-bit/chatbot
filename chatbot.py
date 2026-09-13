while True:
    user=input("You : ")
    user=user.lower().strip()
    if user=="hello":
        print("Bot : Hiii! There")
    elif user=="how are you":
        print("Bot : I am doing great!")
    elif user=="what is your name?":
        print("Bot : I am chatBOT")
    elif user=="thank you":
        print("Bot : You are welcome!")
    elif user=="who made you":
        print("I am Human Made")
    elif user=="you were developed in which language":
        print("Bot : Python")
    elif user=="what is favourite colour":
        print("Bot : Red")
    elif user=="exit":
        print("Bye! Have a nice day")
        break
    else:
        print("Bot : i Don't understand it")
    
