def ispalindrome_string(lst):
    filtered_lst = [elem for elem in lst if not isinstance(elem, str)]
    
    left, right = 0, len(filtered_lst) - 1
    
    while left < right:
        if filtered_lst[left] != filtered_lst[right]:
            return False  
        left += 1
        right -= 1
    
    return True 

print(ispalindrome_string([1, 2, 3, 2, 1])) 
print(ispalindrome_string([1, "hello", 2, 3, 2, 1]))
print(ispalindrome_string([1, 2, 3, 4, 5])) 
print(ispalindrome_string([set([1]), set([2]), set([1])]))  
print(ispalindrome_string([{'a': 1}, [1, 2], [1, 2], {'a': 1}]))  
