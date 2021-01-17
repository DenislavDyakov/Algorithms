'''
Define a function that takes a string as input and returns a boolean if the input is a palindrome
'''

# O(n) time | O(1) space


input_string = "opsspo"

def is_palindrome(input_string):
    left = 0
    right = len(input_string) - 1
    
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        else:
            left +=1
            right -= 1
    return True

print(is_palindrome(input_string))
