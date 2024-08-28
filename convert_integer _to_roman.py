def rom(string, base):
    num = int(string, base)
    
    def int_to_roman(num):
        roman_num = ''
        
        if num >= 1000:
            roman_num += 'M' * (num // 1000)
            num %= 1000
            
        if num >= 900:
            roman_num += 'CM'
            num -= 900
            
        if num >= 500:
            roman_num += 'D'
            num -= 500
        
        if num >= 400:
            roman_num += 'CD'
            num -= 400
        
        if num >= 100:
            roman_num += 'C' * (num // 100)
            num %= 100
        
        if num >= 90:
            roman_num += 'XC'
            num -= 90
        
        if num >= 50:
            roman_num += 'L'
            num -= 50
        
        if num >= 40:
            roman_num += 'XL'
            num -= 40
        
        if num >= 10:
            roman_num += 'X' * (num // 10)
            num %= 10
        
        if num == 9:
            roman_num += 'IX'
            num -= 9
        
        if num >= 5:
            roman_num += 'V'
            num -= 5
        
        if num == 4:
            roman_num += 'IV'
            num -= 4
        
        if num >= 1:
            roman_num += 'I' * num
        
        return roman_num
    
    return int_to_roman(num)

string_input = "0o64"  
base = 8
print(rom(string_input, base))
