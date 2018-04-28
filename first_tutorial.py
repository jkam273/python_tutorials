'''
topics to be covered 
1) printing on console
2) commenting in python 
3) declaring variables, assigning them variables
'''

#print('hello to my first python tutorial')
a = 2
b = 2.5
c = 'my first string'

def myFunction():
    global a
    a = 4
    print(a) 


myFunction()
print(a,b,c) 
