'''
if any two numbers in the input array sum up to a target sum,
the function should return the numbers in any order.

input_array = [3, 8, -10, 18, 5, 7, 1, 23]
sum_number = 13

output_array = [8, 5]
'''
# O(n) time | O(n) space

input_array = [3, 8, -10, 18, 5, 7, 1, 23]
sum_number = 13

def two_number_sum(input_array, sum_number):
    for num in input_array:
        remainder = sum_number - num
        if remainder in input_array:
            return [num, remainder]
    return []        

print(two_number_sum(input_array, 13))


def two_number_sum_improved(input_Array, sum_number):
    input_array.sort()
    left_idx = 0
    right_idx = len(input_array) - 1
    while left_idx < right_idx:
        sum_of_numbers = input_Array[left_idx] + input_Array[right_idx]
        if sum_of_numbers == sum_number:
            return [input_Array[left_idx], input_Array[right_idx]]
        elif sum_of_numbers < sum_number:
            left_idx += 1
        elif sum_of_numbers > sum_number:
            right_idx -= 1
    return []

print(two_number_sum_improved(input_array, 13))

