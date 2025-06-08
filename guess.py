import random

def guess(x):

        random_number = random.randint(1,x)

        guesss = 0 

        while guesss != random_number :
                
                guesss = int(input(f"enter the number between {x} : "))

                if guesss < random_number:
                        print("your guess is low")

                elif guesss > random_number:
                        
                        print("damn, its too high")


        print(f"superb you guessed the correct number and that is {guesss} ")


guess(10)
