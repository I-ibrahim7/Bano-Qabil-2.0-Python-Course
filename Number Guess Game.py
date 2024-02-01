
#NUMBER GUESSING GAME
#MUHAMMAD IBRAHIM
#03320821157

#WELCOME MESSAGE FOR USER
print("Welcome to my guess game ;) ")

#Taking User Input: For YES or NO:
user_input = input("Do you want to play: ").lower()

#Using IF ELSE Conditions for YES or NO:
if user_input == "yes":
    print("LET'S GOOO!")
else:
    print("Kia itna bura hon mai??  :(")
    exit()  
print("Guess a number between 1 to 50")

#The number for Guessed is 5
num = 5

#Total attemtps to guess the number are 5:
given_attempts = 5

#using [FOR LOOP] for given attempts:
for attempts in range(1,given_attempts + 1):

#Taking user input as INTEGER:
    guess = int(input("input your guess here: "))

#IF or ELIF Conditions for the GUESS NUMBER:    
    if guess == num:
        print(f"You guess it right in {attempts} attempt")
        break
    elif guess >  40:
        print(f"Attempt no: {attempts}")
        print(f"Your number is too far away from the guessed number :(")
    elif guess > 30:
        print(f"Attempt no: {attempts}")
        print("Think of a smaller number ;)")
    elif guess > 20:
        print(f"Attempt no: {attempts}")
        print("Think of a smaller number ;)")
    elif guess > 10:
        print(f"Attempt no: {attempts}")
        print("you are very close to it, again think a small number")
    elif guess > 5:
        print(f"Attempt no: {attempts}")
        print("you are really close to it. Its a smaller number than that number ")
    elif guess < 5:
        print(f"Attempt no: {attempts}")
        print("Just a bigger number than that one :)")

else:
    print(f"You ran out of luck the correct number was {num}")
    
print("Thanks for playing")   



        
        
    



