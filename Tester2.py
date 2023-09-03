import re

string = "The number is -123, but there can be anything around it!"
number = int(re.search(r'-?\d+', string).group())
print(number)