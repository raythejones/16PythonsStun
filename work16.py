def union(list1, list2):
    new_list = [var1 for var1 in list1] + [var2 for var2 in list2 if var2 not in list1]
    return new_list

print union([1,2,3], [2,3,4])
print union([1,2,3,4], [2,3,4])
print union([1,2,3,5,7], [2,3,4,5])

def intersection(list1, list2):
    new_list = [var1 for var1 in list1 if var1 in list2]
    return new_list

print intersection([1,2,3], [2,3,4])
print intersection([1,2,3,4], [2,3,4])
print intersection([1,2,3,5,7], [2,3,4,5])

def set_difference(list1, list2):
    new_list = [var1 for var1 in list1 if var1 not in list2]
    return new_list

print set_difference([1,2,3], [2,3,4])
print set_difference([1,2,3,4], [2,3,4])
print set_difference([1,2,3,5,7], [2,3,4,5])

def sym_difference(list1, list2):
    new_list = set_difference(list1, list2) + set_difference(list2, list1)
    return new_list

print sym_difference([1,2,3], [2,3,4])
print sym_difference([1,2,3,4], [2,3,4])
print sym_difference([1,2,3,5,7], [2,3,4,5])

def cart_product(list1, list2):
    new_list = ["(" + str(var1) + ", " + str(var2) + ")" for var1 in list1 for var2 in list2]
    return new_list

print cart_product([1,2], ["red","blue","white"])
