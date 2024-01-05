num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
# both point in the exact address in memory

num2 = 22

print("\nAfter num2 value is updated:")
print("num1=", num1)
print("num2=", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

dict1 = {
    'value': 11
    }

dict2 = dict1
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22
print("\nAfter value is updated:")
print("dict1=", dict1)
print("dict2=", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

# dictionaries are mutable while strings are not.

# nodes of linked list operate like a dictionary
# variables will continue to point to the same node even when we change the value

