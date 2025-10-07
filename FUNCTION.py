# def factorial(n:int)->list:
#     l=[0,1]
#     for  i in range(2,n):
        
        
#      l.append(l[i-1]+l[i-2])
#     return l 
    
# print(factorial(10))
#21
# def sum_1(*args:tuple)->int:
#     s=0
#     for i in args:
#        if str(i)==i:
#            print("harfni qo'shib bo'lmaydi")
#        else:
#            s+=i
        
#     return s
# print(sum_1(1,2,3,4,"ewr","32434"))
   
#23


# def student(name:str,age:int,**kwargs:dict):
#     print(f"talaba ismi:{name} yoshi:{age}" )
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
      
 
# student("Asror",19,country="Uzbekistan",facultey="O'zMU")
#24
# def describe(animal:str,name=None)->str:
#     return f"{animal}:{name}"
# print(describe("it","Bobek"))
    
#25
# def average(*args:tuple)->int:
#     s=0
#     k=0
#     for i in args:
#        if str(i)==i:
#             "string"
#        else:
#            s+=i
#            k+=1
#     return s/k
# print(average(1,2,3,4,"ewe",232,"k"))            
    
#26
# def f(**kwargs:dict)->str:
#     for i,j in kwargs.items():
#         print(f"{i};{j}")
# f(j=1,k=2,l=3)
# def ak(*args:tuple,**kwargs:dict):
#     print("args elementlari:")
#     for i in args:
#         print(i)
        
#     print("kwargs elementlari:")    
#     for j ,i in kwargs.items():
#         print(j,":",i)
        
# ak(1 ,2 ,"dfd","wdwsr",bir=1,ikki=2,l=3)            
#28
# def arg(*args:tuple,belgi=None)->int:
#     if  belgi=="sum":
#      k=0   
#      for i in args:
#        if str(i)==i:
#            "ee"
#        else:
#            k+=i
#      return k       
#     else:
#         j=1
#         for i in args:
#             if str(i)==i:
#                 "erer"
#             else:
#                 j*=i
#         return j                           
# print(arg(1,2,3,4,5,6,"23234","sol",belgi="sm"))    
#30
# def build(*word):
#     for i in word:
#        print(i,end=" ")
       
# build(1,2,"srr","ewwre","eretr")       
# #31
# def sum_all(l:list)->list:
#     l=[i**2 for i in l]
#     return l
# print(sum_all([1,2,3,4,5]))
#32
# def invert_dict(d:dict)->dict:
#     d={j:i for i,j in d.items()}
#     return d
# print(invert_dict({"bir":1,"ikki":2}))
#33
# def  kesishma(set1:set,set2:set)->set:
#        k=set()
#        for i in set1:
#            if i in set2:
#                k.add(i)
#        return k 
# print(kesishma({1,2,3,4,5},{3,4,,5,6,7,8}))          
#34
# def l_t(l:list)->tuple:
#     return tuple(l)
# print(l_t([1,2,3,4,5,7]))
#35
# def D(d:dict,value)->str|int:
#     for i,j in d.items():
#         if j==value:
#             return i
# print(D({"bir":1,
#          "name":"Asror",
#          "age":19},19))
#36
# def filter(numbers:list)-> list:
#     numbers=[i for i in numbers if i%2==0 ]
#     return numbers
# print(filter([1,2,3,4,5,6,7,8]))
#37
# def long(words:list)->str:
#     k=len(words[0])
#     for i in words:
#         if len(i)>k:
#             k=len(i)
#             m=i
#     return   m
# print(long(["asror","python","salom","ozbekiston"]))      
#38
# def merge(d1:dict,d2:dict)->dict:
#     d1.update(d2)
#     return d1
# print(merge({"bir":1,"ikki":2},{"uch":3,"tort":4}))
#39
# def unikal(l:list)->int:
#     s=0
#     for i in range(len(l)):
#         k=0
#         for j in range(len(l)):
#             if l[i]==l[j] and i!=j :
#                 k+=1
#         if k==0:
#             s+=1   
#     return s            
# print(unikal([1,2,3,4,5,4,3])) 
#40
# def list_set(l:list)->set:
#     s=[]
#     for i in l:
#         if not i in s:
#            s.append(i)
#     return s
# print(list_set([1,1,2,3,3,1,5]))
#41

# def Tub(t:int)->bool:
#     i=2
#     k=False
#     while i<=t**0.5:
#         if t%i==0 and t!=2:
#             k=True
#             return False
#         i+=1
#     if not k:
#         return True
# print(Tub(2))        
#42
# def polindrom(l:int)->str:
#     if str(l)[::-1] ==str(l) :
#         return "polindorm son"
#     else:
#         "polindrom emas" 
# print(polindrom(3312))
      
#43
# def w_count(s:str)->dict:
#     s.split()
#     return {"word":len(s)}
# print(w_count("asror qanday zorma"))

#44
# def  char(s:str)->dict:
#     d=dict()
#     for i in s:
#         if  i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(char("asror"))                       
#45
#from typing import Iterable


# def word(words:list)->list:
#     for i in range(len(words)):
#         for j in range(0,len(words)):
#          if len(words[i])<len(words[j]):
#             words[i],words[j]=words[j],words[i]
#     return words        
# words=["asror","bexruz","as","boz"]        

# print(word(words))        
#46
# def max_(d:dict)->str:
#     k=0
#     for i ,j in d.items():
#          if j>k:
#              k=j
#              m=i
#     return i 
# print(max_({"bir":1,"ikki":2,"uch":3,"tort":4}))        
#47
# def is_valid(email:str)->bool:
#     if "@" in email and "." in email:
#         return True
#     else:
#         return False
# print(is_valid("@baxronovasror77.gmail.com"))    
    
#48
# def outter(x:int)->int:
#      return x**2
# def inner(y:int)->int:
#          return outter(2)+y
# print(outter(2),inner(5))     
#49
#50
# def grade(d:dict)->dict:
#     y=dict()
#     for i ,j in d.items():
#         s=0
#         for k,n in j.items():
#             s+=n
            
#         y.update({i:s/len(j)})
#     return y      
# print(grade({"eshmat":
#     {"math":90,
#      "sciense":75},
#     "gishmat":{
#         "math":80,
#         "sciense":70
#     }}))
