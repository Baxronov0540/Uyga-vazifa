# def f(x:int)-> None:
#     return(x)
# a=5
# # print(f(a))    
# def Max(a:int,b:int,c:int)->int:
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# print(Max(3,1,5)*100)    
# def modul(x:int)->int:
#     if x>=0:
#         return x
#     else:
#         return x*(-1)
# res=modul(-100)
# print(res)    

# """
# *args positional arguments
# **kwargs keywords arguments
# """
# def f(*args,**kwargs):
#     return args,kwargs
# print(f(4,5,6,bir=1,ikki=2))
#12
# def contains(x:int,l:list)-> int:
#     if x in l:
#         return True
#     else:
#         return False
# print(contains(1,[2,5,1,3,8,9]))    
#13
# def count_wovels(word:str)->int:
#     l="aeiouAEIOU"
#     k=0
#     for i in word:
#          if i in l:
#              k+=1
#     return k
# r=input("r= ")
# print(count_wovels(r))
#14
# def Reverse(word:str)->str:
#      return word[::-1]
# r=input("r= ")
# print(Reverse(r)) 
#15
# def power(base:int|float,exp:int|float):
#     return base**exp
# print(power(12,2.7))

#17
# def celious(k:int|float)->int|float:
#     return k-273
# print(celious(123))
#18
# def unique_elements(l:list)->set:
#     l1=list(set(l))
#     for i in l1 :
#         l.remove(i)
#     print(l,l1)        
#     return set(l1).difference(set(l))
# print(unique_elements([1,2,3,4,5,4,3,2,1]))            
#19           
def factorial(n:int)->int:
    