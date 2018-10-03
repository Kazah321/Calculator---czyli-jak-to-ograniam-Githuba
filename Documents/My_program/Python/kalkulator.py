class Calculator:
	def __init__(self):
		pass
	def calc_add(self,a,b):
		return a+b
	def calc_sub(self,a,b):
		return a-b


	def calc_sq(self,a):
		return a*a
#test Calculatora
	
x=Calculator()
print(x.calc_add(4,5))
print(x.calc_sub(3,2))
print(x.calc_sq(5))