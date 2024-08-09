# modulo of number without using '%' operator

def modulo(numerator, denominator):
	
	if denominator > 0:
		division = numerator//denominator
		mul = denominator * division
		reminder = numerator - mul
		return reminder
	else:
		return "Invalid"


print(modulo(35,8))      # output = 3
