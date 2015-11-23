#Importing Random module
import random

def game():
    #Initial points
    points=50

    #Game starts 
    print "----------------------------------------------------------"
    print "Hello! What is your name? =>",
    myName=raw_input()

    #Randomizing the number to be guessed
    guessnum=random.randint(1, 20)

    #Initialising Chance as 1
    chance=1

    #Time to guess the number!
    print "Hola", myName, ",Lets play Guess The Number!"
    print "----------------------------------------------------------"
    print "The number is between 1 and 20"
    print "------------------------START-----------------------------"

    while (chance<=5):
        if chance!=5:
            print myName, ",Your", chance, "attempt =>",
        else:
            print myName, ",Your Final attempt =>",
            
        guess=input()
        
        if (guess==guessnum):
            print "Woah",myName,"!! Great Job Buddy!"
            print "You guessed it in the", chance, "th attempt"
            print "You have", points, "points"
            print "Thank You for playing Guess The Number"
            print "--------------------------END-----------------------------"
            break
            
        else:
            points=points-10
            print "Awww...That's not the number I thought of!"
            print "You have lost 10 points and a chance!"
            print "You now have", points, "points and", 5-chance, "chances"
                
            if (guess>guessnum):
                print "Pss..Take a Hint: The number you thought is bigger than what I thought"      
            else:
                print "Pss..Take a Hint: The number you thought is smaller than what I thought"

            
                
        print "----------------------------------------------------------"
        chance=chance+1
        
    else:

        print "Oops! Your time is up", myName
        print "The number I thought was", guessnum
        print "Thank You for playing Guess The Number"
        print "--------------------------END-----------------------------"


game()
print "Do you want to play again (Y/N)?"
a=raw_input()

if (a=='y' or a=='Y'):
    game()

else:
    print "See ya!"
    
    

    



