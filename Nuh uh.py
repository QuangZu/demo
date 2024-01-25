# Create twwo sets
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set2.add(8)
set1.add(9)
print('set1 has '+ str(len(set1))+' elements')

# Union of two sets
union_result = set1.union(set2)
print('Union:', union_result)

# Intersection of two sets
intersection_result = set1.intersection(set2)
print('Intersection:', intersection_result)

# Difference between 2 sets
difference_result = set1.difference(set2)
print('Difference:', difference_result)

#Symetric difference
symetric_difference_result = set1.symmetric_difference(set2)
print('Symetric Difference:', symetric_difference_result)

#Check if set1 is a subset of set2
sub_support = set1.issubset(set2)
print('Subset:', sub_support)

#Check if set1 is a superset of set2
is_support = set1.issuperset(set2)
print('Issuperset:', is_support)