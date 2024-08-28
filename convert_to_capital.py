# convert_to_capital_case

def convert_to_capital_case(text):
	result = ""
	for char in text:
		if('a' <= char <= 'z'):
			result = result + chr(ord(char)-32) 
		else:
			result = result + char #if no char is small, print same
	return result


print(convert_to_capital_case("SGGSNed"))
print(convert_to_capital_case("SGGSNed"))
