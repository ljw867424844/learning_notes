d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)

# Add
d['Adam'] = 67
d['Tmp'] = 99
print(d)

# Delete
d.pop('Tmp')
print(d)

# Modify
d['Bob'] = 60
print(d)

# Search
print('Thomas' in d)
print(d.get('Thomas'))

s = set([1, 1, 2, 2, 3])
print(s)

# Add
s.add(4)
s.add(666)
print(s)

# Delete
s.remove(666)

# Intersection
s2 = {2, 3, 4}
print(s & s2)

# Union
s3 = {5, 6, 7}
print(s | s3)
