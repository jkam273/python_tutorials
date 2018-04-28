'''different from c++ arrays : need not be of similar data type, siza can dynamically increase / decrease. '''
'''
What are lists,tuples ?  -- Data structure in Python , mutable ; tuples immutable. 

list.append(elem)
list.remove(elem)
list.insert(index, elem)
list.index(elem) 
list.sort() 
list.reverse() 
list.pop(index)
list.extend(list2)
'''

a = [1,2,3,4,5,66]
b = (9,9,7,6,4,3,3)

print(a)
print(b)

a.append(999)
print(a)
a.remove(4)
a.insert(3,87)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(a.pop(3))
(a.extend(['g','name','apple','bananan']))
print(a)