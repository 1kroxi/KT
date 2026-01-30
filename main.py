def get_sum(a,b):
    return a + b
def count_capital_letters(letter):
    count = 0
    for char in letter:
        if char.isupper():
            count += 1
    return count
def decode_string(string):
    lower = string.lower()
    result =''
    for char in string:
        count = 0
        for other_char in lower:
            if char.lower() == other_char:
                count +=1
        if count == 1:
            result += '('
        else:
            result += ')'
    return result
def get_odd_count(str):
    count = 0
    chetni = ['2','4','6','8']
    for int in str:
        if int in chetni:
            count +=1
    return count
    
