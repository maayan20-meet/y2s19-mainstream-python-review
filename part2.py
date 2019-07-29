# Part 2 of the Python Review lab.

def encode(x, y):
	if not (500 < x or x > 1000) or not (1 < y or y < 250):
		print("Invalid input: Outside range.")
		return

	while not is_prime_number(x):
		x += 1

	while not is_prime_number(y):
		y += 1

	return x*y

def decode(coded_message):


	prime_numbers = list()

	for i in range(2, 1000):
		if is_prime_number(i):
			prime_numbers.append(i)

	for i in prime_numbers:
		if coded_message%i == 0:
			break

	return coded_message/i, i


def is_prime_number(x):
	# function will check if a number is a prime
	# :param: x - int, number to check
	# return: True if number is prime, flase other wise
	# credit: https://linuxconfig.org/function-to-check-for-a-prime-number-with-python
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
		return False
    return True


print(decode(encode(550, 200)))