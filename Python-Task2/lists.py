# Creating list of Mobile Phone Manufacturers
brands = ['apple','samsung','xiaomi','motorola','oneplus']

# Just Printing
print("Brands are : ",brands)

# Indexed access
print(brands[2])

# Negative Indexing
print(brands[-2])

# Slice in list
print(brands[1:4])
print(brands[:2])
print(brands[3:])

# Negative indexing sliced
print(brands[-3:-1])

# Changing Item
brands[2] = "Mi"

# Looping throug list
for brand in brands:
    print(brand)

# Check for item
if 'samsung' in brands:
    print('Samsung Exists')

# length of list
print(len(brands)," is the length of list")

# Add item to end
brands.append("LG")
print(brands)

# Add item at index
brands.insert(2, 'Vivo')
print(brands)

# Remove item
brands.remove('Vivo')
print(brands)

# Pop last item
brands.pop()
print(brands)

# Deleting with del
del brands[2]
print(brands)

# Copy list
new_brands = brands.copy()
print(new_brands)
brands.pop()

# Copy list using conversion to list constructor
newer_brands = list(brands)
print(newer_brands)

# Joining Lists
total_brands = brands + new_brands
print(total_brands)

# Joining lists using for loop and append
newer_brands.clear()
for brand in total_brands:
    newer_brands.append(brand)
print(newer_brands)

# Extend
new_brands.extend(newer_brands)
print(new_brands)

# Tuple to list
indian = ('Lava', 'Micromax')
indian_brands = list(indian)
indian_brands.append('Freedom 251')
print(indian_brands)

# Count occurence of element in list
print(total_brands.count('samsung'))

# Print Index
print(brands.index('samsung'))

# Reverse List
print(brands.reverse())

# Sort list
print(brands.sort())

# Clear list
brands.clear()
print("Brands are : ", brands)
