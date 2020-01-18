print(20 > 10)
print(20 == 10)
print( 20 < 10)
print(bool("Hello World"))
print(bool(20))



Pyhton Conditions

Equals                      -> x  ==  y
Not Equals           		-> x  !=  y
Less Than           	    -> x  <   y
Less than or equal to       -> x  <=  y
Greater than                -> x  >   y
Greater than or equal to    -> x  >=  y
Boolean OR                  -> x  or  y , x | y
Boolean AND                 -> x  and y , x & y
Boolean NOT                 ->  not X    


#If Statement

x = 70
y = 60

if x > y:                               #Condition
	print("x is greater than y ")


#Elif 


#Checking conditions

x = 70
y = 70

if x > y :
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else :
	print("x is less than y")


x = 50
y = 150

if x > y :
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else :
	print("x is less than y")

#Short Hand If

if x > y: print("x is greater than y")

#Short Hand If...Else

x = 50
y = 150

print(x)   if x > y    else print(y)

##This will be         #This will be printed
##printed if           #if x < y
## x > y
print(x) if x > y else print(y)

x = 50
y = 40
z = 100

#AND is Logical Operator
if x > y and z > x :
	print("All Conditions are True")

#OR is Logical Operator
if x > y or z > x :
	print("One of the Conditions is True")
elif  x > y and z > y:
	print("All conditions are True")
else:
	print("nothing else")



## Pass Statement

x = 100
y = 50

if x > y:
	pass


---------------

x = int(input("Please enter an integer))

if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print("Zero")
elif x == 1:
	print("Single")
else:
	print("More")



#Nested If is if statements in if statements

x = 50
if x > 10:
	print("x is ten")

    if x > 20:
		print("x is greater than 20")
  	else:
  		print("No , x is not greater than 20")

  	# else is breaker !!!!

  	if x > 10 or x != 10 or x > 20:
  		print("x is greater than 10 and 20")

  	else:
  		print("x is not greater than 10 & 20")

#Pass Statement

x = 100
y = 500

if x > y:
	pass

x










