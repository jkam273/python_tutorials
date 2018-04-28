# import random

# def addRand():
#     randomValue = random.randint(0,9) * 10 #assigns random integer value
#     return randomValue


'''
contents - 
This tutorial

1) Dictionaries - key : value #pairs -- shud have unique keys 
dictionary specific functions
1) copy() , if not copied creates reference copies
2) update( var )
3) del obj[key]
4) items() - returns list of (key ,value) pairs 
5) keys() - returns list of keys 
'''

myDict = { 'abhishek': 65 , 'ankita' : 70 , 'sid': 75 , 'pankaj' : 95 }
# myCopy = myDict.copy()
myCopy = myDict
myCopy.update({'abhishek': 55})
print('original  ', myDict)
print('firstCopy ', myCopy)   
del myCopy['pankaj']
print('deleted pankaj' , myCopy)
print('all items in dict copy ' , myCopy.items()) # [(key,value),(key,value)]
print('all keys in dict copy ' , myCopy.keys())





