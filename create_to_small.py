# convert_to_small_case

def convert_to_small_case(text):
	result = ""
	for char in text:
		if('A' <= char <= 'Z'):
			result = result + chr(ord(char)+32)
		else:
			result = result + char 
	return result
	

print(convert_to_small_case("SGGSNed"))
print(convert_to_small_case("SGGSNed"))
