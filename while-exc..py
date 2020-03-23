n=1
previousNumber=0
nmax=50

while n<=nmax:
    print(n,n+previousNumber)
    n+=1
    previousNumber+=1
print('-------')

import random
my_number = random.randint(0,20)
guess=-1

print("Guess my number!")
while guess != my_number :
 
    guess = int(input())
    
    if guess == my_number:
        print("You are right! It was:",my_number)
    elif guess>my_number:
        print("Sorry- my number is smaller than", guess, "Try again!")
    else:
        print("Sorry- my number is greater than", guess, "Try again!")
