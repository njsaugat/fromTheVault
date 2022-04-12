#number guessing game

def factors(a):
    s=[]
    for i in range(2,a+1):
        if a%i==0:
            s.append(i)
        return s


def multiples(a):
    s=[]
    for i in range(1,11):
        j = i * a
        s.append(j)
    return s


import random
num=random.randrange(1,101)
user=int(input("Enter a number."))
factor=factors(num)
multiple=multiples(num)
clues=[]
clue="one factor of the number is " + str(random.choice(factor))
clue1=f"one of the multiples of the number is {random.choice(multiple)}"
clue2=f"{num+random.randint(1,10)} is greater than the number you are guessing" #functions also can be created for greater and smaller but
clue3=f"{num-random.randint(1,10)} is smaller than the number you are guessing" #to make it shorter I used them directly.
clues.append(clue)
clues.append(clue1);clues.append(clue2);clues.append(clue3)
score=0
for clu in clues:
    if user!=num:
        print("The number you enter didn't match.")
        print(f"Here is one clue \n{random.choice(clues)}")
        score-=10
        print()
        user = int(input("Enter a number."))
    else:
        print("you have guessed it correctly.")
        score+=50
        break
print(f"your score is {score}")