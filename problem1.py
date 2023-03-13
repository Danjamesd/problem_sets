# Write a program that prints out the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".
#
# Write a program that asks the user to enter a string and then prints out whether that string is a palindrome or
# not. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
# #
# def is_palindrome(w):
#     return w == w[::-1]
# """palindrome in puthon is represented by {word or group of chars}[::-1]"""
#
# w = input('enter any word: ')
# answer = is_palindrome(w)
#
# if answer:
#     print('yes')
# else:
#     print('no')

# Write a program that takes a list of numbers as input and outputs the largest and smallest numbers in the list.
# *************
# We define a function find_min_max() that takes a list of numbers as input.
#
# We initialize two variables min_num and max_num to the first number in the list.
#
# We iterate through the rest of the numbers in the list using a for loop.
#
# Inside the loop, we compare each number with the current value of min_num and max_num. If the number is smaller than min_num, we update min_num. If the number is larger than max_num, we update max_num.
#
# Finally, we print out the values of min_num and max_num using formatted strings.
# *************
#
# def find_min_max(numbers):
#     """
#     This function takes a list of numbers as input and outputs the largest and smallest numbers in the list.
#     """
#     min_num = numbers[0]
#     max_num = numbers[0]
#
#     for num in numbers:
#         if num < min_num:
#             min_num = num
#         if num > max_num:
#             max_num = num
#
#     print(f"The smallest number is: {min_num}")
#     print(f"The largest number is: {max_num}")
#
#
# # Example usage
# numbers = [10, 5, 20, 8, 15]
# find_min_max(numbers)
# In the example usage, we create a list of numbers and pass it to the find_min_max() function. The output will be the smallest and largest numbers in the list, which in this case are 5 and 20 respectively.
# Write a program that asks the user to enter a number and then prints out whether that number is even or odd.

#
# user_number = int(input('select a number and you will see if it is even or odd '))
#
# if user_number % 2 == 0:
#     print('even')
# else:
#     print('is odd')
# Write a program that takes a list of strings as input and outputs the length of the longest string in the list.
#
# Write a program that asks the user to enter two numbers and then prints out the sum, difference, product,
# # and quotient of those two numbers.
# num = int(input('pick a random number: '))
# another_num = int(input('pick another random number: '))
#
# sum_of = num + another_num
# difference_of = num - another_num
# product_of = num * another_num
# quotient_of = divmod(num, another_num)
#
# print(sum_of, difference_of, product_of, quotient_of)
#
# Write a program that takes a list of numbers as input and outputs the sum of all the even numbers in the list.
#
# Write a program that asks the user to enter a sentence and then prints out how many times each letter appears in
# the sentence. Ignore spaces and punctuation.
#
# ##
# def reverse_list(numbers):
#     """
#     This function takes a list of numbers as input and returns a new list with the same numbers in reverse order.
#     """
#
#     reversed_numbers = []
#     for i in range(len(numbers)-1, -1, -1):
#         reversed_numbers.append(numbers[i])
#     return reversed_numbers
#
#
# # Example usage
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = reverse_list(numbers)
# print(reversed_numbers)


#
#
#
#
# for i in range(1, 101):
#     """define a range, which includes all numbers in between"""
#     if i % 3 == 0 and i % 5 == 0:
#         """if there is no remainder when  i/3 and 1/5. Ie if CURRENT NUMBER meets criterie print fizzbuzzz"""
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         """if next evaluated number is multiple of 3 only - ie not also a multiple of 5 - print Fizz"""
#         print('Fizz')
#     elif i % 5 == 0:
#         """conversely to the above, if it is a multiple of 5, then print buzz"""
#         print('Buzz')
#     else:
#         print(i)
# Write a program that asks the user to enter a temperature in Celsius and then converts it to Fahrenheit. The
# formula for converting Celsius to Fahrenheit is F = (C x 1.8) + 32.
# current_temp = int(input('What is the current temperature in Celsius: '))
# convert_to_fahrenheit = (current_temp * 1.8) + 32
# print(convert_to_fahrenheit)
