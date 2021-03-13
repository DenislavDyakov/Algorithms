'''
the function should take an array as input and return its product sum as output.
if there are arrays nested in the array, their product sum should be calculated first, 
as well as multiplied by the depth of the nested array.

Example: 
the product sum of [1,[2,[3]]] is:
1 + 2 * (2 + (3 * 3))
'''
input_array1 = [1, [2, [3]]] # should return 23
input_array2 = [2, 4, [6, 8], 3, [2, [14, -8, [4]]]] # should return 173

#O(n) time | O(d) space, where d is depth

def product_sum(input_array, multiplier = 1):
    current_sum = 0
    for elem in input_array:
        if type(elem) == list:
            current_sum += product_sum(elem, multiplier + 1)
        else:
            current_sum += elem
    return current_sum * multiplier

assert product_sum(input_array1) == 23, print("Test failed.")
assert product_sum(input_array2) == 173, print("Test failed.")
