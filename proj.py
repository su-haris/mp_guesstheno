import random

#Initial points
points=50

print "Hello! What is your name?"
myName = input()

#Randomizing the number to be guessed
guessnum=random.randint(1, 20)

chance=0

print "Hi", myName, ",Lets play guess the number!"
print "The number is between 1 and 20"
print "Lets start!!!"

while (chance<=5):
	print myName, ",Your", chance, "attempt"
	guess=input()
	
	if (guess==guessnum):
		print "Woah, great job buddy!"
		print "You guessed it in the", chance, "th attempt"
		print "You have", points, "points"
		break()
		
	else:
		chance+=1
		points=points-10
		print "That's not the number I thought of!"
		print "You have lost 10 points and a chance!"
		print "You now have", points, "points and", 5-chance, "chances"
		
		if (guess>guessnum):
			print "Hint: The number you thought is bigger than what I thought"
			
		else:
			print "Hint: The number you thought is smaller than what I thought"
			
	chance=chance+1
	
	
print "Oops! Your time is up", myName
print "The number I thought is", guessnum
	



