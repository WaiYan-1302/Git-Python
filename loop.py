





1
2
3
4
5
6

While loop requires variable ready


x = 1
while x < 7;
	print(x)
	if x = 5;
		break
	x += 1
1
2
3
4

++++++++++++


for x in "pineapple":
	print(x)
 
p
i
n
// Print out all letters in the sting line by line
	


***************************************
break scenario


fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pineapple":
		continue
		print(x)

// continue statement 
exclude the given argument

In above program..................

"pineapple" is left though every members on 
the list is print
********************************************


for x in fruits:
	if x == "banana"
		   continue
	if x == "coocnut"
		    continue
	print(x)



for x in range(10):
	print(x)



// range is a function that determine the range of 0 to given integer


range starts from zero 
s
**********

NumberA =[1,2,3,4,5]
NumberB =[1,2,3,4,5]


for x in range(1, 2, 3, 4, 5):
	for y in range(1,2,3,4,5):
		print(y)


// !!!!!! range can handle at most 3 arguments 
    !!!!!!!

for x in NumberA:
	for y in NumberB:
		print(x ,y) 
		// for loops are nested //

## "pass" function

**********pass function skips the argument above ///
/
words = ["cat","window","defenstrate"]
for w in words:
	print(w,len(w))



for n in range(2,10):
	for x in range(2, n):
		if n % x == 0:
			print(n,'equals',x,'*',n//x )
			break
		else:
			print(n, 'is a prime number


_________________________________


for num in range(2,10):
	if num % 2 == 0:
		print("Found an even number",num)
		continue 
	print("Found a number" , num)

// index difference 
second " print " argument is not insde the if 
statement........
-------------------------------


>> Fibonacii

def fib(n):
	a , b = 0,1
	while a < n:
		print(a , end=' ')
		a , b = b, a+ b
	print()

