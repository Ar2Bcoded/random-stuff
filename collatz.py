# collaztz sequence - always evaluates to 1.
def collatz(number):
	if number % 2 == 0:
		number //= 2
	else:
		number = 3 * number + 1
      
	return number

		
    

x = int(input('Type a number: > '))
attempts = 0

try:
	while x != 1:
		x = collatz(x)
		print(x)
		attempts += 1
except ValueError:
	print('%s is not a number!' % x)
print('Finally finished! It took us %s attempts!' % attempts)
