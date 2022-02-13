from itertools import count
import random 
import math 

#input
lower = int(input("Entert the lower number :"))
upper = int(input("enter the upper number: "))

#generating random number between lower and upper 
x = random.randint(lower,upper)
print("\n\tYou've only ",
        round(math.log(upper-lower + 1, 2)),
        "chances to guess the integer!\n")   

count = 0 

while count < math.log(upper - lower + 1, 2):
    count += 1 

    guess = int(input("guess a number : "))

    if x == guess:
        print("congratulation", count," time you try")

        break

    elif x > guess: 
        print("you guessed too small!")
    elif x < guess : 
        print("ypu guess too high ")

if count >= math.log(upper - lower +1,2 ):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")