#python RaiseException.py

class ShortInputException(Exception):
	'''A user-defined exception class.'''
class LongInputException(Exception):


	def __init__(self, length ,atleast):
		Exception.__int__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something-->')
	if len(text) < 3 :
		raise LongInputException(len(text), 3)
	elif len(text) > 10:
		raise LongInputException(len(text),10)
	elif text.islower() == False :
		print("Capital letter is unacceptable")
		


except EOFError:
	print('Why did you do an EOF on me?')

except ShortInputException as ex:
	print(('ShortInputException: The input was' +
		'{0}long, except at least {1}')
	.format(ex.length, ex.atleast))


except CapitalException as cap:
	print(('Captial case is unacceptable').format(cap.text()))

except LongInputException as Lex:
		print(('LongInputException: The input was' +
			'{0}long, except at least {1}')
		.format(ex.length, ex.atleast)) 

else:
	print('No exception was raised.')

#https://docs.python.org/3/tutorial/errors.html#exceptions

#----------------------------------------------------------

# import time

# f = None
# try:
# 	f = open("poem.txt")
# 	# Our ususl file-reading idiom

# 	while  True:
# 		line f.readline()
# 		if len(line) == 0:
# 			break
# 		print(line, end='')
# 		sys.stdout.flush()
# 		print("Press ctrl+c now")

# 		#To make sure it runs forr a while 

# 		time.sleep(2)

# except IOError:
# 		print("Could not fine file poem.txt")

# except KeyboardInterrupt:
# 		print("You ancelled")

# finally: 
# 		if f :
# 			  f.close()
# 		print("Cleaning up the file")  
