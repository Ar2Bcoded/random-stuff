# collatz second attempt, this time with try and except

def collatz(number):
	if number % 2 == 0:
		number //= 2
	else:
		number = 3 * number + 1
	return number

attempts = 0
while True:
	try:
		x = int(input('Feed me an integer, mortal! '))
		while x != 1:
			x = collatz(x)
			print(x)
			attempts += 1
		if x == 1:
			print('Finally finished! It took us %s attempts!' % attempts)
			break
	except ValueError:
		print('That\'s not an integer, you fool!')