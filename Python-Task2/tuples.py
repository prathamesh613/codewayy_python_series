# Creating Tuple
bills = (1,5,10,20,50,100,200,500,2000)

# Tuple index
print(bills[3])

# Negative Indexing
print(bills[-2])

# Slicing Tuple
print(bills[2:5])
print(bills[:3])
print(bills[4:])

# Negative Index Slicing
print(bills[-5:-1])

# Workaround to change tuple values
bills_list = list(bills)
bills_list.insert(8,1000)
new_bills = tuple(bills_list)

# Loop through tuple
for bill in bills:
    print(bill)

# Check item
if 20 in bills:
    print("20$ Bill Present")

# Length of Tuple
print(len(bills))

# Create Tuple With One Item (Notice the comma)
fruits = ('apple',)
print(type(fruits)," is a tuple")

fruit = ('apple')
print(type(fruit)," is not a tuple")

# Deletion Raises error
# del bills

# Joining Two Tuples
candy = ('cadbury', 'nestle')
chips = ('lays',)
snacks = candy + chips
print(snacks)

# List to tuple
biscuit = ('Krack Jack',)
biscuits = ('parleG','Marie Gold')
cookies = tuple(biscuits) + biscuit
print(cookies)

# Count of element occurence
print(cookies.count('Krack Jack'))

# Index of Element
print(cookies.index('Marie Gold'))
