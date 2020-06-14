# Build a set
fruits = {'apple','mango','banana'}
print(fruits)

# Print fruit in fruits
for fruit in fruits:
    print(fruit)

# Check with in keyword
print("Cherry" in fruits)

# Add elements
fruits.add('Orange')
print(fruits)

# Add more elements at time
fruits.update(['Grape','Pineapple'])

# Print length of set
print(len(fruits))

# Remove item (May give error if item doesn't exist)
fruits.remove('Orange')
print(fruits)

# Remove using discard (Doesn't give error)
fruits.discard('Grape')
print(fruits)

# POP
fruits.pop()
print(fruits)

# Join sets
Alphabets = {'a', 'b', 'c'}
Numbers = {1, 2, 3}
Characters = Alphabets.union(Numbers)
print(Characters)

# Update Set
Alphabets.update(Numbers)
print(Alphabets)

# List to set
vegges = ['tomato', 'cabbage']
vegetable = set((vegges))
print(type(vegetable))
fruits.update(vegetable)
print(fruits)

# Copy elements
vegetables = {'Cauliflower', 'Capsicum', 'cabbage'}

common_vegges = vegetables.intersection(vegges)
print(common_vegges)


# Clear
fruits.clear()
print(fruits)

# Delete
del fruits
