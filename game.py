import random
import time

print("Welcome to Mastermind (CLI Edition)")

#Choose dificulty
digits=int(input("Choose difficulty(3/4/5 digits):"))
if digits < 3 or digits > 5:
    digits = 4 #set as default

#Generate Random Number
num=random.randrange(10**(digits-1),10**digits)

#Attempt limit
max_attempts=10
counter=0

#Strat timer
start=time.time()

#First Guess
n=int(input(f"Guess the {digits}-digit number: "))

if n==num:
    print("Great! You guessed the number in just 1 try! You're a mastermind!")
else:
    while n != num:
        counter += 1

        if counter>=max_attempts:
            print("Game Over! You ran out of attempts.")
            print("The number was:",num)
            break

        count=0
        n=str(n)
        num_str=str(num)
        correct=['X']*digits

        #Check digit by digit
        for i in range(digits):
            if n[i] ==num_str[i]:
                count += 1
                correct[i] =n[i]


        #Feedback
        if(count < digits) and (count != 0):
            print("Not quite the number. But you did get",count, "digit(s) correct!")
            print("Also these numbers in your input were correct:")
            print(' '.join(correct)) #add spaces between list
            print("Attempts left:",max_attempts-counter)
            n=int(input("Enter your next choice of numbers: "))

        elif count == 0:
            print("None of the numbers in your input match.")
            print('Attempts left:',max_attempts-counter)
            n=int(input("Enter your next choice of numbers: "))

    if n == num:
        end=time.time()
        print("You've become a Mastermind!")
        print("It took you only",counter, "tries")
        print("Time taken", int(end-start), "seconds")