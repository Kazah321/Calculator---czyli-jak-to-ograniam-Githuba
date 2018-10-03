class Calculator:
	def __init__(self):
		pass
	def calc_add(self,a,b):
		return a+b
	def calc_sub(self,a,b):
		return a-b
		
	def calc_sq(self,a):
		return a*a
	def calc_div(self, a, b):
		return a/b
	def calc_mul(self, a, b):
		return a*b
#test Calculatora
	
x=Calculator()
print(x.calc_add(4,5))
print(x.calc_sub(3,2))
print(x.calc_sq(5))
print(x.calc_div(4,2))
print(x.calc_div(4,2))

