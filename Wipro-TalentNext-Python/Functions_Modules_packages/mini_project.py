import Functions_Modules_packages.mymodules as mymodules 

#1.Write a Python function that accepts a hyphen-separated sequence of colors as input and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
def sort_colors(input_string):
    colors = input_string.split("-")
    colors.sort()
    return "-".join(colors)

input1 = "green-red-yellow-black-white"
output1 = sort_colors(input1)
print("Output 1:", output1)

#2. Write a module called mymodule.py that contains the following functions:

# The code Functions are in string_utils.py file
name = "bob"
mymodules.ispalindrome(name)
mymodules.count_the_vowels(name)
mymodules.frequency_of_letters(name)