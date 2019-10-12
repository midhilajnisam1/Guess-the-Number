guess_number = 7
chances = 1 #set the chances to 1 which will incriment upto 5 according to the false guesses
print("Welcome to the Guess the Number Game!")
print("You have 5 chances to guess the number!")
print("HINT: It is a number b/w 1-10 ")
while(chances <= 5):
    #takes the guess number from user
    user_input = int(input("Enter your guess:\n"))
    if user_input > guess_number:
        print("Your entered number is greater than guess number")

    elif user_input < guess_number:
        print("Your entered number is lesser than the guess number")

    elif user_input == guess_number:
        print("Congrats! You have entererd the correct number")
        print("You have taken",chances-1,"chances to win")
        break

    print("NOTE:",5 - chances, "no: of guesses left")
    chances = chances + 1

    if chances > 5:
        print("Your chances are over So Game Over")


        






