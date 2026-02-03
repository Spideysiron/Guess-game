from random import randint

def guess():
    comp_num = randint(1,100)
    guesses = 0
    while guesses < 5:   
        user_num = input("Guess the number(1-100) : ")
        if user_num.isdigit():
            user = int(user_num)
            if  1 <= user <= 100:
                guesses += 1
                if user > comp_num:
                    print("Too high")
                        
                elif user < comp_num:
                    print("Too low")
                        
                else:
                    print(f"Correct! You guessed in {guesses} attempts.")
                    break
            else:
                print("Enter number between 1 to 100")
        else:
            print("Enter a valid number")
    else:
        print(f"Game over! The number was {comp_num}")


while True:
    guess()
    again = input("Do you want to play again? (y/n): ").lower().strip()
    if again != "y":
        print("Thanks for playing!")
        break


