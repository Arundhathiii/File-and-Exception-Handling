# Exercise 1: Write a Python program to read a file and display its contents
# file1=open("C:\\Users\\aniru\\Desktop\\Hello.txt",'r')
# print(file1.read())

# Exercise 2: Write a Python program to copy the contents of one file to another file
# file1=open("C:\\Users\\aniru\\Desktop\\Source_file.txt","r")
# file2=open("C:\\Users\\aniru\\Desktop\\Dest_File.txt","w")
#
# file2.write(file1.read())
#
# file1.close()
# file2.close()

# Exercise 3: Write a Python program to read the content of a file and count the total number of words in that file.
# with open("C:\\Users\\aniru\\Desktop\\Source_file.txt", "r") as file2:
#     contents = file2.read()
#     print(contents)
#     words = contents.split()
#     word_count = len(words)
#     print("Total number of words:", word_count)

"""
Exercise 4: Write a Python program that prompts the user to input a string and converts it to an integer.
Use try-except blocks to handle any exceptions that might occur
"""
# a = input("The string which is to be converted to int: ")
# try:
#     b = int(a)
#     print(b, "The string converted to integer")
# except ValueError:
#     print("This string cannot be converted to integer")
# except Exception as e:
#     print("An unexpected error occurred:", e)

"""
Exercise 5: Write a Python program that prompts the user to input a list of integers 
and raises an exception if any of the integers in the list are negative
"""
# list = []
# try:
#     user_input = input("Enter a list of integers > 0 (space-separated): ")
#     list = [int(x) for x in user_input.split()]
#     if any(x <= 0 for x in list):
#         raise ValueError("List must contain only positive integers")
#     print(list)
# except ValueError as e:
#     print(e)

"""
Exercise 6: Write a Python program that prompts the user to input a list of integers 
and computes the average of those integers. Use try-except blocks to handle any exceptions that might occur.
use the finally clause to print a message indicating that the program has finished running.
"""
# try:
#     user_input = (input("Enter a list of integers(space-seperated):"))
#     integers = [int(x)for x in user_input.split()]
#     average=sum(integers)/len(integers)
#     print("The average is:",average)
# except ValueError:
#     print("Invalid input!Please enter a list of integers.")
# except ZeroDivisionError:
#     print("Cannot compute average of an empty list!")
# finally:
#     print("Program finished running.")

"""
Exercise 7 : Write a Python program that prompts the user to input a filename and writes a string to that file.
Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception
occurred.
"""
# try:
#     filename = input("Enter a filename: ")
#     with open("C:\\Users\\aniru\\Desktop\\Sample Test.txt", 'w') as file:
#         file.write("Hello, World!")
#     print("Welcome! Your file has been created successfully.")
# except IOError as e:
#     print("Error: An I/O error occurred:", e)
# except Exception as e:
#     print("An unexpected error occurred:", e)
