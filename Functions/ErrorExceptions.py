#keyboardInterrupt

# 		break
# 		print("Oops! That was no valid number.  Try again...")
# 		print(x)
# 		x = int(input("Please enter a number: "))
# 	except ValueError:
# 	try:
# while True:

# -------------------------------------------------------------------------

#OSError , ValueErro

# import sys

# # try:
# # 	f = open('myfile.txt')
# # 	s = f.readline()
# # 	i = int(s.strip())
# # except OSError as err:
# # 	print("OS error: {0}".format(err))
# # except ValueError:
# # 	print("Could not convert data to an integer.")
# # except:
# # 	print("Unexpected error:" , sys.exc_info()[0])
# # 	raise

# # ---------------------------------------------------------------------------

# try:
# 	text = input('Enter something--> ')
# except EOFError:
# 	print('Why did you do an EOF on me?')
# except KeyboardInterrupt:
# 	print('You cancelled the operation.')
# else:
# 	print('You entered. {}'.format(text))

#------------------------------------------------------------------------------




#Raising Exceptions

class ShortInputException(Exception):
	'''A user-defined exception class.'''

	def __init__(self, length ,atleast):
		Exception.__int__(self)
		self.length = length
		self.atleast = atleast

try:
	text = input('Enter something-->')
	if len(text) < 3:

		raise ShortInputException(len(text),3)
	if print(text.islower) == False :
		raise CapitalException()

except EOFError:
	print('Why did you do an EOF on me?')

except ShortInputException as ex:
	print(('ShortInputException: The input was'+
		'{0}long, except at least{1}')
	.format(ex.length, ex.atleast))


 
else:
	print('No exception was raised.')
