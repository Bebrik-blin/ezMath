const(pi) = 3.14159
depth = 10


def power(base ,pow):

	k = base

	for i in range(pow):
		base = base*k

	return(base)

def factorial(base):
	k = 1
	i = 0

	while i <= base:
		i += 1
		k = k*i

	return(k)

def mroot(base, pow, depth):
	i = 0

	while power(i, pow) <= base:
		if(power(i, pow) == base):

			return(i)

		i+=depth*0.1

	if((power(i, pow) > base) and (power(i-1, pow) < base)):
