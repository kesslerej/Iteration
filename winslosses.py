# Make a local change

# iteration pattern
# doing the same thing once

# [1, 5, 7 ,8 , 4, 3]

#def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	#for item in list:
		#print item

#def add_one(list):
	# standard for loop with change
	#for i in range(0, len(list)):
		#list[i] += 1

	#return list

def print_scores(names, wins, losses):
	for i in range(0, len(names)):
		print names[i] , " are " , wins[i], " - " , losses[i]


# filter pattern
def congratulations(names, wins):
	for i in range(0, len(names)):
		if (wins[i] == 6):
			print "Congrats", names[i],"! You are the winningest team this season!"

def congratulations2(names, losses):
	for i in range(0, len(names)):
		if (losses[i] == 7):
			print "Congrats", names[i],"! You are the lossingest team this season!"





# accumlation pattern = a type of iterationj

#def sum(numbers):
	#total = 0
	#for n in numbers:
		#total += n

	#return total

def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = names
	
	return current_max

def average(numbers):
	average = (numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]) / numbers[i]

	print average

def drop(numbers):


#Write a function that finds the averag of the scores
#write a second fucntion that also finds the average, but drops the lowest 2 scores
