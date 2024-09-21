def get_valid_invalid_text_count(texts):
    valid_count = 0
    invalid_count = 0
    
    for text in texts:
        if isinstance(text, str):
            if text.strip():
                valid_count += 1
            else:
                invalid_count += 1
                
    return valid_count, invalid_count

list = ['[{(', [45, ("()"), '']]
print(get_valid_invalid_text_count(list))
