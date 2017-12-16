#Get User Input
def main():
    lowerb=0
    upperb=100
    print("Welcome to the Guess My Number Game!")
    user_guess=input("Choose a whole number between 1 and 100:")
    user_guess=int(user_guess)
    computer_guess=guess_process(lowerb,upperb)
    if(computer_guess==user_guess):
        print("Your number is ", computer_guess, "!!")
    else:
        print("My bad, dog, there was an error")
        
def guess_process(lowerb,upperb):
    found_guess=False
    while(found_guess==False):
        guess=(upperb-lowerb)/2
        guess += lowerb
        guess=int(guess)
        print("Is your number ",guess, "?")
        response=input("Y / N:  ")
        if(response=="N"):
            print("Is your number higher or lower than: ", guess, "?")
            second_response=input("H / L:  ")
            if(second_response=="H"):
                lowerb = guess
            elif(second_response=="L"):
                upperb = guess
            else:
                print("Please respond with H or L")
        elif(response=="Y"):
            found_guess=True
        else:
            print("Please respond with Y or N")
    return guess
            
main()