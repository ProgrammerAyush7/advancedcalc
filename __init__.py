class Calculator:
	
	"""
	Main Class
	Calculates With 2 Numbers
	
	Author: Programmer Ayush
	Discord: Programmer Ayush#8357
	YouTube: Ayush's Magical World Of Science
	"""
	
	# Main Function (__init__)
	
	def __init__():
		instructions = 'This Calculator can Operate with only 2 Numbers.'
		
		
	# Add Function
	# Returns the Answer
	# 2 Parameters
	def add(num1, num2):
		return num1 + num2
		
	# Subtract Function
	# Returns the Answer
	# 3 Parameters (num1: int, num2: int, auto_arrange: boolean)
	# The Auto Arrange Parameter Arranges the Numbers to not to get a Negative Answer if True
	# Auto Arrange is False as default
	
	def subtract(num1, num2, auto_arrange: bool = False):
		if auto_arrange == True:
			if num1 < num2:
				return num2 - num1
				
			else:
				return num1 - num2
				
		else:
			return num1 - num2
			
	# Modulus Function
	# Returns the Remainder From the Division of 2 Numbers
	# 2 Parameters
	
	def remainder(num1, num2):
		return num1 % num2
		
	# multiply function
	# returns the product of two numbers
	# 2 parameters
	
	def multiply(num1, num2):
		return num1 * num2
		
	# divide function
	# returns the division of two numbers
	# 2 parameters
	
	def divide(num1, num2):
		return num1 / num2