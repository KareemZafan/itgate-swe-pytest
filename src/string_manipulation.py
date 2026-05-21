
def is_equal(str1,str2):
    if str1 == str2:
        return True
    else:           
        return False

def is_capitalized(str1): 
    if str1[0].isupper():
        return True
    else:
        return False   

def is_palindrome(str1):
    str1 = str1.replace(" ", "").lower() # Remove spaces and convert to lowercase
    return str1 == str1[::-1] # Check if the string is equal to its reverse

## madam , level , racecar, a123321a  


def is_uppercase(str1):
    return str1.isupper() # Check if all characters in the string are uppercase 
   

def is_lowercase(str1):
    return str1.islower() # Check if all characters in the string are lowercase 
   

