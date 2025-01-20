# Brent Grossman - CS-161 Week 2 Homework Assignment

# Part 1, Print out the value of a variable in binary and decimal from.
# x is our variable with its value set as 31,
# using the bin() and hex() functions to print 31 in binary and hexadecimal,
# and using [2:] to exclude the first 2 identifying characters from the bin() and hex() functions
x = 31
print("x is", x, "which is", bin(x)[2:], "in binary, and", hex(x)[2:], "in hex\n")

# Part 2, Identify the error when giving an incorrect input type.
# changing the value of x to 1.825 to see what happens.
if x == 31:
    x = 1.825
    try:
        # Here we get a TypeError because 1.825 is a floating point number,
        # and the bin()/hex() functions can only interpret integers
        print("x is now", x, "which is", bin(x)[2:], "in binary, and", hex(x)[2:], "in hex")
    # I am using try/except here to except the TypeError and convert the value of x to 18
    except TypeError:
        x = 18
        print("x is now", x, "which is", bin(x)[2:], "in binary, and", hex(x)[2:], "in hex\n")

# Part 3, Assigning a binary or hex value to a variable.
y = 0b1011
z = 0xA3
print(y, z, "\n")

# Part 4, You can add numbers in any representation.
w = x + y + z
print("the sum is", w, "\n")


# Compression
# Part 1 and 2, Choose meaningful variable names.
# I kept some of the variables given because they seem good as is
# I decided to make a function here that I can use in this part and part 4
# This function is based off of the instructions for part 1 in compression
# It adds the first 2 inputs together, then divides by the 3rd input, subtracts that from 1,
# then multiplies by 100 and rounds to 2 decimal places to give you a percentage
def compression_percentage(a, b, c):
    return round(((1 - ((a + b) / c)) * 100), 2)

original_size = 240
dictionary_size = 25
compressed_text_size = 148
compression_result = compression_percentage(compressed_text_size, dictionary_size, original_size)
print(f"{compression_result}%\n")

# Part 4? (there is no part 3 under compression)
# to test without copying the numbers in the instructions I chose to allow the user to input their own integer values
original = int(input("Enter your original size: "))
compressed = int(input("Enter your compressed size: "))
dict_size = int(input("Enter your dictionary size: "))
total_size = compressed + dict_size
compression_result = compression_percentage(compressed, dict_size, original)
print(f"Compressed text size: {compressed} characters\n"
      f"\t\tDictionary size: {dict_size} characters\n"
      f"\t\t\tTotal size: {total_size} characters\n"
      f"\tOriginal text size: {original} characters\n"
      f"\t\tCompression: {compression_result}%\n")

# testing this with abnormal inputs like 250 as my original size, and then 300 compressed and 10 dict_size
# I get an output of -24.0%, which shows this works when the compressed size is larger than original
# and testing with the original size 550, with compressed size of 350 and a dict_size of 50
# we get a compression of 27.27%

##########################################  Two's Complement Extra Credit  ##########################################
# Here I am initialising my starting_number variable to be used in my loop
starting_number = 0
flag = False
while not flag:
    # Using try/except and a nested if/else for input validation in a while loop
    try:
        starting_number = int(input("Enter a number that is no larger than 127, and no smaller than -128: "))
        if starting_number > 127 or starting_number < -128:
            print("Please only enter numbers less than or equal to 127, and greater than or equal to -128")
        else:
            flag = True
    except ValueError:
        print("Please only enter numbers less than or equal to 127, and greater than or equal to -128")

# Here I convert the users input into an 8-bit binary number
binary = format(starting_number, "08b")
print(f"Your number in binary is {binary}")

# Using a for loop, this iterates over each bit in the users binary number,
# to then make a new ones compliment number in the ones_comp variable
ones_comp = ""
for bit in binary:
    if bit == "1":
        ones_comp += "0"
    else:
        ones_comp += "1"
print(f"Your number in ones compliment is {ones_comp}")

# This calculates the twos compliment by adding 1 to ones compliment,
# and then creating the new twos compliment in the variable twos_comp
twos_comp = ""
carry = 1   # this is the initial carry for adding 1
for bit in reversed(ones_comp):
    if carry == 1:
        if bit == "1":
            twos_comp = "0" + twos_comp   # this is where 1 + 1 = 0 and carry's 1
            carry = 1
        else:
            twos_comp = "1" + twos_comp   # this is where 1 + 0 = 1 and carry's 0
            carry = 0
    else:
        twos_comp = bit + twos_comp    # once carry equals 0 this just adds the value of bit to twos_comp

print(f"Your number in twos compliment is {twos_comp}")
