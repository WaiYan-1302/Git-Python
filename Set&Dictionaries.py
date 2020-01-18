#Sets

#includes a data type for sets
#Curly braces or the set() function can be used to create sets.

basket = {'apple' , 'orange' , 'apple' , 'pear' , 'orange' , 'banana'}
print(basket)

# Sets or the Curly Braces shit remove duplicated elements

'orange' in basket
>> True
'pen' in basket
>>False

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
aa                 #unique letters in a 
a - b              #letters in a but not in b 
a | b              #letters in a or b or both
a & b              #letters in  both a and b       
a ^ b              #letters in a or b --- but not both

a = {x for x in 'abracadabra' if x not in 'abc'}
a

--------------------
#Membership testing 
fruits = {"apple" , "banana" , "cherry" , "kiwi" , "melon" , "mango"}
print("cherry" in fruits)


fruits.add("cucumber")
## It adds cucumber in the set
fruits.update("grape" , "water melon")
# It adds the elements but by tearing and breaking them up into single individual characters

fruits.remove("banana")
#It will remove the indicated object
fruits.discard("kiwi")
#It will also remove the indicated object too

##append function is useless for Sets

>>> Dictionaries
#Dictionaries

#Another useful data type built into Python is dictionary

tel = {'jack' : 4098, 'sape': 4139}
tel['guido'] = 4127
tel[0]

tel['jack']

#It will display the jack and its value
#It works in pairs

list(tel)

sorted(tel)
#It sorts the elements
#It won't work until it's elements are ""list format""

'guido' in tel
'sape'  not in tel




dict([('sape',4139), ('guido',4127), ('jack', 4098)])
dict(sape=4139, guido=4127,jack=4098)


#When looping through dictionaries

knights = {'gallahad' : 'the pure' , 'robin': 'the brave'}
for k,v in knights.items()
	print(k,v)
###  Here k indicates key 
###  v indicates value
######  So there's only two 
knights = {'gallahad' : 'the pure' , 'robin': 'the brave','sape': 23456}

for x,y in knights.items():
	print(x,y)

for i,v in enumerate(['tic' , 'tac' , 'toe']):
		print(i,v)


>> 0 tic
>> 1 tac
>> 2 toe
### If there's no index
## IT'll create it's own one


questions = ['name' , 'quest' , 'favourite color']
answers = ['lancelot' , 'the holy grail' , 'blue']
for q,a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q,a)



 
