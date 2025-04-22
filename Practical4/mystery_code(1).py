# What does this piece of code do?
# Answer:count how many times do we need to pick 2 same nubers randomly	 form 1 to 5

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0 # initialise progress
while progress>=0: 
	progress+=1 #counter
	first_n = randint(1,5) 
	second_n = randint(1,5)
	if first_n == second_n:  # if they pick same number
		print(progress)
		break #find the same number, jump out

