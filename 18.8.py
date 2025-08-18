# a=('sdska','slxskl','xjhujh')
# print(a)

# a=('dharujjn','apple','banana') # print length of tuple
# print(len(a))

# a=("dedhb",)   # single element tuple
# print(type(a))

# a=('dxscdx') 
# print(type(a))


# a=('dedccd','crdcd','rcecer') # print first element of tuple
# b=(1,2,3,4,5,6)
# c=(True, False, True)
# print(a)
# print(b)
# print(c)

# a=('dahrun',22,'developer',True) # tuple with mixed data types
# print(a)

# a=('dharun', 'developer', 'programmer')
# print(type(a))  # Checking the type of tuple

# a=tuple(('apple', 'banana', 'cherry')) # Creating a tuple from a list
# print(type(a))

# a=('apple', 'banana', 'cherry')  # accessing the second element
# print(a[1])

# a=('dharun', 'developer', 'programmer')
# print(a[-2])  # Accessing the second last element in tuple


# a=('dharrun','developer','programmer')
# print(a[:2])

# a=('dharrun','developer','programmer')
# print(a[:-2])

a=('dharun','developer','programmer')
b=list(a)  # Converting tuple to list
b[2] = 'coder'  # Modifying the list
a=tuple(b)  # Converting list back to tuple
print(a)  # Output: ('dharun', 'developer', 'coder')