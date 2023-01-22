import  numpy as np 

a  = np.arange(10) 
print(a)
print(a.dtype)

b  = np.arange(1  ,  15 ,  2 )  #start  , end (exclusive)  , step  
print(b)

#linspace futnion  -  to  create  points  between  two numbers  
c  = np.linspace(0  ,   5  ,  20  ) #start   , end ,  number  of points  ( start  and end are  included )
print(c)

#common arrays 
d  =  np.ones((3 ,  3 ))
print(d)


#diagonal  metrix  
e  = np.eye(3)  #identity metrix  

print(e)

f  =  np.eye(3  , 2 )
print(f)


#diagonal  array  
g  = np.diag([1  , 3 , 44  ,56  ])
print(g)

print(np.diag(g))

#create  array  using  random function 
#create can  array  using given  shape  and cinstruct random  numbers  in it  

h  =  np.random.rand(5)  #uniform  distriuted  random number  
print(h)  


#gaussian sitributed random numbe r 
i = np.random.randn(60) 
print(i)


#slicing  
j = np.arange(10)  
print(j[1 : 9 : 2    ])


#we can also  combine assignemnt  and slicing  
k  = np.arange(10)
k[5  : ]  =  100 
print(k)


#fancy  indexing

m  = np.arange( 8) 
func = ( m  % 2  ==  0   )  
print(m[func]) 





