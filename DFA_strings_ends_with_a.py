alphabet = {'a', 'b'}

def DFA_strings_ends_with_a(text):
    final_state = 'q1'
    state = q0(text)
    if state == final_state:
        return state #accepted
    else:
        return state #rejected 

def q0(text):
    if text == "":
        return "q0"
    elif text[0] in alphabet:
        if text[0] == 'a':
            return q1(text[1:])
        else:
            return q0(text[1:])
    return "q0"

def q1(text):
    if text == "":
        return "q1"
    elif text[0] in alphabet:
        if text[0] == 'b':
            return q0(text[1:])
        else:
            return q1(text[1:])
    return "q1"

text = input("Enter the string: ")
print(DFA_strings_ends_with_a(text))
print(DFA_strings_ends_with_a(text))
