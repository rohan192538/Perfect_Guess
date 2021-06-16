import random
randomNumber= random.randint(1,100)
print(randomNumber)
userGuess= None
guesses=0
while (userGuess!=randomNumber):
    userGuess = int(input("Enter your Guess: "))
    guesses +=1
    if (userGuess==randomNumber):
        print("Your guessed is right !")
    else:
        if(userGuess>randomNumber):
            print("Your guessed is wrong! , please enter lower number")
        else:
            print("Your guessed is wrong ! , please enter higher number")
    
print(f"You guessed the number in {guesses} guess")    
