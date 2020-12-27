'''
the function should takes a string and returns its runlength encoding
the length can only be a number between 1 and 9 to prevent confusions

example: "DDDDDDDDDDDDDDD" = 9D6D
'''

input_string = "AABBBCCCCDDDDDDDDDDDDDD"
# sample output should be: 2A3B4C9D5D

# O(n) time | O(n) space
def run_length_encoding(input_string):
    encoding = []
    runlength = 1

    for i in range(1, len(input_string)):
        first_char = input_string[i - 1]
        next_char = input_string[i]

        if next_char != first_char or runlength == 9:
            encoding.append(str(runlength))
            encoding.append(first_char)
            runlength = 0

        runlength += 1

    encoding.append(str(runlength))
    encoding.append(input_string[len(input_string) - 1])

    return "".join(encoding)

print(run_length_encoding("AABBBCCCCDDDDDDDDDDDDDD"))
