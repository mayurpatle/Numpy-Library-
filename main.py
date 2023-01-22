import  numpy as  np
a  =  np.array([0 , 1 , 2 , 3 ])   #similary you can create  a boolean and  string array  


print(a)
print(a[3 ])

print(np.arange(10))
b =  np.arange(10000)  

""" two dimentional  array   """

t  =  np.array([[1, 2  , 3 ] ,  [ 6  , 7 ,7 ]]) 

print(t.ndim)

print(t.shape)   #two  rows  and  three  columns  

print(len(t))

"""three  dimentional  array """

three = np.array([[[1 , 2  , 3  ] , [5 , 6 ,7  ]]  , [[2 , 4 ,6  ] ,  [ 7  , 8   , 9 ]]])
print(three.ndim)

print(three.shape)

