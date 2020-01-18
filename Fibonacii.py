#Fibonacii



# n = int(input('Please enter a number: '))

def fib(n):
	a,b = 0,1
	while a < n:
			print(a,end='')
		    a, a=b ,  a+b
	print()



def fib2(n):    #return fibonacii series up to n
	result = []
	a , b = 0,1
	while a < n:
		result.append(a)
		a , b= b , a+b
	return result
