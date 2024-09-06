def decimal_to_binary(decimal):
    if decimal == 0:   # agar zero hoga toh zero return kar dega
        return "0"
    
    if decimal < 0:
        return '-' + decimal_to_binary(-decimal)
    
    binary_str = ''
    while decimal > 0:
        binary_str = str(decimal%2) + binary_str       # convert decimal number to binary number repeatedly by dividing it frequently
        decimal = decimal // 2
    return binary_str

def binary_subtract_decimal(a, b):       # This function compare the binary representation of the result of subtracting one decimal number from another
    result = a - b
    
    return decimal_to_binary(result)

a = 8
b = 4

result = binary_subtract_decimal(a, b)
print("Subtraction result in binary:", result)
