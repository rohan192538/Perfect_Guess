# Perfect_Guess
perfect guess is a type of game where user have to guess the number if he guesses the correct number then display "You guessed it right!" and if he guess the wrong number and smaller than the correct number then display "You guessed it wrong! please enter the larger number" and if he guess the wrong number and larger than the correct number then display "You guessed it wrong! please enter smaller number" this project is made using python.
with high score text file we can now update the high score of users with using the given below code.
with open("highscore.txt", "r") as f:
    highscore= int(f.read())  
if (guesses<highscore):
    print("Congrates! You have just broken the highscore")
    with open("highscore.txt", "w") as f :
        f.write(str(guesses)) 

