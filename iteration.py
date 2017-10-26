# iteration pattern
# doing the same thing once for each member of a list

# [1, 5, 7 ,8 , 4, 3]

# Make a change

# Make a new change

def print_list(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def add_one(list):
	# standard for loop with range
	for i in range(0, len(list)):
		list[i] += 1

	return list

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern - a type of iteration
# exclude a calculation from list members

def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"


# accumulation pattern - a type of iteration
# keep track of other data as we go

def sum(numbers):
	total = 0
	for n in numbers:
		total += n

	return total


def max(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

# homework -> 
	# a) write a function that finds the average of the scores
	# b) write a second function that also finds the average, 
	#    but drops the lowest 2 scores


def average(scores):
	print (float(sum(scores)) / len(scores))

def drop(scores):
	current_min = scores[0]
	for s in scores:
		if s < current_min:
			current_min = s

	current_min2 = scores[2]
	for s in scores:
		if s < current_min2 and not current_min:
			current_min2 = s

	return (float(sum(scores)-current_min-current_min2) / (len(scores) - 2))

def fizz_buzz(numbers):
	for n in numbers:
		if n % 3 == 0 and n % 5 == 0:
			return 'FizzBuzz'
		elif n % 3 == 0:
			return 'Fizz'
		elif n % 5 == 0:
			return 'Buzz'
		else:
			return 'Bazz'


	