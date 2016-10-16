# collatz sequence - always evaluates to 1.
def collatz(number):
	if number % 2 == 0:
		number //= 2
	else:
		number = 3 * number + 1
	return number

		
x = input('Type a number: > ')
attempts = 0

if x.isdigit():

        x = int(x)
        while x != 1:
                print(collatz(x))
                x = collatz(x)
                attempts += 1
                
        print('Finally finished! It took us %s attempts!' % attempts)
else:
	print('%s is not a number!' % x)
