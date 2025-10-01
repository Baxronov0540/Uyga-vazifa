# t=(1,2,3,4,5)# t=(1,2,3,4,5)
# print(t)
#2
# t=(1,2,3,4,5)
# print(t[2])

#3
# t=(1,2,3,4,5)
# print(len(t))
#4
# fruits=("banan","apple","uzum","o'rik")
# print(fruits)
#5
# fruits=("banan","apple","uzum","o'rik")
# print( "bor " if "banan"in fruits else "yuq")
#6
# fruits=("banan","apple","uzum","o'rik")
# for i in fruits:
#     print(i)
#7
# num=(1,2,4,34,45)
# fruits=("banan","apple","uzum","o'rik")
# print(num + fruits)
#8
# num=(1,3,32,4,35,4,5,3,46463,3,54643,3)
# print(num.count(3))
#9
# rang=("red","green","blue")
# k1=rang[0]
# k2=rang[1]
# k3=rang[2]
# print(k1,k2,k3)
#10
# rang=("red","green","blue","yellow","brown","black","white","pink","orange")
# for i in enumerate(rang):
#     print(i)
#12
# t=("single",)
# print(t,type(t))
#13
# p=(10,5,20,15)
# j=p[0]
# for i in p:
#    if j<=i:
#       j=i
# print(j)      
#14
# a=("a","b","c")
# i=0
# while len(a)>i:
#     print(a[i])
#     i+=1
#15
# my_data=(("John",23),"Asror",19)
# print(my_data)
#16
# my_data=(("John",23),"Asror",19)
# for i in my_data:
#     if my_data[0]=="John":
#         print(my_data[1])

#187
# l=["milk","eggs","bread"]
# print(tuple(l))
#19
# n=int(input("sonni kiriting; "))
# t=(1,3,12,14,16,23,79,22,4,5,6,7,9,8,2)
# if n in t:
#     print("Bor")
# else:
#     print("Yuq")    
# #20
# print(tuple([i**2 for i in range(1,6)]))
###############################SET##################################################
# s={1,2,4,3,2}
# print(s)
#2
# s={1,2,4,3,2}
# s.add(5
# print(s)
#3
# s={1,2,4,3,2}
# s.add(6)
# s.add(7)
# print(s)

#4
# s={1,2,4,3,2}
# s.remove(3)
# print(s)
#5
# s={1,2,4,3,2}
# print(s.discard(10))
# print(s)
#6
# s={1,2,4,3,2}
# if 4 in s:
#     print("bor")
# else:
#     "yuq"    
#7
# set1={1,2,3,4}
# set2={4,5,6,7,8}
# print(set1,set2)
#8
# set1={1,2,3,4}
# set2={4,5,6,7,8}
# print(set1.union(set2))
#9
# set1={1,2,3,4}
# set2={4,5,6,7,8}
# print(set1.intersection(set1))
#10
# set1={1,2,3,4}
# set2={4,5,6,7,8}
# print(set1.difference(set2),set2.difference(set1))
#112
# l=[1,1,2,3,3,4]
# print(set(l))
#12
# set2={4,5,6,7,8}
# for i in set2:
#     print(i)
#13
# set1={1,2,3,4,4,5,6,7,8}
# n=int(input("n= "))
# if n in set1:
#     print("Bor")
# else:
#     print("Yuq")    
#14
# set1={1,2,3,4}
# set2={1,2,3,4,5}
# print(set1.issubset(set2))
#15
# set1={1,2,3,4}
# set2={1,2,3,4,5}
# print(set2.issuperset(set1))

#16  
# k=["a","b","c","a","e","b"]
# f=set()
# k1=[]
# for i in k:
#     if not i in f:
#         f.add(i)
#     else:
#         f.remove(i)    
# print(f)        
#17
# set2={1,2,3,4,5}
# set2.clear()
# print(set2)

#18
# s=set()
# for i in range(3):
#     n=input("yoqtirgan rangni kiritng; ")
#     s.add(n)
# print(s)    
# #19
# s={1,2,34,5}
# s1={21,4,1,2,5,7,21}
# print(s.symmetric_difference(s1))
#20
# print(set([i for i in range(1,11) if i%2==0]))
