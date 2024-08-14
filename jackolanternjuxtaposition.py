# Take input as a string
numbers_str = input()
# Split the string into a list of numbers
numbers = [int(x) for x in numbers_str.split()]
result = numbers[0] * numbers[1] * numbers[2]

# Print the result
print(result)